---
id: framework_decision_protocol
type: framework
title: "Decision Protocol — the Philosophy of the Relationship as an operating procedure"
partition: 00_philosophy
layer: L5
related: [philosophy_relationship, philo_practical_doctrine, philo_source_of_opportunity, philo_step_back, philo_evidence_changes, philo_capital_preservation, synthesis_unified_framework, synthesis_pre_trade_checklist, framework_trading_journal]
uses: [concept_expectancy, concept_position_sizing, concept_risk_reward_r_multiples, concept_trade_management, concept_trading_plan, concept_trading_psychology, concept_market_regimes, concept_multi_timeframe_analysis]
status: synthesized
---

# Decision Protocol

> **Education, not financial advice.** This protocol turns the owner's
> philosophy ([[philosophy_relationship]]) into a working procedure. Every
> number in it is either a formula, a default for the owner to set, or a
> clearly labelled hypothetical. None of it describes the real win rate or
> P&L of any strategy.

The philosophy states *what to believe*. This document states *what to do,
in what order, and what to write down*. A trade candidate passes through
nine gates (0 to 8). Each gate asks one question, names the principle of
Section XVIII ([[philo_practical_doctrine]]) it enforces, and points to the
knowledge-base concepts that supply its tools. Every answer is written into
the journal ([[framework_trading_journal]]) before the order is sent.

The manifesto ends with the aim of understanding the market "well enough
to know when to act, when to wait, and when I am wrong" (Section XXI,
[[philo_manifesto]]). The protocol gives each of the three a written form:
`take` after Gate 6, `skip` or `wait` on the Step-back path, and the
invalidation condition fixed in Gate 2 before entry.

## How the protocol works

Three rules hold the gates together.

1. **A gate is a question with a written answer.** If the answer cannot be
   written in plain words, the gate has failed. A feeling of confidence is
   not an answer.
2. **A failed gate is a decision, not a deduction.** The master checklist
   ([[synthesis_pre_trade_checklist]]) lets a trade through at 7/10. This
   protocol is stricter, because the philosophy is: when understanding,
   evidence and mathematics disagree, the trade is not forced
   ([[principle_06_do_not_force]]). A failed gate sends the candidate down
   the **Step-back path** with a recorded `skip` or `wait`.
3. **Pre-trade answers are frozen.** They are written before entry,
   timestamped (`decided_at`), and never edited afterwards. Section XVI
   ([[philo_journal]]) explains why: reasoning reconstructed after the
   result is hindsight dressed up as analysis.

```
            ┌────────────────────────── any gate fails ──────────────────────────┐
            │                                                                     ▼
 Gate 0 → Gate 1 → Gate 2 → Gate 3 → Gate 4 → Gate 5 → Gate 6 ──► ENTRY ──► Gate 7 ──► Gate 8
 state    ladder   context  conditions three   maths    size          execute /    review
                   & level             elements                       evidence
                                                                      changed
            STEP BACK (skip / wait) ── written as a journal row ── reviewed in Gate 8 too
```

### Map of the gates

| Gate | The question | Principles enforced | Philosophy | Layer | Journal fields written |
|---|---|---|---|---|---|
| 0 State check | Am I in a state to decide at all? | [[principle_10_emotional_independence]], [[principle_12_process_not_money]] | XII, XIII | L7 | `emotional_state_pre` |
| 1 Ladder | What do I see, what do I infer, what do I claim? | [[principle_01_understand_before_acting]], [[principle_03_future_is_uncertain]], [[principle_05_mathematical_justification]] | IV, I | L1/L3 | `observation`, `interpretation`, `hypothesis` |
| 2 Context & level | Which level is the claim about, and where is it wrong? | [[principle_02_context_before_movement]], [[principle_03_future_is_uncertain]] | III, II | L2 | `timeframe`, `invalidation`, `planned_stop`, `planned_target` |
| 3 Conditions | Does today match the measured conditions of a defined setup? | [[principle_04_conditional_probability]] | V, VI | L2/L4 | `setup_id`, `regime_tag`, `session`, `evidence_for`, `evidence_against` |
| 4 Three elements | Do understanding, evidence and mathematics agree? | [[principle_01_understand_before_acting]], [[principle_05_mathematical_justification]], [[principle_06_do_not_force]] | VIII, XV | L4 | `understanding_score`, `evidence_score`, `math_score` |
| 5 Mathematics | Is the expected value positive after costs, given the estimate's uncertainty? | [[principle_05_mathematical_justification]], [[principle_04_conditional_probability]] | VII, VI | L0/L6 | `est_win_prob`, `est_avg_win_r`, `est_avg_loss_r`, `est_cost_r`, `est_ev_r` |
| 6 Size | Can I be wrong, repeatedly, and still continue? | [[principle_09_protect_capital]], [[principle_10_emotional_independence]] | XIV | L6 | `decision`, `planned_entry`, `risk_pct`, `position_size` |
| 7 Execute | Am I following the plan, and what do I do when the evidence changes? | [[principle_07_respond_methodically]], [[principle_02_context_before_movement]], [[principle_12_process_not_money]], [[principle_09_protect_capital]] | X, XIII | L5 | `executed_per_plan`, `exit_reason`, `mae_r`, `mfe_r`, `emotional_state_during` |
| 8 Review | Was the decision good, separately from the result? What changes? | [[principle_08_decision_quality_not_outcome]], [[principle_11_record_and_investigate]] | XI, XVI, XVII | L8 | `result_r`, `cost_r`, `outcome_within_expected`, `lesson`, `hypothesis_update`, `reviewed_at` |
| Step back | Not trading is a decision | [[principle_06_do_not_force]], [[principle_01_understand_before_acting]], [[principle_10_emotional_independence]] | IX, XIII | L7 | `decision` = `skip` or `wait` |

The layers are those of the knowledge base's stack ([[framework_ontology]]);
the gates follow the analysis-to-execution order of
[[synthesis_unified_framework]].

---

## Gate 0 — State check

**Enforces:** [[principle_10_emotional_independence]],
[[principle_12_process_not_money]] · **Philosophy:** XII
([[philo_protect_process]]), XIII ([[philo_decisions_not_money]]) ·
**Concepts:** [[concept_trading_psychology]], [[concept_probabilistic_thinking]],
[[concept_trading_plan]], [[concept_risk_of_ruin_drawdown]]

