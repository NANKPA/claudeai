---
id: framework_trading_journal
type: framework
title: "Trading Journal — a record of understanding"
partition: 00_philosophy
layer: L8
related: [philosophy_relationship, philo_journal, principle_11_record_and_investigate, framework_decision_protocol, concept_trading_journal_review]
uses: [concept_expectancy, concept_risk_reward_r_multiples, concept_performance_metrics, concept_overfitting_validation, concept_market_regimes, concept_trading_psychology]
status: synthesized
---

# Trading Journal — a record of understanding

> **Education, not financial advice.** The two example rows in
> `journal-template.csv` are hypothetical. Their prices, estimates and
> results are invented to show how the fields are filled.

Section XVI of the philosophy ([[philo_journal]]) asks for a journal that
records the *development and testing of understanding*, not just entries,
exits and profits. This template puts that into practice. It is the record
side of the Decision Protocol ([[framework_decision_protocol]]): each gate of
the protocol writes into named columns here, and the reviews read them back.

**Files**

| File | What it is |
|---|---|
| `journal-template.md` | This guide: why each field exists, the rules, the review routine |
| `journal-template.csv` | The header row (39 columns, fixed order) and two `EXAMPLE-` rows |
| `decision-protocol.md` | The gates that fill the pre-trade columns |
| `tools/philosophy/journal_review.py` | The weekly and monthly review script (reads these exact columns) |

**One row is one decision, not one trade.** Takes, skips and waits all get a
row. Section IX ([[philo_step_back]]) says that not trading is a decision; a
journal that records only trades hides half of the decisions and all of the
discipline.

---

## Why the journal exists

Section XVI gives the journal five jobs. Each column below serves at least
one of them.

1. **Record the reasoning at the time of the decision:** the conditions,
   the reasoning, the probability estimate, and what would invalidate the
   hypothesis.
2. **Examine what happened afterwards:** did the market stay inside the
   expected range, did the hypothesis hold, was the plan followed, did
   emotion interfere, was the result informative or just one draw from an
   uncertain process?
3. **Expose contradictions.** The owner's own example: describing a setup as
   high probability without the evidence to back it. Another: a strategy
   that works in some conditions and fails in others.
4. **Replace memory with a record.** Section VII warns that memory keeps the
   winners and drops the failures.
5. **Discover, not vindicate.** In the owner's words, "The purpose is not to
   prove that I was right."

---

## The two rules that keep it honest

### Rule 1: pre-trade fields are written before entry and never edited

Section XVI is plain that a journal does not remove hindsight bias by
itself; the reasoning has to be recorded before or at the decision, not
rebuilt afterwards so that it looks more logical. So:

- Columns 1–28 (`trade_id` to `emotional_state_pre`) are the **pre-trade
  fields**. They are complete, and the row is saved, *before* the order is
  sent. `decided_at` is that moment.
- After `decided_at`, the pre-trade fields are **frozen**. Never edit them,
  not even to fix an obvious mistake. Write corrections in `lesson` as
  `correction: ...`.
- Make the freeze checkable. Keep the file append-only and save a
  timestamped copy, or commit it to a private git repository, right after
  each decision. Then any later edit shows up as a difference.
- If a position was opened before the pre-trade fields were written, the
  row is still filled in, but `executed_per_plan` = `n` whatever the result.
  An unrecorded decision is a process breach.
- A `wait` that later becomes a `take` gets a **new row** with a new
  `decided_at`. The `wait` row stays as it was.
- The same goes for an impulse entry. If you open a position after
  recording `skip` or `wait`, that is a new decision. Write a new row with
  `decision` = `take`, the scores as you would honestly give them at that
  moment, and `executed_per_plan` = `n`. The review then counts it as a
  trade taken outside the process, which is what it was. The original row
  stays untouched.

### Rule 2: every decision gets a row, and records never mix

- Live decisions go in the live journal. Forward (paper) tests and backtests
  go in **separate files with the same 39 columns**. Mixing them would blend
  real execution with hypothetical execution, which is the separation
  Section XVII ([[philo_scientific_method]]) asks for. In backtest files the
  emotional columns are `na`.
