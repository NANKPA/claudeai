"""The owner's decision protocol (00_philosophy/decision-protocol.md, Gates 0-6) as code.

A trading bot calls `PhilosophyGate.evaluate(proposal, setup, account)` before it places any order.
The gate never places orders. It returns `take`, `skip` or `wait`, the reason for every gate with the
principle it enforces, the risk and position size when the answer is `take`, and a pre-trade journal
row in the format of 00_philosophy/journal-template.csv. Write that row (see journal.py) BEFORE the
order is sent: Section XVI's rule that the reasoning is recorded at the decision, not afterwards.

The gate FAILS CLOSED: a missing, non-finite, out-of-range or ambiguous input is a `skip` with a
"0 Inputs" reason and a journal row, never an exception and never a `take`. Every check is written
so that the trade must prove it passes. Treat any exception from your own code around it as `skip`.

Sign conventions: prices and costs are positive; `realized_today_r` / `realized_week_r` are signed
results (losses negative); `drawdown_from_peak_pct` is read as a magnitude (-20 and 20 both mean 20%
below the peak); `open_risk_pct` is the total risk already open, >= 0.

Education and decision support, not financial advice. Paper-trade a setup until its own
condition-matched record clears the gates; the gate is built to say "no" to everything else.
"""
from __future__ import annotations

import math
import re
import uuid
from dataclasses import asdict, dataclass, field, fields, replace
from datetime import datetime, timezone

P = {i: pid for i, pid in enumerate([
    "principle_01_understand_before_acting", "principle_02_context_before_movement",
    "principle_03_future_is_uncertain", "principle_04_conditional_probability",
    "principle_05_mathematical_justification", "principle_06_do_not_force",
    "principle_07_respond_methodically", "principle_08_decision_quality_not_outcome",
    "principle_09_protect_capital", "principle_10_emotional_independence",
    "principle_11_record_and_investigate", "principle_12_process_not_money"], start=1)}

# The journal template's vocabulary, plus the emotions Section XII names (greed and excitement push
# risk beyond what the process justifies; fear abandons a valid process).
EMOTION_COLOURS = {
    "green": {"calm", "focused"},
    "amber": {"tired", "distracted", "anxious", "carryover", "fear", "fearful", "afraid", "scared", "nervous"},
    "red": {"frustrated", "overconfident", "fomo", "revenge", "greed", "greedy", "excited", "excitement",
            "euphoric", "angry", "tilt", "tilted"},
}
JOURNAL_COLUMNS = (
    "trade_id", "decided_at", "instrument", "timeframe", "setup_id", "regime_tag", "session",
    "observation", "interpretation", "hypothesis", "invalidation", "evidence_for",
    "evidence_against", "understanding_score", "evidence_score", "math_score", "est_win_prob",
    "est_avg_win_r", "est_avg_loss_r", "est_cost_r", "est_ev_r", "decision", "planned_entry",
    "planned_stop", "planned_target", "risk_pct", "position_size", "emotional_state_pre",
    "executed_per_plan", "exit_reason", "result_r", "cost_r", "mae_r", "mfe_r",
    "emotional_state_during", "outcome_within_expected", "lesson", "hypothesis_update", "reviewed_at",
)
PRE_TRADE_COLUMNS = JOURNAL_COLUMNS[:28]
UNCLEAR_REGIMES = {"", "unclear", "unknown", "none", "na", "n/a"}


class InputError(ValueError):
    """An input the gate refuses to reason about. evaluate() turns it into a skip."""