Section XII names the four emotions that hijack a method: fear, greed,
frustration and excitement. It also describes two moments of particular
pressure: just after a loss (the urge to recover) and just after a win
(confidence that outruns the evidence). Gate 0 runs before any chart work,
and again before each new candidate.

**Ask, and answer in writing:**

1. Am I trying to win back a loss, or to "make the day" a certain amount?
2. Am I looking at the market because a setup may appear, or because I feel
   I must be doing something?
3. Is anything carried over from a previous session (a loss, an argument, a
   missed move)?
4. Have I slept, eaten, and am I free of distraction for the session window?
5. How much of today's and this week's loss limit is already used (Gate 6)?
6. If the next trade loses a full 1R, will I accept that calmly, in advance?

**Classify the state** and write it in `emotional_state_pre` (vocabulary in
the journal template):

| State | Tags | What follows |
|---|---|---|
| Green | `calm`, `focused` | Proceed to Gate 1. |
| Amber | `tired`, `distracted`, `anxious`, `carryover` | Either step back, or trade at half the Gate 6 risk. Write which, and why, before Gate 1. |
| Red | `frustrated`, `overconfident`, `fomo`, `revenge` | Step back. No new candidate until a reset is done and the state is re-checked. |

**After-loss rules** (Section XII: the desire to recover money becomes
stronger than the desire to follow the method):

- The next trade is sized by Gate 6 exactly as any other trade. A smaller
  account produces a smaller position automatically. Size is never
  increased to recover.
- Take a fixed pause before the next evaluation (default: 15 minutes
  intraday, the next session for swing trades). Re-run Gate 0 afterwards.
- A loss carries no information about the next trade. The next candidate
  must justify itself through the gates on its own.
- After the plan's number of consecutive losses in a session (default 3),
  the session is over for that setup. After the daily or weekly loss
  limit, the session or week is over for every setup.
- If the thought "I need to get this back" appears, the state is red.

**After-win rules** (Section XII: after a win the trader may raise risk,
abandon rules, or take trades that would previously have been rejected):

- `risk_pct` never changes because of recent P&L. Base risk changes only at
  the monthly review, from evidence (Gate 6.2).
- Profits are equity, not "house money". They are sized identically.
- Before the next candidate, ask: *would I have taken this trade before the
  win?* If the honest answer is no, it is a skip.
- Whether to stop after a large win is a question for the journal, not for
  the moment: the monthly review can compare trades taken just after a win
  with the rest. If they are measurably worse, add a post-win stop to the
  plan.

**Practitioner echoes (T2, paraphrased).** Jared Tendler's playbook
([[strategy_jared_tendler_psychology]]) treats emotional carryover from
earlier sessions as a risk in itself, and prescribes a mid-session reset
(name the emotion, move, refocus, then allow at most one small trade or a
15-minute break) whose limit, once broken, ends the session. Mark Douglas
([[book_trading_in_the_zone]]) asks the trader to accept a trade's risk
fully before entering it. Umar Ashraf's development framework
([[strategy_umar_ashraf_5_stage]]) singles out ego and revenge trading as
the hazard of the developing stage.

---

## Gate 1 — Observation → interpretation → hypothesis → decision

**Enforces:** [[principle_01_understand_before_acting]],
[[principle_03_future_is_uncertain]], [[principle_05_mathematical_justification]]
· **Philosophy:** IV ([[philo_price_expression]]), I
([[philo_market_is_relationship]]) · **Concepts:**
[[concept_market_microstructure]], [[concept_auction_market_theory]],
[[concept_order_flow]], [[concept_price_action]]

Section IV separates four stages of reasoning and warns that an error at one
stage spoils everything after it. Price shows the terms on which
participants were willing and able to trade; it does not show their reasons.
So each rung is written **separately**, in its own journal field.

| Rung | What it is | Test it must pass | Typical error |
|---|---|---|---|
| **Observation** (`observation`) | What is on the screen, measured. | Another trader could verify it from the chart alone. It contains numbers (levels, sizes, times) and no motives. | Writing a motive as a fact: "institutions are buying", "smart money trapped sellers". Words that name a motive belong on the next rung. |
| **Interpretation** (`interpretation`) | What the observation *may* mean about the relationship between buyers and sellers. | It is phrased as possibility ("may", "suggests") and names at least one **alternative** interpretation. | One story, stated with certainty. |
| **Hypothesis** (`hypothesis`) | A testable claim about what happens next. | It names the level (timeframe) it is about, the destination B, the time horizon, and it is specific enough to be proved wrong. | "It should go up." No level, no horizon, no way to be wrong. |
| **Decision** (`decision`) | `take`, `skip` or `wait`. | Written last, after Gates 2 to 6. | Deciding first and then filling the rungs to fit. |

The owner's own example in Section IV is the template: price has risen
substantially (observation); buying pressure *may* be increasing
(interpretation); conditions *may* favour further upside (hypothesis); enter
only if the hypothesis, the evidence, the probability estimate and the risk
justify it (decision).

**Gate 1 fails** when the observation cannot be stated without a motive,
when no alternative interpretation can be named, or when the hypothesis
cannot be phrased so that it could be wrong. Fail → Step back
(Section IX: do not trade what you do not understand).

---

## Gate 2 — Context and level (A → C → B)

**Enforces:** [[principle_02_context_before_movement]],
[[principle_03_future_is_uncertain]] · **Philosophy:** III
([[philo_acb_principle]]), II ([[philo_market_system_of_rules]]) ·
**Concepts:** [[concept_multi_timeframe_analysis]], [[concept_market_structure]],
[[concept_market_regimes]], [[concept_volatility]],
[[concept_support_resistance]], [[concept_trade_management]]

Section III makes two claims that pull in opposite directions, and this gate
holds both. A path from A to B may pass through an adverse leg C that is
fully consistent with the larger hypothesis. But B is a *hypothesized*
destination, not a promised one; not every adverse move is a detour. The
only way to tell the two apart in real time is to define, **before entry**,
what each would look like.

**Answer five questions in writing:**

1. **Which level is the hypothesis about?** Name the timeframe on which B is
   defined (for example the 1-hour structure), and the timeframe used for
   the trigger. Record both in `timeframe` (for example `1h/5m`). A 5-minute
   signal does not get to invalidate a 1-hour hypothesis, and a 1-hour
   hypothesis does not excuse ignoring a 1-hour invalidation.