- Copy the template, then delete the two `EXAMPLE-` rows from the working
  file. The `EXAMPLE-` prefix in `setup_id` marks them so that they can
  also be filtered out.

---

## Format conventions

- **CSV:** UTF-8, comma-separated, the header row exactly as in the
  template. A field that contains a comma, a quote or a line break is
  wrapped in double quotes (spreadsheets do this on export). Inside a
  field, separate list items with `;`.
- **Timestamps:** ISO 8601 with the UTC offset, for example
  `2026-10-05T09:47:00-04:00`.
- **R values** are decimals. **1R** is the amount at risk between the
  planned entry and the planned stop (Van Tharp's convention,
  [[concept_risk_reward_r_multiples]]).
  - `est_avg_loss_r`, `est_cost_r`, `cost_r`, `mae_r` and `mfe_r` are
    **positive magnitudes**.
  - `result_r` and `est_ev_r` are **signed** (a loss is negative).
  - `result_r` is **net of all costs**. Its gross value is
    `result_r + cost_r`.
- **Probabilities** are decimals from 0 to 1 (`0.48`, not `48%`).
- **`risk_pct`** is in percent units: `0.5` means 0.5% of equity.
- **Scores** are integers 0, 1 or 2.
- **Categorical values** are lowercase and exact: `decision` = `take` |
  `skip` | `wait`; `executed_per_plan` = `y` | `n` | `na`;
  `outcome_within_expected` = `y` | `n` | `na`.
- **Not applicable:** leave numeric fields empty; write `na` in categorical
  fields.
- **Expected value:** `est_ev_r = est_win_prob × est_avg_win_r − (1 −
  est_win_prob) × est_avg_loss_r − est_cost_r`, rounded to two decimals.
  This is Section VII's formula in R ([[concept_expectancy]]).

---

## Field reference (39 columns, in this order)

Phase **pre** = written before entry and frozen at `decided_at`.
Phase **post** = written at review.