@dataclass
class SetupRecord:
    """A setup's condition-matched track record (the "setup card" of Gates 3-5).

    Count only trades that match the card's conditions and were NOT used to design the rules:
    out-of-sample backtest, forward (paper) or live trades. Either pass `results_r` (one NET R
    multiple per trade, after costs, plus `avg_cost_r`, the average cost already inside them) or the
    summary statistics (win rate, average win and loss in R BEFORE costs, the average round-trip
    cost in R and, if you have it, the recorded standard deviation of R).
    """
    setup_id: str
    n: int = 0
    win_rate: float | None = None
    avg_win_r: float | None = None
    avg_loss_r: float = 1.0                 # a positive magnitude
    avg_cost_r: float = 0.0
    sd_r: float | None = None               # recorded sd of R (Gate 5.3); the larger of it and the 2-point value is used
    results_r: list[float] | None = None
    out_of_sample: bool = True
    source: str = "own"                     # "own" (your backtest/journal) or "claimed" (someone else's numbers: T4)
    valid_regimes: list[str] | None = None  # regimes the record was measured in; today's must be one of them
    valid_sessions: list[str] | None = None

    def stats(self) -> dict:
        """Gross win/loss in R, cost in R, mean NET R, sd, n and win rate, after validation."""
        _finite_nonneg("avg_cost_r", self.avg_cost_r)
        if self.results_r:
            r = [float(x) for x in self.results_r]
            if not all(math.isfinite(x) for x in r):
                raise InputError("results_r contains a non-finite value")
            n = len(r)
            mean = sum(r) / n
            sd = math.sqrt(sum((x - mean) ** 2 for x in r) / (n - 1)) if n > 1 else float("nan")
            wins = [x for x in r if x > 0]
            losses = [-x for x in r if x <= 0]
            p = len(wins) / n
            c = float(self.avg_cost_r)
            w_net = sum(wins) / len(wins) if wins else 0.0
            l_net = sum(losses) / len(losses) if losses else 0.0
            # net -> gross: a net win is the gross win minus the cost; a net loss is the gross loss plus it
            return {"n": n, "mean_r": mean, "sd_r": sd, "p": p, "w": w_net + c, "l": max(l_net - c, 0.0), "c": c,
                    "losses": len(losses)}
        if self.win_rate is None or self.avg_win_r is None:
            return {"n": 0, "mean_r": float("nan"), "sd_r": float("nan"), "p": float("nan"),
                    "w": float("nan"), "l": float("nan"), "c": float(self.avg_cost_r), "losses": 0}
        p, w, loss, c = float(self.win_rate), float(self.avg_win_r), float(self.avg_loss_r), float(self.avg_cost_r)
        if not (math.isfinite(p) and 0.0 <= p <= 1.0):
            raise InputError(f"win_rate must be a probability in [0, 1], got {self.win_rate!r}")
        _finite_pos("avg_win_r", w)
        _finite_pos("avg_loss_r (a positive magnitude)", loss)
        n = int(self.n)
        if n < 0:
            raise InputError("n must be >= 0")
        mean = p * w - (1 - p) * loss - c
        sd = (w + loss) * math.sqrt(p * (1 - p))
        if self.sd_r is not None:
            _finite_nonneg("sd_r", self.sd_r)
            sd = max(sd, float(self.sd_r))
        return {"n": n, "mean_r": mean, "sd_r": sd, "p": p, "w": w, "l": loss, "c": c,
                "losses": round(n * (1 - p))}


@dataclass
class TradeProposal:
    """One candidate trade, written the way Gates 1-3 ask: what is observed, what is inferred, what
    is claimed, where it is wrong, and which defined conditions are present."""
    setup_id: str
    instrument: str
    side: str                                  # "long"/"buy" or "short"/"sell"
    entry: float
    stop: float
    target: float
    cost_price: float | None = None            # REQUIRED for a take: round-trip friction in price units
    timeframe: str = ""                        # the level the hypothesis is about (Gate 2): REQUIRED
    regime_tag: str = ""                       # REQUIRED; "unclear" means step back
    session: str = ""                          # REQUIRED
    observation: str = ""                      # Gate 1: what is seen, without motive
    interpretation: str = ""                   # what it may mean
    alternative_interpretation: str = ""       # Gate 1: the other reading that fits the same observation
    hypothesis: str = ""                       # level, destination (B), horizon
    horizon: str = ""                          # when B should be reached (Gate 2)
    invalidation: str = ""                     # what would prove it wrong, written before entry
    explanation: str = ""                      # why it should work: a market mechanism
    undermined_by: str = ""                    # what would undermine the explanation
    required_conditions: list[str] = field(default_factory=list)
    conditions_present: dict[str, object] = field(default_factory=dict)   # name -> True / False / "borderline"
    evidence_for: list[str] = field(default_factory=list)
    evidence_against: list[str] = field(default_factory=list)            # UNRESOLVED arguments against: block
    resolved_against: list[str] = field(default_factory=list)            # arguments checked and resolved: recorded
    value_gap_only: bool = False               # Section XV: the only evidence is "price is far from value"
    trade_id: str | None = None
    decided_at: str | None = None