2. **Where is B, and by when?** A price level plus a time horizon. The
   horizon comes from the setup's record of time-to-target where one
   exists. B is written in `planned_target` and cannot be moved further
   away during the trade unless the plan already contains a trailing rule.
3. **What does C, movement within structure, look like?** Define the normal
   adverse range in measured units. Best: from the setup's record, the
   adverse excursion (MAE) that winning trades usually show (for example
   their 80th percentile). Before a record exists: a provisional band in
   ATR multiples ([[concept_volatility]]).
4. **What counts as structural change?** Write the specific signals that
   would mean the structure itself has changed, not just wobbled.
5. **What is the invalidation condition?** Written in `invalidation`. It has
   up to three parts: a **price** condition (a close, not a wick, beyond a
   named level on the hypothesis timeframe), a **structure or condition**
   test (for example, the regime flips), and a **time** condition (B not
   reached by the horizon means the hypothesis is stale).

| Movement within structure (C) | Evidence the structure changed |
|---|---|
| Adverse move inside the measured MAE band | Close beyond the invalidation level on the hypothesis timeframe |
| No acceptance beyond the key level (price returns quickly) | Acceptance: time and volume build beyond the level ([[concept_auction_market_theory]]) |
| The reason for the hypothesis is still observable | The reason is gone: the condition set of Gate 3 no longer holds |
| Speed and size inside the setup's recorded range | Speed or size far outside the recorded range, or a new factor (unscheduled news, [[concept_news_trading]]) |

**The stop goes where the hypothesis is wrong**, not where the loss starts
to hurt (master checklist item 7). If the honest stop is so far away that
Gate 6 produces a position too small to be worth the costs, the candidate
fails. The stop is never tightened to make the size work.

**Gate 2 fails** when the level of the hypothesis cannot be named, or when
the invalidation cannot be written as a checkable condition. Fail → Step
back.

---

## Gate 3 — Conditions

**Enforces:** [[principle_04_conditional_probability]] · **Philosophy:** VI
([[philo_conditional_probability]]), V ([[philo_recurring_storyline]]) ·
**Concepts:** [[concept_market_regimes]], [[concept_volatility]],
[[concept_trading_sessions_killzones]], [[concept_news_trading]],
[[concept_multi_timeframe_analysis]], [[concept_edge]] · **Open questions:**
[[question_define_conditions]], [[question_repeatable_behaviors]]

Section VI says a probability is only meaningful for a defined situation,
and Section V says a pattern seen before matters only if today's conditions
are sufficiently similar to those in which it showed an advantage. So a
trade is never taken on "a setup that looks familiar". It is taken on a
**setup card**: a written definition whose conditions are measurable, with a
record attached.

```
setup_id:        sweep-reversal-v1            (version suffix is mandatory)
claim:           what recurring relationship this setup bets on, and why
required conditions (each one measurable, with a threshold):
  C1 regime:     e.g. 1h ATR percentile < 60 over the last 60 sessions
  C2 session:    e.g. ny_am, and no scheduled tier-1 release within ±30 min
  C3 location:   e.g. trade through the prior-day low by ≤ 0.5 × ATR(14, 5m)
  C4 trigger:    e.g. a 5m close back inside within 3 bars
  C5 room:       e.g. ≥ 2R to the next opposing level
exclusions:      situations where the setup is explicitly off
record:          n, period, source (out-of-sample / forward / live),
                 win rate, avg win R, avg loss R, avg cost R, sd of R
valid for:       the regimes and sessions the record actually covers
history:         dated versions; what changed and on what evidence
```

**The gate:** list each required condition, the value measured today, and
match / no match. Write the matches in `evidence_for`, and everything that
argues against the trade (including near-misses and recent failures at the
same level) in `evidence_against`. Tag the regime (`regime_tag`) and session
(`session`).

**Rules:**

- If **any required condition is absent**, the setup's probability estimate
  does not apply to today. `evidence_score` = 0, and the candidate is a
  `skip`. A situation that matches no defined setup is not a trade. It may
  be a research note (Step-back path).
- If all conditions are present but one sits on its threshold, or
  `evidence_against` holds an unresolved item, `evidence_score` = 1 (Gate 4
  will make it a `wait`).
- Before moving on, answer the closing question of Section VI: *does
  today's market still resemble the environment in which this estimate was
  measured?* If the record covers only low-volatility sessions and today is
  not one, the answer is no.

---

## Gate 4 — The three-element test

**Enforces:** [[principle_01_understand_before_acting]],
[[principle_05_mathematical_justification]], [[principle_06_do_not_force]] ·
**Philosophy:** VIII ([[philo_source_of_opportunity]]), XV
([[philo_value_vs_price]]) · **Concepts:** [[concept_edge]],
[[concept_expectancy]], [[concept_probabilistic_thinking]]

Section VIII defines an opportunity as the agreement of three things: a
defensible explanation (understanding), present-day conditions that support
it (evidence), and a favourable assessment of outcomes against risks
(mathematics). The gate scores each from 0 to 2.

| Score | Understanding (`understanding_score`) | Evidence (`evidence_score`) | Mathematics (`math_score`) |
|---|---|---|---|
| **2** | Gates 1 and 2 are clean: the ladder is written, the hypothesis names level, destination, horizon and invalidation, and I can say why it should work and what would undermine it. | Every required condition of the setup card is present and measured today; nothing unresolved in `evidence_against`. | The setup's condition-matched record has n ≥ 30 out-of-sample, forward or live trades, and its expectancy after costs stays positive one standard error below the estimate (Gate 5.4). |
| **1** | An explanation exists but has a gap: the level is ambiguous, or I cannot say what would undermine it. | All required conditions present, but one is borderline, or an argument against is unresolved. | The point estimate after costs is positive, but n < 30 or the conservative estimate is ≤ 0. Worth testing, not trading. |
| **0** | No explanation beyond "it is moving", or the explanation cannot be proved wrong. | A required condition is absent, or no defined setup applies. | No record, expectancy ≤ 0 after costs, or the only numbers are in-sample or claimed by someone else (T4, [[framework_source_tiers]]). |

**Decision rule:**

- **2 / 2 / 2** → continue to Gate 5.
- **Any 0** → `skip`.
- **Otherwise** (a 1 somewhere, no 0) → `wait`. The contradiction is
  investigated, not overruled.