| # | Column | Phase | Format / allowed values | What to write | Why it exists |
|---|---|---|---|---|---|
| 1 | `trade_id` | pre | text, unique | One id per decision, e.g. `2026-10-05-01`. Skips and waits get ids too. Name screenshots after it. | XVI: a record that can be examined and cross-referenced instead of remembered. |
| 2 | `decided_at` | pre | ISO 8601 + offset | The moment the pre-trade fields were complete, before any order. | XVI: proves the reasoning came before the result (hindsight bias). |
| 3 | `instrument` | pre | text | Symbol and contract. | I, II: each market has its own participants and mechanics; estimates do not transfer automatically. |
| 4 | `timeframe` | pre | `hypothesis_tf/trigger_tf`, e.g. `1h/5m` | The level the hypothesis is about, then the trigger chart. | III: a move means different things at different levels. Protocol Gate 2. |
| 5 | `setup_id` | pre | versioned id from the setup card, e.g. `sweep-reversal-v1`; `EXAMPLE-` reserved | The defined setup whose conditions and record apply. | VI: a probability exists only for a defined situation. XVII: versions keep development apart from evaluation. Gate 3. |
| 6 | `regime_tag` | pre | vocabulary below | The market state, measured. | VI: the same pattern has different odds in trending and ranging markets. V: context changes a pattern's meaning. |
| 7 | `session` | pre | vocabulary below | When the decision was made. | VI: conditions include time of day ([[concept_trading_sessions_killzones]]). |
| 8 | `observation` | pre | text | What is on the chart, in numbers. No motives. | IV: separate what is observed from what is inferred. Gate 1. |
| 9 | `interpretation` | pre | text | What it *may* mean, plus at least one alternative. | IV: price shows the terms of trade, not the reasons. Gate 1. |
| 10 | `hypothesis` | pre | text | A claim that can be wrong: level, destination B, horizon. | III, IV; [[principle_03_future_is_uncertain]]: B is a hypothesis, not a promise. Gate 1. |
| 11 | `invalidation` | pre | text: price + condition + time | What would prove the hypothesis wrong, written before entry. | XVI asks for exactly this. III: separates the C-leg from structural change. Gate 2. |
| 12 | `evidence_for` | pre | `;`-separated list | Each matched condition, with the value measured today. | VIII: evidence is one of the three elements. Gate 3. |
| 13 | `evidence_against` | pre | `;`-separated list | Unmatched or borderline conditions, recent failures, the contradiction being investigated. | II: my model may be incomplete. VIII: contradictions are investigated, not overruled. XVI: exposes contradictions. |
| 14 | `understanding_score` | pre | 0 / 1 / 2 | Rubric in Gate 4 of the protocol. | VIII: a defensible, testable explanation. |
| 15 | `evidence_score` | pre | 0 / 1 / 2 | Rubric in Gate 4. | VIII: today's market shows the conditions. |
| 16 | `math_score` | pre | 0 / 1 / 2 | Rubric in Gate 4; Gate 5 may lower it to 0. | VIII, VII: a favourable assessment of outcomes against risks. |
| 17 | `est_win_prob` | pre | decimal 0–1 | From the setup card's condition-matched record, never from feel. | VI; XVI: "the probability estimate I am using". Lets the review test calibration. |
| 18 | `est_avg_win_r` | pre | decimal ≥ 0 | Average win in R from the record, capped at this trade's target room. | VII: the size of wins matters as much as their frequency. |
| 19 | `est_avg_loss_r` | pre | decimal ≥ 0 | Average loss in R from the record (≈ 1.0, more with slippage). | VII: a strategy can win often and still lose money. |
| 20 | `est_cost_r` | pre | decimal ≥ 0 | Expected round-trip cost (spread + commission + slippage) ÷ 1R. | VII: costs belong in the formula. XIX: [[question_survives_costs]]. |
| 21 | `est_ev_r` | pre | signed decimal | The formula above. | VII: expected value is the test. Gate 5. |
| 22 | `decision` | pre | `take` / `skip` / `wait` | `take` only if all three scores are 2 and `est_ev_r` > 0. | IX: not trading is a decision. VIII: no agreement, no trade. |
| 23 | `planned_entry` | pre | price | Planned entry (also recorded for skips, so they can be studied). | XIII: execute the plan rather than the mood. |
| 24 | `planned_stop` | pre | price | Where the hypothesis is wrong. Defines 1R. | III, XIV: being wrong must be survivable. |
| 25 | `planned_target` | pre | price | Destination B. | III: B written down cannot quietly move. |
| 26 | `risk_pct` | pre | percent units, e.g. `0.43`; empty if no position | Risk actually taken after rounding the size down. | XIV: capital preservation. Gate 6. |
| 27 | `position_size` | pre | units / contracts / lots; empty if no position | `equity × risk% / (stop distance × point value)`, rounded down. | XIV; [[concept_position_sizing]]. |
| 28 | `emotional_state_pre` | pre | tags (vocabulary below), `;`-separated | The Gate 0 state. | XII: fear, greed, frustration and excitement override methods. Gate 0. |
| 29 | `executed_per_plan` | post | `y` / `n` / `na` | `y`: the position was entered, managed and exited by the plan. `n`: any deviation (late or early entry, moved stop, discretionary exit, entry before the row was written, an impulse entry recorded as a new `take` row). `na`: no position, as decided (`skip`, `wait`). | XVI: "Was the trade executed according to the plan?" XIX: [[question_consistent_execution]]. |
| 30 | `exit_reason` | post | vocabulary below | Why the position closed. | X: invalidation, changed evidence and normal variation are different events. Gate 7. |
| 31 | `result_r` | post | signed decimal, net of costs; empty on a `take` with no fill | On a `take`: the realised result in R. On a `skip` or `wait`: optional counterfactual (see the feedback loop); usually left empty. | XI: the outcome is recorded, then judged separately from the decision. |
| 32 | `cost_r` | post | decimal ≥ 0; empty if no position | Realised costs in R (already included in `result_r`). | XIX: does the edge survive costs? Compared with `est_cost_r`. |
| 33 | `mae_r` | post | decimal ≥ 0; empty if no position | Maximum adverse excursion from entry, in R. | III, X: measures the normal C-band, so "normal variation" becomes a number. |
| 34 | `mfe_r` | post | decimal ≥ 0; empty if no position | Maximum favourable excursion from entry, in R. | X, VII: whether targets are realistic and how much was given back. |
| 35 | `emotional_state_during` | post | tags, `;`-separated; `na` if no position | The state during the trade. | XVI: "Did emotions influence the decision?" |
| 36 | `outcome_within_expected` | post | `y` / `n` / `na` | `y` if the result and path (MAE, MFE, loss size, time) fell inside the range the setup's record and plan anticipated. `n` triggers the Section X investigation. `na` without a position. | XVI: "Did the market behave within the range of outcomes I expected?" XI: variance versus a broken assumption. |
| 37 | `lesson` | post | text | What the decision taught about the *process*, the answers to the Section X questions when evidence changed, and any `correction:`. | X, XVI: record findings; say "unexplained" when that is the truth. |
| 38 | `hypothesis_update` | post | `none` or `observe:` / `propose:` / `revise:` / `retire:` + text | What this row implies for the setup card (see the feedback loop below). | XII: change through investigation, not pressure. XVII: tested change. |
| 39 | `reviewed_at` | post | ISO 8601 + offset | When the post-trade fields were completed. | XVI: closes the record. Must be later than `decided_at`. |

