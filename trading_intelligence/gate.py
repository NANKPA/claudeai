"""The owner's decision protocol (00_philosophy/decision-protocol.md, Gates 0-6) as code.

A trading bot calls `PhilosophyGate.evaluate(proposal, setup, account)` before it places any order.
The gate never places orders. It returns `take`, `skip` or `wait`, the reason for every gate with the
principle it enforces, the risk and position size when the answer is `take`, and a pre-trade journal
row in the format of 00_philosophy/journal-template.csv. Write that row (see journal.py) BEFORE the
order is sent: Section XVI's rule that the reasoning is recorded at the decision, not afterwards.

Education and decision support, not financial advice. Paper-trade a setup until its own
condition-matched record clears the gates; the gate is built to say "no" to everything else.
"""
from __future__ import annotations

import math
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone

P = {i: pid for i, pid in enumerate([
    "principle_01_understand_before_acting", "principle_02_context_before_movement",
    "principle_03_future_is_uncertain", "principle_04_conditional_probability",
    "principle_05_mathematical_justification", "principle_06_do_not_force",
    "principle_07_respond_methodically", "principle_08_decision_quality_not_outcome",
    "principle_09_protect_capital", "principle_10_emotional_independence",
    "principle_11_record_and_investigate", "principle_12_process_not_money"], start=1)}