@dataclass
class AccountState:
    equity: float
    emotional_state: str | None = None         # REQUIRED: tags from the journal vocabulary, e.g. "calm,focused"
    point_value: float = 1.0                   # account currency per 1.0 price move per unit of size
    lot_step: float = 1.0                      # sizes are rounded DOWN to a multiple of this
    base_risk_pct: float = 0.5                 # percent of equity at risk per trade, set at the monthly review
    step_back_when_amber: bool = False         # Gate 0: amber means step back instead of half risk
    trading_style: str = "intraday"            # "intraday" (pause in minutes) or "swing" (pause until the next session)
    realized_today_r: float = 0.0              # today's closed result in R (losses negative)
    realized_week_r: float = 0.0
    consecutive_losses_setup_session: int = 0
    drawdown_from_peak_pct: float = 0.0        # magnitude below peak equity
    open_risk_pct: float = 0.0                 # risk already open ("heat"), correlated positions counted once
    minutes_since_last_loss: float | None = None   # None = no loss today
    loss_this_session: bool = False            # swing style: a loss in the current session means wait


@dataclass(frozen=True)
class Limits:
    """Gate 6.3 example defaults. Write your own in the trading plan, before the session; never loosen
    them mid-session. Floors the protocol itself sets: n >= 30, Kelly fraction <= 1/2, EV floor >= 0."""
    daily_loss_r: float = 3.0
    weekly_loss_r: float = 5.0
    max_consecutive_losses: int = 3
    drawdown_halve_pct: float = 10.0
    drawdown_stop_pct: float = 20.0
    max_heat_pct: float = 2.0
    min_trades: int = 30
    min_ev_r: float = 0.0
    kelly_fraction_cap: float = 0.25
    pause_after_loss_min: float = 15.0
    max_base_risk_pct: float | None = None     # optional cap on base risk (shown as a warning when it binds)
    max_leverage: float | None = None          # optional cap on notional / equity

    def __post_init__(self):
        for f in fields(self):
            v = getattr(self, f.name)
            if v is None and f.name in ("max_base_risk_pct", "max_leverage"):
                continue
            if not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(v) or v < 0:
                raise InputError(f"Limits.{f.name} must be a finite number >= 0, got {v!r}")
        if self.min_trades < 30:
            raise InputError("Limits.min_trades cannot go below the protocol's floor of 30 (it may only be tightened)")
        if not 0 < self.kelly_fraction_cap <= 0.5:
            raise InputError("Limits.kelly_fraction_cap must be in (0, 0.5]: Kelly is a ceiling, 1/4 to 1/2 at most")
        for name in ("daily_loss_r", "weekly_loss_r", "max_heat_pct", "drawdown_stop_pct", "max_consecutive_losses"):
            if getattr(self, name) <= 0:
                raise InputError(f"Limits.{name} must be > 0")
        if self.drawdown_halve_pct > self.drawdown_stop_pct:
            raise InputError("Limits.drawdown_halve_pct must not exceed drawdown_stop_pct")

    # higher is looser for these; lower is looser for the rest
    _LOOSER_WHEN_HIGHER = ("daily_loss_r", "weekly_loss_r", "max_consecutive_losses", "drawdown_halve_pct",
                           "drawdown_stop_pct", "max_heat_pct", "kelly_fraction_cap", "max_base_risk_pct",
                           "max_leverage")

    def tightened(self, overrides: dict | None) -> tuple["Limits", list[str]]:
        """Apply only the overrides that make the limits stricter; return the ignored keys."""
        changes, ignored = {}, []
        for k, v in (overrides or {}).items():
            if not hasattr(self, k) or k.startswith("_"):
                ignored.append(f"{k} (unknown)")
                continue
            cur = getattr(self, k)
            if v is None or not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(v):
                ignored.append(f"{k} (not a finite number)")
                continue
            stricter = (cur is None or v < cur) if k in self._LOOSER_WHEN_HIGHER else v > cur
            if k == "pause_after_loss_min":
                stricter = v > cur
            (changes.__setitem__(k, v) if stricter else ignored.append(f"{k} (would loosen the plan)"))
        return replace(self, **changes), ignored