### Recommended vocabularies

| Column | Values |
|---|---|
| `regime_tag` | `trend_low_vol`, `trend_high_vol`, `range_low_vol`, `range_high_vol` (the 2×2 of [[concept_market_regimes]]), `event` (a release or headline dominates), `unclear` (→ step back) |
| `session` | `asia`, `london`, `ny_am`, `ny_pm`, `overnight`, `daily` (decisions made on the daily close) |
| `emotional_state_pre`, `emotional_state_during` | green: `calm`, `focused` · amber: `tired`, `distracted`, `anxious`, `carryover` · red: `frustrated`, `overconfident`, `fomo`, `revenge` |
| `exit_reason` | `target`, `stop`, `invalidation` (a condition-based exit before the stop), `time_stop`, `evidence_changed` (Gate 7 step 2), `management` (a pre-written breakeven, partial or trailing rule), `discretionary` (outside the plan, so `executed_per_plan` = `n`), `na` (no position) |
| `hypothesis_update` | `none`, `observe: ...`, `propose: ...`, `revise: ...`, `retire: ...` |

Extend a vocabulary when needed, but never rename a value once it is in
use, or the reviews can no longer group the rows.

### Checks every row should pass

1. `est_ev_r` matches the formula to within 0.01.
2. `decision` = `take` only if all three scores are 2 and `est_ev_r` > 0.
3. Any score of 0 means `decision` = `skip`.
4. On a `take` row, `result_r`, `cost_r`, `mae_r` and `mfe_r` are filled
   only if the order filled. A `take` that never filled keeps them empty,
   with `exit_reason` = `na`.
5. A `skip` or `wait` row never carries a real position. Its
   `executed_per_plan` and `exit_reason` are `na`, and `cost_r`, `mae_r`,
   `mfe_r`, `risk_pct` and `position_size` stay empty. A `result_r` there
   is read as a counterfactual and kept out of every statistic.
6. `reviewed_at` is later than `decided_at`.
7. `risk_pct` never exceeds the plan's maximum.

---

## The review routine

Run the review script on the working file (not on the template):

```
python3 tools/philosophy/journal_review.py <csv>
```

for example `python3 tools/philosophy/journal_review.py journal-2026.csv`.
The script reads exactly these 39 columns and writes a markdown review. Add
`--out <path>` to write it somewhere private rather than to the default
location inside the knowledge base. It counts only `take` rows with a
`result_r` as trades, treats a `result_r` on a `skip` or `wait` row as a
counterfactual, and marks any group with fewer than 30 trades as an
anecdote. Whatever it prints, each review must answer the questions below.
Anything it does not compute can be worked out by hand with the formulas
given here and in the Decision Protocol.

### After every session (5–10 minutes)