**Investigating a contradiction.** Section VIII lists the possibilities when
the explanation points one way and the numbers another: the understanding
is incomplete, the model does not apply to these conditions, or the pattern
is not statistically meaningful. Write which one you think it is in
`evidence_against`. If it resolves before the trigger window closes, write a
**new** journal row with a new `decided_at`; never edit the `wait` row. If it
does not resolve, the `wait` becomes a skip at the end of the window.

The one thing never allowed: settling the contradiction in favour of the
trade you want. In the owner's words, "An opportunity is not created by my
desire to trade."

**A gap between price and value is not evidence on its own.** Section XV
([[philo_value_vs_price]]) calls a perceived discrepancy between price and an
estimate of value "the beginning of an investigation, not proof of an
edge": the estimate may be wrong, the gap may persist, and the costs may
outweigh the benefit. So "price is far from value" can raise a candidate,
but it earns an `evidence_score` above 0 only through a setup card whose
conditions define that gap, and a `math_score` above 0 only if the card's
record shows the gap paying after costs (Gates 3 and 5; H19 in
`hypotheses.md` tests the claim).

---

## Gate 5 — Mathematics

**Enforces:** [[principle_05_mathematical_justification]],
[[principle_04_conditional_probability]] · **Philosophy:** VII
([[philo_mathematics_sword]]), VI ([[philo_conditional_probability]]) ·
**Concepts:** [[concept_expectancy]], [[concept_risk_reward_r_multiples]],
[[concept_probabilistic_thinking]], [[concept_performance_metrics]],
[[concept_overfitting_validation]], [[concept_backtesting]] · **Formulas:**
[[formula_sheet]] · **Open questions:** [[question_estimate_reliability]],
[[question_survives_costs]]

Gate 4 asked whether the *setup* has a measured edge. Gate 5 asks whether
*this trade*, at this entry, stop, target and cost, keeps it. Gate 5 can
lower `math_score` to 0; it can never raise it.

### 5.1 Expected value in R