@dataclass
class GateResult:
    gate: str
    status: str            # "pass", "warn" or "fail"
    detail: str
    principles: list[str]


@dataclass
class Decision:
    action: str            # "take", "skip" or "wait"
    gates: list[GateResult]
    understanding_score: int | None = None
    evidence_score: int | None = None
    math_score: int | None = None
    est_win_prob: float | None = None
    est_avg_win_r: float | None = None
    est_avg_loss_r: float | None = None
    est_cost_r: float | None = None
    est_ev_r: float | None = None
    risk_pct: float | None = None
    position_size: float | None = None
    journal_row: dict = field(default_factory=dict)

    def explain(self) -> str:
        lines = [f"Decision: {self.action.upper()}"]
        for g in self.gates:
            lines.append(f"  [{g.status:4}] {g.gate}: {g.detail}")
        if self.action == "take":
            lines.append(f"  size {self.position_size} at {self.risk_pct:.3f}% risk; EV {self.est_ev_r:+.3f}R after costs")
        return "\n".join(lines)

    def to_dict(self) -> dict:
        return asdict(self)


def emotion_colour(tags: object) -> str:
    """red if any red tag; amber if any amber tag or any word outside the vocabulary; green only if
    every word is a green tag; "unknown" if nothing was recorded."""
    words = [w for w in re.split(r"[^a-z]+", str(tags or "").lower()) if w]
    if not words:
        return "unknown"
    if any(w in EMOTION_COLOURS["red"] for w in words):
        return "red"
    if any(w not in EMOTION_COLOURS["green"] for w in words):
        return "amber"
    return "green"


def _finite(name: str, v) -> float:
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(float(v)):
        raise InputError(f"{name} must be a finite number, got {v!r}")
    return float(v)


def _finite_pos(name: str, v) -> float:
    x = _finite(name, v)
    if not x > 0:
        raise InputError(f"{name} must be > 0, got {v!r}")
    return x


def _finite_nonneg(name: str, v) -> float:
    x = _finite(name, v)
    if not x >= 0:
        raise InputError(f"{name} must be >= 0, got {v!r}")
    return x


def _as_list(v) -> list[str]:
    if v is None:
        return []
    if isinstance(v, str):
        return [v] if v.strip() else []
    return [str(x) for x in v if str(x).strip()]


def _side(v) -> int:
    s = str(v or "").strip().lower()
    if s in ("long", "buy", "l"):
        return 1
    if s in ("short", "sell", "s"):
        return -1
    raise InputError(f"side must be long/buy or short/sell, got {v!r}")