- Fill the post-trade fields of every row from the session, skips and waits
  included. Do not touch the pre-trade fields.
- Grade each decision separately from its outcome (protocol Gate 8.2).
- Treat the journal as a cool-down: what you felt, when focus slipped, and
  one *if–then* plan for tomorrow. (Jared Tendler's playbook,
  [[strategy_jared_tendler_psychology]], T2, frames post-session journaling
  this way.)

### Weekly

Run the script, then answer:

1. **Process.** What share of positions has `executed_per_plan` = `y`? For
   each `n`, which gate was skipped or bent? How many `take` rows had
   failing scores (impulse entries)?
2. **State.** Do the red and amber states in `emotional_state_pre` line up
   with the `n` rows or the worst results? Are trades taken just after a
   loss, or just after a win, different from the rest?
3. **Decisions.** How many takes, skips and waits? A week with many sound
   skips is a good week of process.
4. **Surprises.** Every row with `outcome_within_expected` = `n` gets the
   Section X questions answered in `lesson`, if that has not been done.
5. **Costs.** Is `cost_r` drifting above `est_cost_r`?
6. **Limits.** Were any loss limits hit, and were they respected?

**Allowed weekly actions:** tighten a limit, write `observe:` and `propose:`
entries, put a setup on hold. **Not allowed:** raising risk or changing a
setup's rules. Those wait for the monthly review and its larger sample
(Section XII: no changes from a few losses or a few wins).

### Monthly

Run the script, then work **per `setup_id`, split by `regime_tag`** (and by
`session` where the sample allows):

1. **Sample.** n live rows with a position; the forward and backtest files
   alongside, never merged.
2. **Realised statistics.** Win rate, average win R, average loss R, mean
   `result_r`, its standard deviation, `SE = sd / √n`, mean − 1 SE, mean −
   2 SE, and `t ≈ √n · mean / sd` ([[concept_performance_metrics]]).
3. **Calibration.** Mean `est_ev_r` against mean `result_r`; `est_win_prob`
   against the realised win rate. Estimates that run consistently above
   reality are the contradiction Section XVI warns about: calling a setup
   high probability without evidence.
4. **Costs.** Mean `cost_r` against mean `est_cost_r`. Is the mean result
   still positive net of costs?
5. **Path.** The MAE distribution of winners (this updates the Gate 2
   C-band); the MFE of losers (are targets realistic, is too much given
   back?); average loss above 1R (slippage or moved stops).
6. **Streaks and drawdown.** Compare the longest losing run and the deepest
   drawdown with what the setup's win rate and R-record predict
   (`ln(N·p) / ln(1/q)`, or a Monte Carlo reshuffle,
   [[concept_risk_of_ruin_drawdown]]). Section XI: neither dismiss a bad run
   nor panic over a normal one.
7. **Decision versus outcome.** Count the four cells (earned, variance,
   lucky, earned loss). A growing "lucky" count is a warning even in a
   profitable month.
8. **Strengths.** Review what went well as carefully as the mistakes. The
   knowledge base's journal note credits Brett Steenbarger with this
   approach ([[concept_trading_journal_review]]).
9. **The six open questions**, per setup (table below).

**Monthly actions:** update each setup card's estimates (these become the
`est_*` inputs for next month's trades); set the Gate 6 evidence factor;
decide the pending `propose:` entries, which become `revise:`, `retire:` or
"needs more data".

---

## How journal evidence feeds back into the hypotheses

The `hypothesis_update` column is the channel through which the market
corrects the model. Section II states the principle: the market need not
fit my understanding; my understanding has to keep being tested against
the market.

```
 decision row ──► post-trade review ──► hypothesis_update (observe / propose)
       ▲                                              │
       │                                              ▼
 Gate 5 est_* inputs ◄── setup card (conditions, ◄── monthly review
 for the next trade       estimates, version)        (revise / retire, on evidence)
```

### The update ladder