Work in R, where **1R is the amount at risk between entry and stop**
(Van Tharp's convention, [[book_trade_your_way_financial_freedom]]). R makes
trades of different sizes and instruments comparable. Section VII's formula
becomes:

```
E[R] = p · W  −  (1 − p) · L  −  C

p  = est_win_prob     probability of a win, as a decimal (0–1)
W  = est_avg_win_r    average winning trade, in R, before costs
L  = est_avg_loss_r   average losing trade, in R, as a positive number
                      (≈ 1.0 if stops are respected; above 1.0 with slippage)
C  = est_cost_r       average round-trip cost (spread + commission +
                      slippage), in R
E[R] = est_ev_r
```

Break-even win rate after costs: `p_BE = (L + C) / (W + L)`.

### 5.2 The owner's $7 example, converted to R

Section VII's hypothetical strategy: 60% wins averaging $100, 40% losses
averaging $120, $5 cost per trade, expected value $7. Taking **1R = the $120
average loss**:

| Input | Dollars | In R (÷ $120) |
|---|---|---|
| p (win probability) | 0.60 | 0.60 |
| W (average win) | $100 | 0.833R |
| L (average loss) | $120 | 1.000R |
| C (cost per trade) | $5 | 0.042R |
| **E** = 0.60 × 0.833 − 0.40 × 1.000 − 0.042 | **$7.00** | **+0.058R** |

The same $7, read differently: if the trader *planned* to risk $100 and
losses averaged $120 because of slippage or moved stops, then 1R = $100,
W = 1.0R, L = 1.2R, C = 0.05R and E = +0.07R. The dollars are identical, but
an average loss above 1R is itself a finding: stops are slipping or being
moved, and the journal should show where.

Break-even after costs is p_BE = (1 + 0.042) / (0.833 + 1) = **56.8%**
(54.5% before costs). The estimated 60% clears it by about **3 percentage
points**. That margin is the whole edge, and the next section shows how
little evidence a small sample gives about it.

### 5.3 The uncertainty of the estimate

Section VI insists on asking how reliable an estimate is; Section XIX lists
it as an open question ([[question_estimate_reliability]]). Two standard
errors (from [[formula_sheet]]) answer it:

```
SE(p̂)     = √( p̂ (1 − p̂) / n )            uncertainty of the win rate
SE(E[R])  = sd(R) / √n                      uncertainty of the expectancy
t         ≈ √n · mean(R) / sd(R)            (Van Tharp's SQN is this statistic)
n needed  ≈ (z · sd(R) / E[R])²             trades needed for E to sit z SEs above 0
```

For the $7 example, sd(R) ≈ (W + L) · √(p(1 − p)) = 1.833 × 0.49 ≈ 0.90R.

| Trades (n) | SE of win rate | Win rate, ±2 SE | SE of E[R] | t |
|---|---|---|---|---|
| 30 | 8.9 pts | 42% – 78% | 0.164R | 0.36 |
| 100 | 4.9 pts | 50% – 70% | 0.090R | 0.65 |
| 300 | 2.8 pts | 54% – 66% | 0.052R | 1.12 |
| 1,000 | 1.5 pts | 57% – 63% | 0.028R | 2.05 |

After 100 trades, the honest statement about this strategy is "somewhere
between losing and winning". It needs about **240 trades** for its
expectancy to sit one standard error above zero, and about **950** for two.
A thin edge needs a large sample; this is Section VI's law of large numbers
turned into a number. By contrast, the knowledge base's trend-follower
illustration in [[concept_expectancy]] (35% wins, 3R average win, +0.40R)
has sd ≈ 1.9R and needs only about 90 trades for two standard errors.

### 5.4 Minimum sample and the conservative estimate

Defaults (the owner may tighten them in the trading plan):

1. **Only relevant records count.** Same setup version, conditions matching
   the card, and data **not used to design the rules**: out-of-sample
   backtest, forward (paper) test, or live. In-sample results do not count
   (Section XVII; [[concept_overfitting_validation]]).
2. **Floor: n ≥ 30.** Below it there is no estimate, only an anecdote
   (`math_score` ≤ 1). The master checklist uses the same floor.
3. **Conservative test: mean R − 1 × SE > 0 after costs** for
   `math_score` = 2. This rule scales itself: a large edge passes quickly,
   a thin edge needs hundreds of trades.
4. **Full risk needs mean R − 2 × SE > 0** (Gate 6.2). Between one and two
   standard errors the setup is traded at half risk.

### 5.5 Where the inputs come from

`est_win_prob`, `est_avg_win_r`, `est_avg_loss_r` and `est_cost_r` come from
the setup card's condition-matched record, updated at the monthly review.
They never come from memory, from how the chart "looks", or from a video's
headline claims (T4 in [[framework_source_tiers]]; see the sanity check in
[[concept_risk_reward_r_multiples]]).

### 5.6 Trade-level check

- **Target room:** the planned target in R is `(planned_target −
  planned_entry) / (planned_entry − planned_stop)` (sign reversed for
  shorts). If it is below the setup's average win, lower W to it.
- **Cost in R for this trade:** `cost in price units ÷ stop distance in
  price units`. A tight stop inflates cost in R: one point of friction is
  0.10R on a 10-point stop and 0.025R on a 40-point stop
  ([[concept_trade_execution]], [[concept_scalping]]).
- **Write `est_ev_r`.** It must be > 0 after costs (or above the plan's
  minimum, if the plan sets one). If it is not, `math_score` drops to 0 and
  the candidate is a `skip`.

---

## Gate 6 — Size

**Enforces:** [[principle_09_protect_capital]],
[[principle_10_emotional_independence]] · **Philosophy:** XIV
([[philo_capital_preservation]]) · **Concepts:** [[concept_position_sizing]],
[[concept_risk_of_ruin_drawdown]], [[concept_kelly_criterion_optimal_f]],
[[concept_correlation_portfolio_risk]], [[concept_leverage_margin]],
[[concept_prop_firm_risk_rules]]

Section XIV treats capital as the means of taking future opportunities, and
risk management as a direct consequence of accepting that individual
outcomes are uncertain. Gate 6 sizes the trade so that being wrong, several
times in a row, does not end the game.

### 6.1 Fixed-fractional risk

```
position_size = (equity × risk_pct / 100) / (stop_distance × point_value)
```

Round **down** to a whole unit. Then record the risk actually taken
(`risk_pct` after rounding). Risk is set by stop × size, never by the
leverage the broker allows ([[concept_leverage_margin]]).

### 6.2 Evidence-scaled risk

The plan sets one **base risk** (the knowledge base records 0.25–1% per
trade as the usual discretionary range in [[concept_position_sizing]]).
The evidence decides how much of it is used:

| Evidence (Gate 5.4) | Risk used |
|---|---|
| mean R − 2 SE > 0 | base risk |
| mean R − 1 SE > 0, but mean R − 2 SE ≤ 0 | half base risk |
| otherwise | no live trade (paper / forward test only) |
| Gate 0 state amber | half of the above, or step back |

Base risk changes only at the monthly review, and only on evidence. It is
never raised in-session.

### 6.3 Limits (circuit breakers)

The numbers below are **example defaults**. Write your own in the trading
plan ([[concept_trading_plan]]) before trading, not during a session.

| Limit | Example default | When hit |
|---|---|---|
| Risk per trade | base risk × evidence factor | n/a |
| Daily loss | 2–3R (range used in [[concept_risk_of_ruin_drawdown]]) | Session over. Journal, no more trades. |
| Weekly loss | 5R | Week over. Review before the next week. |
| Consecutive losses, same setup, same session | 3 | That setup is off for the session. |
| Drawdown from peak equity | −10% → halve base risk; −20% → stop live trading, return to paper and review | Restore only through the monthly review. |
| Open risk ("heat") | ≤ 2% of equity in total; correlated positions count as one idea | No new position until heat falls. |

Practitioner echo (T2): JJ Simon's playbook
([[strategy_jj_simon_fair_pricing]]) stops reversion trades for the session
after three consecutive failures, on the reasoning that the market may be
trending and establishing a new fair value. That is a regime switch written
as a loss limit.

### 6.4 The recovery asymmetry

The owner's example in Section XIV: a $1,000 account that loses 50% must
then make **100%** on the remaining $500 to get back. In general:

```
gain needed to recover = 1 / (1 − drawdown) − 1
damage from k losses in a row at risk f = 1 − (1 − f)^k
```

| Drawdown | Gain needed to recover |
|---|---|
| 10% | 11.1% |
| 20% | 25.0% |
| 30% | 42.9% |
| 50% | 100% |
| 75% | 300% |

| Risk per trade | After 10 losses in a row | After 20 losses in a row | Gain needed to recover from 20 |
|---|---|---|---|
| 0.25% | −2.5% | −4.9% | +5.1% |
| 0.5% | −4.9% | −9.5% | +10.5% |
| 1% | −9.6% | −18.2% | +22.3% |
| 2% | −18.3% | −33.2% | +49.8% |

Long losing runs are normal even for sound strategies (Gate 8.3). Size so
that the worst run you should expect is uncomfortable but survivable.
(Marci Silfrain's advice to plan for the next 20 trades to be losers is
recorded in her playbook note as coming from a podcast recap, T3:
[[strategy_marci_silfrain_measured_move]].)

### 6.5 Kelly: an upper bound, never a target

The Kelly fraction ([[paper_kelly_1956]], [[concept_kelly_criterion_optimal_f]])
is the bet size that maximises long-run growth *when p and the payoff are
known exactly*. In trading they are estimates, so Kelly is used only as a
ceiling.

```
b  = (W − C) / (L + C)        net payoff ratio
f* = p − (1 − p) / b          Kelly fraction of equity at risk
```

For the $7 example: b = (0.833 − 0.042) / (1 + 0.042) = 0.76, so
f* = 0.60 − 0.40 / 0.76 ≈ **7.4%** of equity per trade. Now move p down by
one standard error of a 50-trade sample (to 53%): f* = **−8.7%**, which says
do not bet at all. One standard error of estimation noise turns "risk 7%"
into "risk nothing". That is why the rule is:

```
risk_pct ≤ min( base risk × evidence factor ,  ¼ × Kelly computed from the conservative p )
```

The knowledge base's sizing notes give ¼ to ½ Kelly as the practical range
and warn that betting above twice Kelly destroys growth even with an edge.
In practice the fixed-fractional base risk is almost always the binding
limit; Kelly's job here is to catch the case where a thin or uncertain edge
cannot support even that.

**Gate 6 output:** final `decision` (`take` only if Gates 0–6 all pass),
`planned_entry`, `risk_pct`, `position_size`. Save the journal row now. The
order is placed after the row exists.

---

## Gate 7 — Execute per plan; when the evidence changes

**Enforces:** [[principle_07_respond_methodically]],
[[principle_02_context_before_movement]], [[principle_12_process_not_money]],
[[principle_09_protect_capital]] · **Philosophy:** X
([[philo_evidence_changes]]), XIII ([[philo_decisions_not_money]]) ·
**Concepts:** [[concept_trade_execution]], [[concept_trade_management]],
[[concept_volatility]], [[concept_news_trading]]

Section XIII: when the conditions justify a trade, execute the plan rather
than letting fear or excitement decide. Section X: when the evidence
changes, manage the risk first and investigate second.

### 7.1 Before and at entry

- The journal row (pre-trade fields) is saved and timestamped.
- Enter only when the trigger defined on the setup card has **completed**
  (a closed candle, not a forming one; master checklist item 6).
- The hard stop goes in with the entry order. A mental stop is not a stop.

### 7.2 In-trade rules

| Allowed | Not allowed |
|---|---|
| Exit at the stop, the target, the invalidation condition or the time stop | Widening the stop |
| Reduce risk by a management rule written in the plan **before** the trade (breakeven or partial rule) | Adding to a losing position |
| Exit early when the procedure below says the reason for the trade is gone | Moving B further away without a pre-written trailing rule |
| Do nothing while price moves inside the measured C-band | Re-entering right after a stop-out without a new row through all gates |

### 7.3 The "evidence changed" procedure

**Step 1: manage risk first.** Work down the list and stop at the first yes.

1. **Is the written invalidation condition met?** → Exit. No debate
   (`exit_reason` = `invalidation` or `stop`).
2. **Is the reason for the trade gone even though the stop is not hit** (a
   Gate 3 condition no longer holds: regime flip, unscheduled news, the
   level accepted against you)? → The estimate behind the trade no longer
   applies (Section VI). Exit, or reduce to the plan's minimum if the plan
   says so (`exit_reason` = `evidence_changed`).
3. **Is the move inside the measured C-band, with the reason intact?** →
   Hold. Do nothing. Note it.
4. **Unsure which of these applies?** → The stop already caps the loss. You
   may reduce or exit; you may never widen or add.

Section X is explicit that neither reflex is acceptable: assuming the market
is "simply taking a detour", and dropping every hypothesis the moment price
moves against you.

**Step 2: investigate**, once the position is flat or its risk is reduced.
Answer the owner's questions from Section X, in the `lesson` field:

1. Why did the conditions change?
2. Was the move consistent with normal variation in similar situations
   (compare with the setup's MAE record)?
3. Did a new factor enter the market?
4. Has the market moved into a different environment (regime)?
5. Was my original interpretation wrong?
6. Did the strategy behave within its expected range of outcomes, or did
   something happen that challenges its assumptions?

Measure the size and speed of the change and compare it with historical
examples rather than answering from instinct.

**Step 3: accept uncertainty.** "Unexplained" is a legitimate answer.
Section X says to acknowledge uncertainty rather than invent a satisfying
explanation.

**Step 4: record.** `exit_reason`, `mae_r`, `mfe_r`,
`emotional_state_during`, and whether the plan was followed
(`executed_per_plan`).

---

## Gate 8 — Post-trade review

**Enforces:** [[principle_08_decision_quality_not_outcome]],
[[principle_11_record_and_investigate]] · **Philosophy:** XI
([[philo_being_wrong]]), XVI ([[philo_journal]]), XVII
([[philo_scientific_method]]) · **Concepts:**
[[concept_trading_journal_review]], [[concept_probabilistic_thinking]],
[[concept_performance_metrics]], [[concept_overfitting_validation]]

Section XI: a loss does not prove the decision was wrong, and a win does not
prove it was right. The review grades the two separately, on the same day
for intraday trades. Skips and waits are reviewed too.

### 8.1 Fill the post-trade fields

`executed_per_plan`, `exit_reason`, `result_r` (net of costs), `cost_r`,
`mae_r`, `mfe_r`, `emotional_state_during`, `outcome_within_expected`,
`lesson`, `hypothesis_update`, `reviewed_at`. Definitions are in the journal
template ([[framework_trading_journal]]).

### 8.2 Decision quality versus outcome

**The decision was good** if all of these are true: the pre-trade fields
were complete before entry; each gate's answer was honest (the scores can be
defended from the written fields); size followed Gate 6; the trade was
executed and exited according to the plan.

| | Outcome favourable | Outcome unfavourable |
|---|---|---|
| **Good decision** | *Earned.* Repeat the process. Do not let it raise confidence beyond the evidence. | *Variance.* Accept it. Check that it sits inside the expected range. No rule change. |
| **Poor decision** | *Lucky.* Treat it as a mistake. It is the most dangerous cell, because it rewards breaking the process (Section XII's "excitement"). | *Earned loss.* Find the gate that was skipped or bent, and fix the process. |

Annie Duke's name for judging a decision by its result is "resulting"
([[book_thinking_in_bets]], [[concept_probabilistic_thinking]]). This table
is the antidote.

### 8.3 Is a losing run within expected variation?

Section XI asks for a way to tell whether a run of losses fits the
strategy's expected behaviour or shows that its assumptions no longer hold.
A rule of thumb for the longest losing run to expect in N trades with win
rate p (q = 1 − p):

```
expected longest losing run ≈ ln(N · p) / ln(1 / q)
```

| Win rate | 100 trades | 500 trades |
|---|---|---|
| 60% | ≈ 4.5 | ≈ 6.2 |
| 48% | ≈ 5.9 | ≈ 8.4 |
| 40% | ≈ 7.2 | ≈ 10.4 |

A run inside this range is not, by itself, evidence against the setup. A run
well beyond it, or a drawdown beyond what a Monte Carlo reshuffle of the
setup's R-record produces in, say, 95% of paths
([[concept_risk_of_ruin_drawdown]], [[concept_backtesting]]), is evidence.
It triggers a review of the setup and a drop to half risk, not an emotional
rewrite of the rules.

### 8.4 What one trade is allowed to change

Almost nothing. Section XII separates changing a method through disciplined
investigation from changing it under emotional pressure. A single trade may
produce an `observe` or a `propose` entry in `hypothesis_update`. Only the
monthly review, with an adequate sample, may `revise` a setup card (see the
journal template's feedback loop). The one exception is risk *reduction*: a
limit can be tightened at once. A limit is never loosened mid-week.

---

## The Step-back path

**Enforces:** [[principle_06_do_not_force]],
[[principle_01_understand_before_acting]],
[[principle_10_emotional_independence]] · **Philosophy:** IX
([[philo_step_back]]), XIII ([[philo_decisions_not_money]]) · **Concepts:**
[[concept_trading_psychology]], [[concept_market_regimes]],
[[concept_trading_plan]]

The owner's line is that "not trading is a decision, not a failure to make
one." The protocol treats it that way: a step back is a journal row with
`decision` = `skip` or `wait`, its own reasoning, and its own review.

- **`skip`**: the candidate failed a gate. It is closed. If the situation
  later changes, that is a new candidate and a new row.
- **`wait`**: the candidate is coherent but something is unresolved (a score
  of 1). Investigate within the trigger window, then write a new row, or let
  it lapse into a skip.

### When to stand aside

| Trigger | Source |
|---|---|
| Gate 0 is red, or amber and you chose not to trade | XII |
| You cannot write the observation → hypothesis ladder in plain words | IV, IX |
| The level of the hypothesis or its invalidation cannot be stated | III |
| `regime_tag` is `unclear`, or no defined setup's conditions match | VI |
| Any three-element score is 0 | VIII |
| Expected value after costs ≤ 0, or the sample is too small | VII |
| A loss limit or the consecutive-loss stop is hit | XIV |
| The evidence changed and the investigation is unresolved: stand aside in that instrument for the session | X |
| Unscheduled news or a structural break: the old estimates no longer apply | VI |
| **Over-watching:** you have watched for a long stretch, have no valid setup, and notice yourself narrating every tick or "pre-loading" an entry | IX |

On over-watching, Section IX is specific: constant observation invites
explanations for movements that have no demonstrated predictive value, and
the time spent watching starts to feel like a reason to act. The response is
mechanical: close the chart for a fixed period (the plan sets it), then
re-run Gate 0.

### What to do while standing aside

Section IX describes an investigation mode, not idleness:

1. Look at the moves that preceded the current behaviour and at the wider
   environment.
2. Compare the situation with similar historical examples.
3. Ask whether a recognisable, **testable** relationship exists. If it
   might, write it as a draft setup card and test it on data (paper or
   backtest journal), not with money.

### Returning

Return when Gate 0 is green and a defined setup's conditions are present.
A move you missed is not a reason to return: Section XIII says a missed
opportunity does not justify abandoning discipline. A missed move is never
chased.

---

## Where this sits in the knowledge base

| Protocol | Unified framework stage ([[synthesis_unified_framework]]) | Master checklist item ([[synthesis_pre_trade_checklist]]) |
|---|---|---|
| Gate 0 | L7 Will I follow it? | 10 State of mind |
| Gate 1 | L1 Mechanics, L3 Lens | (not in the checklist: the ladder is the philosophy's addition) |
| Gate 2 | L2 Context | 4 HTF bias, 7 Invalidation |
| Gate 3 | L2 Context, L4 Setup | 2 Regime, 3 Session, 5 Location, 6 Trigger |
| Gate 4 | L0 Edge, L4 Setup | (the agreement rule is the philosophy's addition) |
| Gate 5 | L0 Edge, L6 How much | 1 Edge, 8 Target & R:R |
| Gate 6 | L6 How much | 9 Size |
| Gate 7 | L5 When and how | 6 Trigger, 7 Invalidation |
| Gate 8 | L8 Is it still working? | Post-trade log |

Two additions come from the philosophy rather than from the existing
checklist: the separate rungs of Gate 1 (Section IV) and the requirement
that understanding, evidence and mathematics *agree* (Section VIII). The
`skip` and `wait` decisions also become records rather than absences.

---

## Worked example (hypothetical)

> **Everything in this section is hypothetical.** The instrument, prices,
> setup record and outcome are invented to show the mechanics. They are not
> a backtest, a recommendation, or a claim about any real strategy. The same
> trade is the `take` example row in `journal-template.csv`.

**Account and plan.** Equity $50,000. Base risk 0.5% per trade. Daily loss
limit 3R; weekly 5R; three consecutive losses per setup per session.
Instrument: a hypothetical index micro future ("HYPO-IDX-micro"), $2 per
point, estimated round-trip cost $2 per contract.

**Setup card `EXAMPLE-sweep-reversal-v1` (hypothetical).** Claim under test:
when price runs the stops below an obvious prior-day low during an intact
uptrend and fails to gain acceptance below it, it may rotate back toward the
session's value ([[concept_liquidity_sweep_reversal]], [[concept_liquidity]]).
Conditions C1–C5 as in the Gate 3 template. Record: n = 120 condition-matched
trades (80 out-of-sample backtest, 40 forward paper), win rate 0.48, average
win 1.90R, average loss 1.05R, average cost 0.06R.

**Gate 0.** One −1R loss yesterday, slept normally, no carryover noticed.
Daily loss used: 0R; week: −1R of −5R. State: `calm`. Proceed.

**Gate 1.**
- *Observation:* at 09:36 ET price traded 6 points below the prior-day low
  (18,239) to 18,233, then closed back above it on the second 5-minute bar.
  5-minute volume on the drop was 1.8× its 20-bar average.
- *Interpretation:* sell stops below the prior-day low may have been
  triggered and met by buyers. Alternative: a breakdown that has not yet
  extended.
- *Hypothesis:* on the 1-hour uptrend, the sweep is a C-leg within
  structure; price may rotate to the session VWAP at 18,286 before 11:00 ET.

**Gate 2.** Level: 1-hour structure, 5-minute trigger (`1h/5m`). B = 18,286
by 11:00 ET. Normal C-band: the record's winners show adverse excursion up
to 0.8R at the 80th percentile. Structural change: a 5-minute close below
the sweep low. Invalidation: 5-minute close below 18,233 (hard stop 18,232),
or no VWAP by 11:00 ET (time stop).

**Gate 3.** C1 regime: 1-hour ATR percentile 38 (< 60) ✓. C2 session:
`ny_am`, the 08:30 release is more than 30 minutes past ✓. C3 sweep depth:
6 points against ATR(14, 5m) of 15 = 0.4 ATR (≤ 0.5) ✓. C4 reclaim on bar 2
(≤ 3) ✓. C5 room: 36 points to VWAP against an 18-point stop = 2.0R (≥ 2R)
✓, but exactly at the threshold, so it goes in `evidence_against` along with
"the prior-day low was tested twice last week". Regime tag `trend_low_vol`.

**Gate 4.** Understanding 2, evidence 2 (the borderline room is at, not
below, the threshold and is noted), mathematics 2 (n = 120 ≥ 30; see Gate 5).

**Gate 5.**
- E[R] = 0.48 × 1.90 − 0.52 × 1.05 − 0.06 = **+0.31R** (`est_ev_r`).
- Break-even after costs: (1.05 + 0.06) / (1.90 + 1.05) = 37.6%. The 48%
  estimate clears it by about 10 points; even the conservative win rate
  (48% − 4.6 points = 43.4%) clears it.
- sd(R) ≈ 2.95 × √(0.48 × 0.52) ≈ 1.47R; SE = 1.47 / √120 ≈ 0.13R.
  mean − 1 SE = +0.17R; mean − 2 SE = +0.04R; t ≈ 2.3.
- This trade: target 2.0R ≥ the 1.90R average win, so W stays 1.90.
  Cost: 6 contracts × $2 = $12 against 1R = $216, i.e. 0.056R, in line with
  the 0.06R estimate.

**Gate 6.**
- Evidence factor: mean − 2 SE > 0, so full base risk (0.5%).
- Size = ($50,000 × 0.005) / (18 points × $2) = $250 / $36 = 6.94 → **6
  contracts**. Actual risk 6 × 18 × $2 = $216 = **0.43%** (`risk_pct`).
- Kelly ceiling: b = (1.90 − 0.06) / (1.05 + 0.06) = 1.66; f* = 0.48 −
  0.52 / 1.66 = 16.6%; from the conservative 43.4%, f* = 9.3%, and a
  quarter of that is 2.3%. Not binding: 0.43% is far below it.
- Heat: no other open positions. Decision: **take**. Row saved 09:47 ET.

**Gate 7.** Entry 18,250. Price first dips to 18,238 (0.67R adverse, inside
the 0.8R C-band): step 3, hold. It then rallies to 18,271.5 (+1.19R) by
10:24. At 10:31 an unscheduled headline hits; price falls 40 points in two
minutes (about 2.7 × the 5-minute ATR, outside the setup's recorded range).
The hard stop at 18,232 fills at 18,230. Result: 20 points × 6 × $2 = $240
plus $12 costs = $252 = **−1.17R** net. MAE 1.11R, MFE 1.19R.

Investigation, after flat: (1) the conditions changed because of the
headline; (2) the speed was outside normal variation for this setup; (3) a
new factor entered; (4) the environment changed: the 1-hour ATR percentile
reached 85 for the rest of the session, so C1 no longer held and the setup
was off for the day; (5) whether the reading of the sweep was wrong cannot
be told, because the headline swamped the auction, so this is recorded as
unexplained by the setup; (6) the loss of 1.17R sits inside the plan's
slippage allowance of 1.25R, so the outcome was within the expected range.

**Gate 8.** Good decision (all gates passed honestly, executed and exited per
plan), unfavourable outcome: the *variance* cell. `executed_per_plan` = y,
`exit_reason` = stop, `outcome_within_expected` = y. Lesson: the process
held, the loss came from an unscheduled headline, slippage was 0.11R and
within the allowance. Gate 0's after-loss pause was taken. Hypothesis
update: `observe` — tag trades hit by unscheduled headlines (`news_shock`)
so the monthly review can measure their effect; no rule change from one
trade.

A second hypothetical row in the CSV shows the Step-back path: a breakout
candidate two days later that is skipped because a required condition
(compression) is absent and its record is only 18 paper trades.

---

## One-page checklist

*Print this. Every box is a written answer, not a feeling. Any unticked box
→ STEP BACK (`skip` or `wait`, written in the journal).*

**Gate 0 · State** ([[principle_10_emotional_independence]])
- [ ] Not trying to recover a loss or hit a money target; not trading from boredom
- [ ] No carryover; rested; free of distraction · state tag written
- [ ] Daily / weekly loss limits and consecutive-loss stop not hit
- [ ] After a loss: pause taken, size unchanged · After a win: "would I have taken this before?"

**Gate 1 · Ladder** ([[principle_01_understand_before_acting]])
- [ ] Observation: measured, verifiable, no motives
- [ ] Interpretation: "may", plus at least one alternative
- [ ] Hypothesis: level, destination B, horizon; can be proved wrong

**Gate 2 · Context & level** ([[principle_02_context_before_movement]], [[principle_03_future_is_uncertain]])
- [ ] Hypothesis timeframe / trigger timeframe named
- [ ] C-band (normal adverse move) defined in measured units
- [ ] Structural-change signals written
- [ ] Invalidation written before entry: price (close) + condition + time
- [ ] Stop sits where the hypothesis is wrong, not where it hurts

**Gate 3 · Conditions** ([[principle_04_conditional_probability]])
- [ ] A versioned setup card applies
- [ ] Every required condition measured today and matched
- [ ] Evidence against written; today resembles the record's environment

**Gate 4 · Three elements** ([[principle_06_do_not_force]])
- [ ] Understanding 2 · Evidence 2 · Mathematics 2 (any 0 = skip; any 1 = wait)

**Gate 5 · Mathematics** ([[principle_05_mathematical_justification]])
- [ ] E[R] = p·W − (1−p)·L − C > 0 after costs, from condition-matched out-of-sample records
- [ ] n ≥ 30 and mean R − 1 SE > 0
- [ ] This trade's target room and cost in R checked

**Gate 6 · Size** ([[principle_09_protect_capital]])
- [ ] size = equity × risk% / (stop × point value), rounded down
- [ ] Risk = base × evidence factor (× ½ if amber); ≤ ¼ Kelly from conservative p
- [ ] Heat and correlation within limits
- [ ] Journal row saved and timestamped **before** the order

**Gate 7 · Execute** ([[principle_07_respond_methodically]])
- [ ] Trigger completed; hard stop placed with entry
- [ ] Never widen, never add to a loser, never move B
- [ ] Evidence changed → risk first (invalidated? reason gone? inside C-band?) → then investigate the six questions → "unexplained" is allowed

**Gate 8 · Review** ([[principle_08_decision_quality_not_outcome]], [[principle_11_record_and_investigate]])
- [ ] Post-trade fields filled the same day; pre-trade fields untouched
- [ ] Decision graded separately from outcome (earned / variance / lucky / earned loss)
- [ ] Losing run compared with expected variation
- [ ] One trade → observe or propose only; revisions wait for the monthly review

**Step back** ([[principle_06_do_not_force]]) — not trading is a decision: write the row.