class PhilosophyGate:
    """Gates 0-6 of the decision protocol. `take` only when every gate passes."""

    def __init__(self, limits: Limits | None = None):
        self.limits = limits or Limits()

    def evaluate(self, t: TradeProposal, setup: SetupRecord | None, acct: AccountState) -> Decision:
        gates: list[GateResult] = []
        d = Decision(action="skip", gates=gates)
        try:
            decided_at = t.decided_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
        except Exception:  # noqa: BLE001
            decided_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
        try:
            action = self._run(t, setup, acct, d, gates)
        except InputError as e:
            gates.append(GateResult("0 Inputs", "fail", f"refused: {e}", [P[11], P[9]]))
            action = "skip"
        except Exception as e:  # noqa: BLE001 - fail closed on anything unexpected
            gates.append(GateResult("0 Inputs", "fail", f"refused ({type(e).__name__}): {e}", [P[11], P[9]]))
            action = "skip"
        d.action = action
        if action != "take":
            d.risk_pct = d.position_size = None
        d.journal_row = self._journal_row(t, d, acct, decided_at)
        return d

    def _run(self, t: TradeProposal, setup: SetupRecord | None, acct: AccountState, d: Decision,
             gates: list[GateResult]) -> str:
        L = self.limits
        # ── inputs ─────────────────────────────────────────────────────────
        equity = _finite_pos("equity", acct.equity)
        point_value = _finite_pos("point_value", acct.point_value)
        lot_step = _finite_pos("lot_step", acct.lot_step)
        base_risk = _finite_pos("base_risk_pct", acct.base_risk_pct)
        entry = _finite_pos("entry", t.entry)
        stop = _finite_pos("stop", t.stop)
        target = _finite_pos("target", t.target)
        today = _finite("realized_today_r", acct.realized_today_r)
        week = _finite("realized_week_r", acct.realized_week_r)
        dd = abs(_finite("drawdown_from_peak_pct", acct.drawdown_from_peak_pct))
        heat = _finite_nonneg("open_risk_pct", acct.open_risk_pct)
        streak = _finite_nonneg("consecutive_losses_setup_session", acct.consecutive_losses_setup_session)
        sign = _side(t.side)
        if t.cost_price is not None:
            _finite_nonneg("cost_price", t.cost_price)
        if acct.minutes_since_last_loss is not None:
            _finite_nonneg("minutes_since_last_loss", acct.minutes_since_last_loss)

        # ── Gate 0: state, circuit breakers, then the after-loss pause ──────
        colour = emotion_colour(acct.emotional_state)
        if colour == "unknown":
            gates.append(GateResult("0 State", "fail", "emotional state not recorded: classify it before deciding", [P[10], P[11]]))
            return "skip"
        if colour == "red":
            gates.append(GateResult("0 State", "fail", f"state is red ({acct.emotional_state}): step back, reset, re-check",
                                    [P[10], P[12]]))
            return "skip"
        state_mult = 1.0
        if colour == "amber":
            if acct.step_back_when_amber:
                gates.append(GateResult("0 State", "fail", f"state amber ({acct.emotional_state}): stepping back", [P[10]]))
                return "skip"
            state_mult = 0.5
            gates.append(GateResult("0 State", "warn", f"state amber ({acct.emotional_state}): half the Gate 6 risk", [P[10]]))
        else:
            gates.append(GateResult("0 State", "pass", "state green", [P[10]]))
        breakers = [
            (not today > -L.daily_loss_r, f"daily loss limit reached ({today:+.2f}R): session over"),
            (not week > -L.weekly_loss_r, f"weekly loss limit reached ({week:+.2f}R): week over"),
            (not streak < L.max_consecutive_losses, f"{streak:g} consecutive losses on this setup: off for the session"),
            (not dd < L.drawdown_stop_pct, f"drawdown {dd:.1f}% from peak: stop live trading, return to paper and review"),
        ]
        for hit, why in breakers:
            if hit:
                gates.append(GateResult("0/6 Circuit breaker", "fail", why, [P[9], P[10]]))
                return "skip"
        style = str(acct.trading_style or "intraday").lower()
        if style == "swing":
            if acct.loss_this_session:
                gates.append(GateResult("0 After-loss pause", "fail", "a loss this session: wait for the next session, "
                                        "then re-run Gate 0", [P[10], P[12]]))
                return "wait"
        else:
            if acct.minutes_since_last_loss is None and today < 0:
                gates.append(GateResult("0 After-loss pause", "fail", "today has a loss but the time since it is unknown; "
                                        "record minutes_since_last_loss", [P[10]]))
                return "wait"
            if acct.minutes_since_last_loss is not None and not acct.minutes_since_last_loss >= L.pause_after_loss_min:
                gates.append(GateResult("0 After-loss pause", "fail",
                                        f"{acct.minutes_since_last_loss:.0f} min since the last loss; pause "
                                        f"{L.pause_after_loss_min:.0f} min, then re-run Gate 0", [P[10], P[12]]))
                return "wait"

        # ── Gate 1 + 2: ladder, level, invalidation (understanding) ─────────
        stop_dist = (entry - stop) * sign
        target_dist = (target - entry) * sign
        if not t.invalidation.strip():
            gates.append(GateResult("2 Context & level", "fail", "no invalidation written before entry", [P[3], P[2]]))
            d.understanding_score = 0
            return "skip"
        if not (stop_dist > 0 and target_dist > 0):
            gates.append(GateResult("2 Context & level", "fail", "stop or target is on the wrong side of entry", [P[3], P[2]]))
            d.understanding_score = 0
            return "skip"
        if not t.timeframe.strip():
            gates.append(GateResult("2 Context & level", "fail", "the level (timeframe) of the hypothesis is not named", [P[2]]))
            d.understanding_score = 0
            return "skip"
        ladder = [t.observation.strip(), t.interpretation.strip(), t.hypothesis.strip()]
        if not all(ladder) or len({x.lower() for x in ladder}) < 3 or not t.explanation.strip():
            d.understanding_score = 0
            gates.append(GateResult("1 Ladder", "fail", "observation / interpretation / hypothesis not written separately, "
                                    "or no explanation beyond 'it is moving'", [P[1], P[3]]))
        elif not (t.undermined_by.strip() and t.alternative_interpretation.strip() and t.horizon.strip()):
            d.understanding_score = 1
            gates.append(GateResult("1-2 Ladder & level", "warn", "explanation has a gap: the alternative interpretation, "
                                    "the horizon, or what would undermine it is not stated", [P[1], P[2]]))
        else:
            d.understanding_score = 2
            gates.append(GateResult("1-2 Ladder & level", "pass", "ladder written, level and horizon named, invalidation set",
                                    [P[1], P[2], P[3]]))

        # ── Gate 3: conditions (evidence) ────────────────────────────────────
        req = _as_list(t.required_conditions)
        present = dict(t.conditions_present or {})
        missing = [k for k in req if present.get(k) is not True and str(present.get(k)).lower() != "borderline"]
        borderline = [k for k in req if str(present.get(k)).lower() == "borderline"]
        regime = str(t.regime_tag or "").strip().lower()
        session = str(t.session or "").strip().lower()
        unresolved = _as_list(t.evidence_against)
        if regime in UNCLEAR_REGIMES or not session:
            d.evidence_score = 0
            gates.append(GateResult("3 Conditions", "fail", "regime unclear or session not tagged: stand aside", [P[4], P[6]]))
        elif not req:
            d.evidence_score = 0
            gates.append(GateResult("3 Conditions", "fail", "no defined setup card with measured conditions applies"
                                    + (" (a price-vs-value gap alone is not evidence, Section XV)" if t.value_gap_only else ""),
                                    [P[4]]))
        elif missing:
            d.evidence_score = 0
            gates.append(GateResult("3 Conditions", "fail", f"required condition(s) absent: {', '.join(missing)}", [P[4]]))
        elif setup is not None and setup.valid_regimes and regime not in {x.strip().lower() for x in setup.valid_regimes}:
            d.evidence_score = 0
            gates.append(GateResult("3 Conditions", "fail", f"today's regime '{regime}' is not one the record was measured in "
                                    f"({', '.join(setup.valid_regimes)})", [P[4]]))
        elif setup is not None and setup.valid_sessions and session not in {x.strip().lower() for x in setup.valid_sessions}:
            d.evidence_score = 0
            gates.append(GateResult("3 Conditions", "fail", f"today's session '{session}' is not one the record was measured in",
                                    [P[4]]))
        elif borderline or unresolved:
            d.evidence_score = 1
            gates.append(GateResult("3 Conditions", "warn", "conditions present but borderline "
                                    f"({', '.join(borderline) or 'none'}) or an argument against is unresolved", [P[4]]))
        else:
            d.evidence_score = 2
            gates.append(GateResult("3 Conditions", "pass", "every required condition present and measured", [P[4]]))

        # ── Gate 4 + 5.4: the setup's record (mathematics) ───────────────────
        if setup is not None and setup.setup_id != t.setup_id:
            raise InputError(f"setup record {setup.setup_id!r} does not match proposal setup {t.setup_id!r}")
        s = setup.stats() if setup is not None else None
        if s is None or not math.isfinite(s["mean_r"]):
            d.math_score, mdet = 0, "no condition-matched record for this setup"
        elif setup.source != "own" or not setup.out_of_sample:
            d.math_score, mdet = 0, "only in-sample or someone else's numbers (T4); they do not count"
        elif not s["mean_r"] > 0:
            d.math_score, mdet = 0, f"expectancy after costs is {s['mean_r']:+.3f}R"
        elif s["n"] < L.min_trades:
            d.math_score, mdet = 1, f"n = {s['n']} < {L.min_trades}: an anecdote, worth testing, not trading"
        elif s["losses"] < 1 or not (math.isfinite(s["sd_r"]) and s["sd_r"] > 0):
            d.math_score, mdet = 1, "the record has no losses or no variation: it cannot measure risk yet"
        else:
            se = s["sd_r"] / math.sqrt(s["n"])
            if s["mean_r"] - se > 0:
                d.math_score, mdet = 2, f"n = {s['n']}, mean {s['mean_r']:+.3f}R, mean - 1 SE = {s['mean_r'] - se:+.3f}R > 0"
            else:
                d.math_score, mdet = 1, f"mean {s['mean_r']:+.3f}R but mean - 1 SE = {s['mean_r'] - se:+.3f}R <= 0"
        gates.append(GateResult("4 Record", {2: "pass", 1: "warn", 0: "fail"}[d.math_score], mdet, [P[5], P[4]]))

        # ── Gate 4: the three elements must agree ───────────────────────────
        scores = (d.understanding_score, d.evidence_score, d.math_score)
        if 0 in scores:
            gates.append(GateResult("4 Three elements", "fail", f"understanding/evidence/math = {scores}: a 0 means skip",
                                    [P[1], P[5], P[6]]))
            return "skip"
        if 1 in scores:
            gates.append(GateResult("4 Three elements", "warn", f"understanding/evidence/math = {scores}: investigate the "
                                    "contradiction; never settle it in favour of the trade you want", [P[6], P[1]]))
            return "wait"
        gates.append(GateResult("4 Three elements", "pass", "understanding, evidence and mathematics agree (2/2/2)",
                                [P[1], P[5], P[6]]))

        # ── Gate 5.6: this trade's expected value (gross W and L, this trade's cost) ──
        if t.cost_price is None:
            gates.append(GateResult("5 Trade EV", "fail", "this trade's cost in R is not checked: give cost_price "
                                    "(spread + fees + slippage, in price units)", [P[5]]))
            d.math_score = 0
            return "skip"
        target_r = target_dist / stop_dist
        cost_r = float(t.cost_price) / stop_dist
        w_trade = min(s["w"], target_r)
        ev = s["p"] * w_trade - (1 - s["p"]) * s["l"] - cost_r
        d.est_win_prob, d.est_avg_win_r, d.est_avg_loss_r = round(s["p"], 4), round(w_trade, 4), round(s["l"], 4)
        d.est_cost_r, d.est_ev_r = round(cost_r, 4), round(ev, 4)
        if not (math.isfinite(ev) and ev > L.min_ev_r):
            d.math_score = 0
            gates.append(GateResult("5 Trade EV", "fail", f"EV after this trade's costs is {ev:+.3f}R "
                                    f"(target {target_r:.2f}R, cost {cost_r:.3f}R)", [P[5]]))
            return "skip"
        gates.append(GateResult("5 Trade EV", "pass", f"EV {ev:+.3f}R after costs (target {target_r:.2f}R, cost {cost_r:.3f}R)",
                                [P[5]]))

        # ── Gate 6: size ────────────────────────────────────────────────────
        se = s["sd_r"] / math.sqrt(s["n"])
        factor = 1.0 if s["mean_r"] - 2 * se > 0 else 0.5
        dd_mult = 0.5 if dd >= L.drawdown_halve_pct else 1.0
        if dd_mult < 1:
            gates.append(GateResult("6 Drawdown", "warn", f"drawdown {dd:.1f}%: base risk halved", [P[9]]))
        base = base_risk
        if L.max_base_risk_pct is not None and base > L.max_base_risk_pct:
            gates.append(GateResult("6 Base risk cap", "warn", f"base risk {base:g}% capped at the plan's "
                                    f"{L.max_base_risk_pct:g}%", [P[9]]))
            base = L.max_base_risk_pct
        p_cons = s["p"] - math.sqrt(s["p"] * (1 - s["p"]) / s["n"])
        denom = s["l"] + cost_r
        kelly = (p_cons - (1 - p_cons) / ((w_trade - cost_r) / denom)) if (denom > 0 and w_trade - cost_r > 0) else -1.0
        if not (math.isfinite(kelly) and kelly > 0):
            gates.append(GateResult("6 Kelly ceiling", "fail", f"Kelly from the conservative win rate ({p_cons:.3f}) is "
                                    f"{kelly:+.3f}: the edge cannot support any risk", [P[9], P[5]]))
            return "skip"
        kelly_cap = L.kelly_fraction_cap * kelly * 100
        room = L.max_heat_pct - heat
        if not room > 0:
            gates.append(GateResult("6 Heat", "fail", f"open risk {heat:.2f}% already at the {L.max_heat_pct:.2f}% limit", [P[9]]))
            return "skip"
        risk = min(base * factor * dd_mult, kelly_cap, room) * state_mult     # amber halves the final Gate 6 risk
        raw = (equity * risk / 100) / (stop_dist * point_value)
        size = math.floor(raw / lot_step + 1e-9) * lot_step
        actual = size * stop_dist * point_value / equity * 100
        if not (size > 0 and math.isfinite(actual)):
            gates.append(GateResult("6 Size", "fail", "stop too wide for the risk budget: size rounds to 0", [P[9]]))
            return "skip"
        if not actual <= risk + 1e-9:
            gates.append(GateResult("6 Size", "fail", f"rounded size would risk {actual:.3f}% > budget {risk:.3f}%", [P[9]]))
            return "skip"
        if L.max_leverage is not None and not size * entry * point_value <= L.max_leverage * equity:
            gates.append(GateResult("6 Leverage", "fail", f"notional {size * entry * point_value:,.0f} exceeds "
                                    f"{L.max_leverage:g}x equity", [P[9]]))
            return "skip"
        d.position_size = round(size, 8)
        d.risk_pct = round(actual, 4)
        gates.append(GateResult("6 Size", "pass", f"evidence factor {factor:g}, drawdown x{dd_mult:g}, state x{state_mult:g}, "
                                f"1/4 Kelly cap {kelly_cap:.2f}%, heat room {room:.2f}%: risk {d.risk_pct:.3f}%", [P[9]]))
        if today - 1 <= -L.daily_loss_r:
            gates.append(GateResult("6 Daily limit", "warn", "a full 1R loss on this trade would reach the daily limit", [P[9]]))
        return "take"

    @staticmethod
    def _journal_row(t: TradeProposal, d: Decision, acct: AccountState, decided_at: str) -> dict:
        def g(obj, name, default=""):
            try:
                v = getattr(obj, name)
                return default if v is None else v
            except Exception:  # noqa: BLE001
                return default
        stamp = re.sub(r"[^0-9T]", "", str(decided_at))[:15]
        tid = g(t, "trade_id") or f"{g(t, 'setup_id', 'setup')}-{g(t, 'instrument', 'x')}-{stamp}-{uuid.uuid4().hex[:6]}"
        against = _as_list(g(t, "evidence_against", [])) + [f"resolved: {x}" for x in _as_list(g(t, "resolved_against", []))]
        against += [f"{x.gate}: {x.detail}" for x in d.gates if x.status != "pass"]
        row = {c: "" for c in JOURNAL_COLUMNS}
        row.update({
            "trade_id": tid, "decided_at": decided_at, "instrument": g(t, "instrument"), "timeframe": g(t, "timeframe"),
            "setup_id": g(t, "setup_id"), "regime_tag": g(t, "regime_tag"), "session": g(t, "session"),
            "observation": g(t, "observation"),
            "interpretation": g(t, "interpretation") + (f" | alternative: {t.alternative_interpretation}"
                                                        if str(g(t, "alternative_interpretation")).strip() else ""),
            "hypothesis": g(t, "hypothesis") + (f" | horizon: {t.horizon}" if str(g(t, "horizon")).strip() else ""),
            "invalidation": g(t, "invalidation"), "evidence_for": "; ".join(_as_list(g(t, "evidence_for", []))),
            "evidence_against": "; ".join(against),
            "understanding_score": d.understanding_score, "evidence_score": d.evidence_score,
            "math_score": d.math_score, "est_win_prob": d.est_win_prob, "est_avg_win_r": d.est_avg_win_r,
            "est_avg_loss_r": d.est_avg_loss_r, "est_cost_r": d.est_cost_r, "est_ev_r": d.est_ev_r,
            "decision": d.action, "planned_entry": g(t, "entry"), "planned_stop": g(t, "stop"), "planned_target": g(t, "target"),
            "risk_pct": d.risk_pct if d.action == "take" else "",
            "position_size": d.position_size if d.action == "take" else "",
            "emotional_state_pre": g(acct, "emotional_state"),
        })
        return {k: ("" if v is None else v) for k, v in row.items()}