| Value | Who may write it | Meaning | Effect |
|---|---|---|---|
| `none` | any row | Nothing new about the setup. | None. |
| `observe: ...` | any row | A pattern worth watching. Name the tag or column that will track it. | A tag or note, nothing more. |
| `propose: ...` | any row, or the weekly review | A specific, testable change, plus the evidence that would accept or reject it. | Queued for the monthly review. |
| `revise: ...` | **monthly review only** | A change to the setup card's conditions, rules or estimates, justified by the sample. | New version (`-v2`); its sample starts from zero. |
| `retire: ...` | **monthly review only** | The evidence shows the setup's assumptions no longer hold. | Setup off; card archived with the reason. |

### Rules for changing a hypothesis

- **One trade can never revise a setup.** At most it can `observe` or
  `propose`. Section XII separates disciplined investigation from emotional
  pressure, and a single outcome is the purest form of pressure.
- **A revision creates a new version.** Section XVII warns that adjusting
  rules until they fit past results learns the noise. If v1's trades kept
  counting toward v2, development and evaluation would be mixed. v2 starts
  its own sample, is tested forward (paper, then small size) on data that
  did not suggest the change, and earns its `math_score` from scratch
  ([[concept_overfitting_validation]]).
- **Estimates update; conditions change rarely.** Refreshing `est_*` from a
  larger sample is routine. Changing *what the setup is* is a revision.
- **Retiring is allowed.** Section XII also says a method should not be
  defended indefinitely once the evidence shows its assumptions no longer
  hold. `retire:` is how the journal says so.
- **Skips feed back too.** Skips that repeatedly cite the same missing
  condition may point to a different setup worth defining and testing (the
  `EXAMPLE-` skip row shows this).
- **Counterfactuals are research, not grades.** You may record in a skip's
  `result_r` what the planned trade would have returned, measured
  mechanically from its planned entry, stop and target. The review script
  keeps these apart from real results. Use them only at the monthly review,
  to ask whether a filter is too strict or too loose
  ([[question_define_conditions]]). Never use them to grade the skip: a
  skip is judged by its reasons, and Section XIII says a missed opportunity
  does not justify abandoning discipline.

### Which columns answer the six open questions

Section XIX ([[philo_open_questions]]) lists what the philosophy still has
to prove. Each monthly review answers them, per setup, from the journal:

| Open question | Columns and statistics that answer it |
|---|---|
| [[question_repeatable_behaviors]] | `result_r` by `setup_id`: mean − 2 SE > 0 on live and forward rows; stability month to month |
| [[question_define_conditions]] | `regime_tag`, `session`, `evidence_score`, `evidence_against`: do the results change across the splits, and did borderline conditions behave differently? |
| [[question_estimate_reliability]] | `est_win_prob` against the realised win rate; `est_ev_r` against `result_r`; the SE of each estimate |
| [[question_survives_costs]] | `cost_r` against `est_cost_r`; mean `result_r` (already net) |
| [[question_survives_regime_change]] | `result_r` by `regime_tag` and by month; decay in mean R; rows tagged `event` or `unclear` |
| [[question_consistent_execution]] | `executed_per_plan`, `exit_reason` = `discretionary`, `emotional_state_pre` and `emotional_state_during` against results |

---

## The example rows in `journal-template.csv`

Both rows are hypothetical and marked `EXAMPLE-` in `setup_id`.

1. **`EX-2026-10-05-01`: take** (`EXAMPLE-sweep-reversal-v1`). The worked
   example of the Decision Protocol: every gate passes, the trade is sized
   at 0.43% after rounding down, an unscheduled headline pushes price
   through the stop, and the result is −1.17R net. The review grades it a
   good decision with an unfavourable outcome, the outcome as within the
   expected range, and the hypothesis update as `observe:` only.
2. **`EX-2026-10-07-01`: skip** (`EXAMPLE-compression-breakout-v1`). A
   breakout that looks convincing on the chart. A required condition is
   absent (the setup is defined for compression, and volatility is high), so
   `evidence_score` = 0. The provisional record is 18 paper trades, so the
   positive `est_ev_r` of 0.35R sits inside its own uncertainty. The row
   records `skip`, leaves the position and result fields empty, sets
   `executed_per_plan` = `na`, and proposes testing the idea as a separate
   setup.