EMOTION_COLOURS = {
    "green": {"calm", "focused"},
    "amber": {"tired", "distracted", "anxious", "carryover"},
    "red": {"frustrated", "overconfident", "fomo", "revenge"},
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


@dataclass
class SetupRecord:
    """A setup's condition-matched track record (the "setup card" of Gates 3-5).

    Count only trades that match the card's conditions and were NOT used to design the rules:
    out-of-sample backtest, forward (paper) or live trades. Either pass `results_r` (one net R
    multiple per trade, after costs) or the summary statistics (win rate, average win and loss in R
    before costs, and the average round-trip cost in R).
    """
    setup_id: str
    n: int = 0
    win_rate: float | None = None
    avg_win_r: float | None = None
    avg_loss_r: float = 1.0
    avg_cost_r: float = 0.0
    results_r: list[float] | None = None
    out_of_sample: bool = True
    source: str = "own"            # "own" (your backtest/journal) or "claimed" (someone else's numbers: T4)

    def stats(self) -> dict:
        """Mean net R, its standard error, and the inputs Gate 5 needs."""
        if self.results_r:
            r = [float(x) for x in self.results_r]
            n = len(r)
            mean = sum(r) / n
            sd = math.sqrt(sum((x - mean) ** 2 for x in r) / (n - 1)) if n > 1 else float("nan")
            wins = [x for x in r if x > 0]
            losses = [-x for x in r if x <= 0]
            p = len(wins) / n
            w = sum(wins) / len(wins) if wins else 0.0
            loss = sum(losses) / len(losses) if losses else 0.0
            # results are net: their average cost is already inside W and L
            return {"n": n, "mean_r": mean, "sd_r": sd, "p": p, "w": w, "l": loss, "c": 0.0,
                    "cost_inside": self.avg_cost_r, "net_results": True}
        if self.win_rate is None or self.avg_win_r is None:
            return {"n": 0, "mean_r": float("nan"), "sd_r": float("nan"), "p": float("nan"),
                    "w": float("nan"), "l": self.avg_loss_r, "c": self.avg_cost_r, "cost_inside": 0.0,
                    "net_results": False}
        p, w, loss, c = self.win_rate, self.avg_win_r, self.avg_loss_r, self.avg_cost_r
        mean = p * w - (1 - p) * loss - c
        sd = (w + loss) * math.sqrt(p * (1 - p))
        return {"n": int(self.n), "mean_r": mean, "sd_r": sd, "p": p, "w": w, "l": loss, "c": c,
                "cost_inside": 0.0, "net_results": False}


@dataclass
class TradeProposal:
    """One candidate trade, written the way Gates 1-3 ask: what is observed, what is inferred, what
    is claimed, where it is wrong, and which defined conditions are present."""
    setup_id: str
    instrument: str
    side: str                                  # "long" or "short"
    entry: float
    stop: float
    target: float
    cost_price: float | None = None            # expected round-trip friction in price units (spread+fees+slippage)
    timeframe: str = ""                        # the level the hypothesis is about (Gate 2)
    regime_tag: str = ""
    session: str = ""
    observation: str = ""                      # Gate 1: what is seen, without motive
    interpretation: str = ""                   # what it may mean
    hypothesis: str = ""                       # level, destination, horizon
    invalidation: str = ""                     # what would prove it wrong, written before entry
    explanation: str = ""                      # why it should work: a market mechanism
    undermined_by: str = ""                    # what would undermine the explanation
    required_conditions: list[str] = field(default_factory=list)
    conditions_present: dict[str, object] = field(default_factory=dict)   # name -> True / False / "borderline"
    evidence_for: list[str] = field(default_factory=list)
    evidence_against: list[str] = field(default_factory=list)            # unresolved arguments against
    value_gap_only: bool = False               # Section XV: the only evidence is "price is far from value"
    trade_id: str | None = None
    decided_at: str | None = None


@dataclass
class AccountState:
    equity: float
    point_value: float = 1.0                   # account currency per 1.0 price move per unit of size
    lot_step: float = 1.0                      # sizes are rounded DOWN to a multiple of this
    base_risk_pct: float = 0.5                 # percent of equity at risk per trade, set at the monthly review
    emotional_state: str = "calm"              # tags from the journal vocabulary, e.g. "calm,focused"
    step_back_when_amber: bool = False         # Gate 0: amber means step back instead of half risk
    realized_today_r: float = 0.0              # today's closed result in R (losses negative)
    realized_week_r: float = 0.0
    consecutive_losses_setup_session: int = 0
    drawdown_from_peak_pct: float = 0.0
    open_risk_pct: float = 0.0                 # risk already open ("heat"), correlated positions counted once
    minutes_since_last_loss: float | None = None


@dataclass
class Limits:
    """Example defaults from Gate 6.3. Write your own in the trading plan, before the session."""
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
    max_base_risk_pct: float = 1.0


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


def emotion_colour(tags: str) -> str:
    found = {t.strip().lower() for t in str(tags or "").replace(";", ",").split(",") if t.strip()}
    for colour in ("red", "amber", "green"):
        if found & EMOTION_COLOURS[colour]:
            return colour
    return "amber" if found else "unknown"    # unrecognised words count as amber; no tags at all is "unknown"


class PhilosophyGate:
    """Gates 0-6 of the decision protocol. `take` only when every gate passes."""

    def __init__(self, limits: Limits | None = None):
        self.limits = limits or Limits()

    def evaluate(self, t: TradeProposal, setup: SetupRecord | None, acct: AccountState) -> Decision:
        L = self.limits
        gates: list[GateResult] = []
        d = Decision(action="skip", gates=gates)
        decided_at = t.decided_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
        risk_mult = 1.0

        def finish(action: str) -> Decision:
            d.action = action
            d.journal_row = self._journal_row(t, d, acct, decided_at)
            return d

        # ── Gate 0: state and circuit breakers ──────────────────────────────
        colour = emotion_colour(acct.emotional_state)
        if colour == "red":
            gates.append(GateResult("0 State", "fail", f"state is red ({acct.emotional_state}): step back, reset, re-check",
                                    [P[10], P[12]]))
            return finish("skip")
        if colour == "unknown":
            gates.append(GateResult("0 State", "fail", "emotional state not recorded: classify it before deciding",
                                    [P[10], P[11]]))
            return finish("skip")
        if colour == "amber":
            if acct.step_back_when_amber:
                gates.append(GateResult("0 State", "fail", f"state amber ({acct.emotional_state}): stepping back", [P[10]]))
                return finish("skip")
            risk_mult *= 0.5
            gates.append(GateResult("0 State", "warn", f"state {colour} ({acct.emotional_state}): half risk", [P[10]]))
        else:
            gates.append(GateResult("0 State", "pass", "state green", [P[10]]))
        if acct.minutes_since_last_loss is not None and acct.minutes_since_last_loss < L.pause_after_loss_min:
            gates.append(GateResult("0 After-loss pause", "fail",
                                    f"{acct.minutes_since_last_loss:.0f} min since the last loss; pause {L.pause_after_loss_min:.0f} min, "
                                    "then re-run Gate 0", [P[10], P[12]]))
            return finish("wait")
        breakers = [
            (acct.realized_today_r <= -L.daily_loss_r, f"daily loss limit reached ({acct.realized_today_r:+.2f}R): session over"),
            (acct.realized_week_r <= -L.weekly_loss_r, f"weekly loss limit reached ({acct.realized_week_r:+.2f}R): week over"),
            (acct.consecutive_losses_setup_session >= L.max_consecutive_losses,
             f"{acct.consecutive_losses_setup_session} consecutive losses on this setup: off for the session"),
            (acct.drawdown_from_peak_pct >= L.drawdown_stop_pct,
             f"drawdown {acct.drawdown_from_peak_pct:.1f}% from peak: stop live trading, return to paper and review"),
        ]
        for hit, why in breakers:
            if hit:
                gates.append(GateResult("0/6 Circuit breaker", "fail", why, [P[9], P[10]]))
                return finish("skip")

        # ── Gate 1 + 2: ladder, level, invalidation (understanding) ─────────
        ladder = [t.observation.strip(), t.interpretation.strip(), t.hypothesis.strip()]
        ladder_ok = all(ladder) and len({x.lower() for x in ladder}) == 3
        side = t.side.lower()
        if side not in ("long", "short"):
            raise ValueError("side must be 'long' or 'short'")
        sign = 1 if side == "long" else -1
        stop_dist = (t.entry - t.stop) * sign
        target_dist = (t.target - t.entry) * sign
        geometry_ok = stop_dist > 0 and target_dist > 0
        if not t.invalidation.strip() or not geometry_ok:
            why = "no invalidation written before entry" if not t.invalidation.strip() else \
                "stop or target is on the wrong side of entry"
            gates.append(GateResult("2 Context & level", "fail", why, [P[3], P[2]]))
            d.understanding_score = 0
            return finish("skip")
        if not ladder_ok or not t.explanation.strip():
            d.understanding_score = 0
            gates.append(GateResult("1 Ladder", "fail", "observation / interpretation / hypothesis not written separately, "
                                    "or no explanation beyond 'it is moving'", [P[1], P[3]]))
        elif not t.undermined_by.strip() or not t.timeframe.strip():
            d.understanding_score = 1
            gates.append(GateResult("1-2 Ladder & level", "warn", "explanation has a gap: the level (timeframe) or what "
                                    "would undermine it is not stated", [P[1], P[2]]))
        else:
            d.understanding_score = 2
            gates.append(GateResult("1-2 Ladder & level", "pass", "ladder written, level named, invalidation set", [P[1], P[2], P[3]]))

        # ── Gate 3: conditions (evidence) ────────────────────────────────────
        req = list(t.required_conditions)
        present = {k: t.conditions_present.get(k) for k in req}
        missing = [k for k, v in present.items() if v is not True and str(v).lower() != "borderline"]
        borderline = [k for k, v in present.items() if str(v).lower() == "borderline"]
        if not req:
            d.evidence_score = 0
            gates.append(GateResult("3 Conditions", "fail", "no defined setup card with measured conditions applies", [P[4]]))
        elif missing or t.value_gap_only:
            d.evidence_score = 0
            why = f"required condition(s) absent: {', '.join(missing)}" if missing else \
                "the only evidence is a price-vs-value gap (Section XV: the start of an investigation, not an edge)"
            gates.append(GateResult("3 Conditions", "fail", why, [P[4]]))
        elif borderline or [x for x in t.evidence_against if x.strip()]:
            d.evidence_score = 1
            gates.append(GateResult("3 Conditions", "warn", "conditions present but borderline "
                                    f"({', '.join(borderline) or 'none'}) or an argument against is unresolved", [P[4]]))
        else:
            d.evidence_score = 2
            gates.append(GateResult("3 Conditions", "pass", "every required condition present and measured", [P[4]]))

        # ── Gate 4 + 5.4: the setup's record (mathematics) ───────────────────
        s = setup.stats() if setup else None
        if setup and setup.setup_id != t.setup_id:
            raise ValueError(f"setup record {setup.setup_id!r} does not match proposal setup {t.setup_id!r}")
        if s is None or not math.isfinite(s["mean_r"]):
            d.math_score, mdet = 0, "no condition-matched record for this setup"
        elif setup.source != "own" or not setup.out_of_sample:
            d.math_score, mdet = 0, "only in-sample or someone else's numbers (T4); they do not count"
        elif s["mean_r"] <= 0:
            d.math_score, mdet = 0, f"expectancy after costs is {s['mean_r']:+.3f}R"
        else:
            se = s["sd_r"] / math.sqrt(s["n"]) if s["n"] > 1 else float("inf")
            if s["n"] < L.min_trades:
                d.math_score, mdet = 1, f"n = {s['n']} < {L.min_trades}: an anecdote, worth testing, not trading"
            elif s["mean_r"] - se > 0:
                d.math_score, mdet = 2, f"n = {s['n']}, mean {s['mean_r']:+.3f}R, mean - 1 SE = {s['mean_r'] - se:+.3f}R > 0"
            else:
                d.math_score, mdet = 1, f"mean {s['mean_r']:+.3f}R but mean - 1 SE = {s['mean_r'] - se:+.3f}R <= 0"
        gates.append(GateResult("4 Record", {2: "pass", 1: "warn", 0: "fail"}[d.math_score], mdet, [P[5], P[4]]))

        # ── Gate 4: the three elements must agree ───────────────────────────
        scores = (d.understanding_score, d.evidence_score, d.math_score)
        if 0 in scores:
            gates.append(GateResult("4 Three elements", "fail", f"understanding/evidence/math = {scores}: a 0 means skip",
                                    [P[1], P[5], P[6]]))
            return finish("skip")
        if 1 in scores:
            gates.append(GateResult("4 Three elements", "warn", f"understanding/evidence/math = {scores}: investigate the "
                                    "contradiction; never settle it in favour of the trade you want", [P[6], P[1]]))
            return finish("wait")
        gates.append(GateResult("4 Three elements", "pass", "understanding, evidence and mathematics agree (2/2/2)", [P[1], P[5], P[6]]))

        # ── Gate 5.6: this trade's expected value ───────────────────────────
        target_r = target_dist / stop_dist
        cost_r = (t.cost_price / stop_dist) if t.cost_price is not None else s["c"] + s["cost_inside"]
        extra_cost = cost_r - s["cost_inside"] if s["net_results"] else cost_r
        w_trade = min(s["w"], target_r)
        ev = s["p"] * w_trade - (1 - s["p"]) * s["l"] - extra_cost
        d.est_win_prob, d.est_avg_win_r, d.est_avg_loss_r = round(s["p"], 4), round(w_trade, 3), round(s["l"], 3)
        d.est_cost_r, d.est_ev_r = round(cost_r, 3), round(ev, 3)
        if ev <= L.min_ev_r:
            d.math_score = 0
            gates.append(GateResult("5 Trade EV", "fail", f"EV after this trade's costs is {ev:+.3f}R "
                                    f"(target {target_r:.2f}R, cost {cost_r:.3f}R)", [P[5]]))
            return finish("skip")
        gates.append(GateResult("5 Trade EV", "pass", f"EV {ev:+.3f}R after costs (target {target_r:.2f}R, cost {cost_r:.3f}R)", [P[5]]))

        # ── Gate 6: size ────────────────────────────────────────────────────
        se = s["sd_r"] / math.sqrt(s["n"])
        factor = 1.0 if s["mean_r"] - 2 * se > 0 else 0.5
        if acct.drawdown_from_peak_pct >= L.drawdown_halve_pct:
            risk_mult *= 0.5
            gates.append(GateResult("6 Drawdown", "warn", f"drawdown {acct.drawdown_from_peak_pct:.1f}%: base risk halved", [P[9]]))
        risk = min(acct.base_risk_pct, L.max_base_risk_pct) * factor * risk_mult
        p_cons = s["p"] - math.sqrt(s["p"] * (1 - s["p"]) / s["n"])
        b = (w_trade - extra_cost) / (s["l"] + extra_cost) if (s["l"] + extra_cost) > 0 else float("inf")
        kelly = p_cons - (1 - p_cons) / b if b > 0 else -1.0
        if kelly <= 0:
            gates.append(GateResult("6 Kelly ceiling", "fail", f"Kelly from the conservative win rate ({p_cons:.3f}) is "
                                    f"{kelly:+.3f}: the edge cannot support any risk", [P[9], P[5]]))
            return finish("skip")
        risk = min(risk, L.kelly_fraction_cap * kelly * 100)
        room = L.max_heat_pct - acct.open_risk_pct
        if room <= 0:
            gates.append(GateResult("6 Heat", "fail", f"open risk {acct.open_risk_pct:.2f}% already at the "
                                    f"{L.max_heat_pct:.2f}% limit", [P[9]]))
            return finish("skip")
        risk = min(risk, room)
        raw = (acct.equity * risk / 100) / (stop_dist * acct.point_value)
        size = math.floor(raw / acct.lot_step + 1e-9) * acct.lot_step
        if size <= 0:
            gates.append(GateResult("6 Size", "fail", "stop too wide for the risk budget: size rounds to 0", [P[9]]))
            return finish("skip")
        d.position_size = round(size, 8)
        d.risk_pct = round(size * stop_dist * acct.point_value / acct.equity * 100, 4)
        gates.append(GateResult("6 Size", "pass", f"evidence factor {factor:g}, state/drawdown x{risk_mult:g}, "
                                f"1/4 Kelly cap {L.kelly_fraction_cap * kelly * 100:.2f}%: risk {d.risk_pct:.3f}%", [P[9]]))
        if acct.realized_today_r - 1 < -L.daily_loss_r:
            gates.append(GateResult("6 Daily limit", "warn", "a full 1R loss on this trade would pass the daily limit", [P[9]]))
        return finish("take")

    @staticmethod
    def _journal_row(t: TradeProposal, d: Decision, acct: AccountState, decided_at: str) -> dict:
        row = {c: "" for c in JOURNAL_COLUMNS}
        row.update({
            "trade_id": t.trade_id or f"{t.setup_id}-{decided_at.replace(':', '').replace('-', '')[:15]}",
            "decided_at": decided_at, "instrument": t.instrument, "timeframe": t.timeframe,
            "setup_id": t.setup_id, "regime_tag": t.regime_tag, "session": t.session,
            "observation": t.observation, "interpretation": t.interpretation, "hypothesis": t.hypothesis,
            "invalidation": t.invalidation, "evidence_for": "; ".join(t.evidence_for),
            "evidence_against": "; ".join(t.evidence_against + [g.detail for g in d.gates if g.status != "pass"]),
            "understanding_score": d.understanding_score, "evidence_score": d.evidence_score,
            "math_score": d.math_score, "est_win_prob": d.est_win_prob, "est_avg_win_r": d.est_avg_win_r,
            "est_avg_loss_r": d.est_avg_loss_r, "est_cost_r": d.est_cost_r, "est_ev_r": d.est_ev_r,
            "decision": d.action, "planned_entry": t.entry, "planned_stop": t.stop, "planned_target": t.target,
            "risk_pct": d.risk_pct if d.action == "take" else "", "position_size": d.position_size if d.action == "take" else "",
            "emotional_state_pre": acct.emotional_state,
        })
        return {k: ("" if v is None else v) for k, v in row.items()}
