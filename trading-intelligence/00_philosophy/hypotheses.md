---
id: synthesis_philosophy_hypotheses
type: synthesis
title: "The Philosophy as Falsifiable Hypotheses"
partition: 00_philosophy
layer: L8
related: [philosophy_relationship, philo_open_questions, philo_scientific_method, synthesis_evidence_lab, synthesis_research_program]
status: synthesized
---

# The Philosophy as Falsifiable Hypotheses

> **Education, not financial advice. Not a trading signal.** Each entry below is a claim to be
> tested. A "supported" status means the data behaved as the claim says under the stated
> definitions. It does not mean any strategy is profitable, and none of the numbers is the win
> rate or P&L of a real account, trader or strategy.

The owner closes Section XIX ([[philo_open_questions]]) by asking that the philosophy say what it
believes, why it believes it, "and establish what evidence would demonstrate that it is wrong."
Section XVII ([[philo_scientific_method]]) asks that a theory meet actual outcomes before it is
treated as a method. This page does that for twenty claims drawn from the philosophy
([[philosophy_relationship]]). Each claim is restated precisely enough to be refuted. Each has an
observation that would refute it, written down before the result was read. And each has its
current evidence: the evidence lab ([[synthesis_evidence_lab]]) where a study has run, or "not yet
tested" where none has. The machine-readable registry is `hypotheses.yaml`, and the plan for the
untested claims is the research program ([[synthesis_research_program]]).

## How to read this page

**What an entry contains.** The claim. The sections and principles it comes from (`tests` in the
registry). What would refute it. The evidence so far, and a status. The layer is the knowledge
base's 9-layer stack ([[framework_ontology]]). Registry ids are shown in `code` so each entry can
be found in `hypotheses.yaml`.

**Statuses.**

| Status | Meaning |
|---|---|
| supported | A study tested the claim, and the data behaved as the claim states. |
| qualified | A study tested it, and the data agreed only in part, or only under conditions the claim does not state. |
| not-supported | A study tested it, and the refuting observation written in advance occurred. |
| untested | No study has tested it yet. The registry's `test_design` says how one would. |

A "study" is a pre-registered evidence-lab study published in `evidence-lab.md`, or, for the
journal hypotheses, a monthly journal review that meets the sample stated in the entry. Every
status other than "untested" on this page comes from the lab's studies S1–S7.

**What a status grades.** A status grades the operational statement on this page, not the
philosophy as a whole. The philosophy mostly speaks in careful conditionals: B is a hypothesis,
probability is conditional, a pattern *may* recur. Testing it means choosing one concrete version
of each idea: a target of 3 ATR, a trend filter built on two moving averages, a 5-day horizon.
Another reasonable version could come out differently. H2 is the clearest case. It is
not-supported, but it does not refute Section III, because Section III never claims that the size
of an adverse move decides its meaning.

**Four kinds of claim.**

- *Market claims* (H1–H6, H9–H11, H19) are about how prices behaved. Only data can settle them.
- *Mathematical claims* (H7, H12, H13) follow from their assumptions. The lab computed how large
  the effects are. What could fail is an assumption, such as independent trades or known
  parameters, and the lab argues that real conditions make each problem worse, not better.
- *Journal claims* (H8, H14–H18) are about the trader. They can only be tested on the owner's own
  records, kept as the trading journal requires ([[framework_trading_journal]]) and gathered
  through the decision protocol ([[framework_decision_protocol]]).
- *A method claim* (H20) is about whether one of the tools behaves as intended.

All numbers are copied from `evidence-lab.md` as regenerated on 2026-10-12. Data run to
2026-09-30. The in-sample period ends on 2012-12-31 and the out-of-sample period starts on
2013-01-01.

---

## A → C → B: detours and breakdowns (Section III)

Section III ([[philo_acb_principle]]) holds two ideas in tension. Price may move against a
hypothesis on the way to B. And yet B is, in the owner's words, "a hypothesized destination, not
a guaranteed one." Principles 2 and 3 ([[principle_02_context_before_movement]],
[[principle_03_future_is_uncertain]]) turn this into practice: read the move in its context, and
treat the destination as uncertain. Four claims separate what the evidence lab could test from
what it could not.

### H1. An adverse move weakens the hypothesis without settling it

`hypothesis_acb_detour_not_verdict` · **supported** · L2 · tests [[philo_acb_principle]],
[[principle_02_context_before_movement]], [[principle_03_future_is_uncertain]]

- **Claim.** Take a long hypothesis from A toward B = A + 3 ATR within 60 daily bars. If price
  first touches an adverse level C, between 0.5 and 3 ATR below A, the chance of still reaching B
  falls, but it stays well above zero in both trend regimes and both periods.
- **Refuted if.** At some depth up to 3 ATR, the 95% interval for P(B | C) lies entirely below
  5%, so the adverse move would settle the question. Or touching C does not lower P(B) at all, so
  the adverse move would cost nothing.
- **Evidence (S1).** Out of sample, a 1-ATR detour cut P(B) from 69.3% to 56.1% in uptrends and
  from 57.4% to 40.7% otherwise. After a 3-ATR detour, B was still reached 36.2% [30.7, 41.8] of
  the time in uptrends and 17.6% [12.5, 24.3] in the other regime.
- **Why supported.** Neither refuting observation occurred, at any depth or in either period.

### H2. A deep enough adverse move signals a breakdown

`hypothesis_depth_signals_breakdown` · **not-supported** · L2 · tests [[philo_acb_principle]],
[[principle_02_context_before_movement]], [[principle_07_respond_methodically]] · helps answer
[[question_define_conditions]]

- **Claim.** Past some depth, an adverse move carries information of its own. P(B | C) falls
  below what a *memoryless* market produces: a market with the same drift, volatility and regime,
  but no memory. That would make depth a usable breakdown signal.
- **Refuted if** (S1's pre-registered rule). No depth up to 3 ATR has an interval entirely below
  the memoryless null in both periods, in either regime.
- **Evidence (S1).** That is what happened, with and without the two futures series. The only
  single-period interval clear of the null was the out-of-sample uptrend at 3 ATR, and it sat
  *above* the null. That is 1 of 20 comparisons, about what chance alone produces.
- **What it means.** P(B) falls with depth for geometric reasons alone: from C the target is
  farther away and less time is left. On these data, depth added nothing beyond that geometry.
  Measuring depth is the most common way of turning the owner's caution, that not every adverse
  movement is merely a detour, into a rule, and it failed. So telling a breakdown from a detour needs something other than the size of the move,
  which is what Principle 2 asks for. H4 is the next candidate.

### H3. The context at A shapes the whole detour curve

`hypothesis_context_at_a_shapes_path` · **qualified** · L2 · tests [[philo_acb_principle]],
[[philo_recurring_storyline]], [[principle_02_context_before_movement]],
[[principle_04_conditional_probability]] · helps answer [[question_define_conditions]]

- **Claim.** The trend regime at A ([[concept_market_regimes]]) shifts P(B | C) at every depth,
  by more than the two regimes' different drift and volatility would produce on their own.
- **Refuted if.** Out of sample, the uptrend-minus-other gap has an interval that includes zero
  at most depths. Or, once each regime is measured against its own memoryless null, the gap is
  zero within its interval at every depth.
- **Evidence (S1).** Out of sample, the uptrend curve sat above the other curve by 12 points
  [+3, +20] unconditionally and by 19 points [+10, +26] at 3 ATR. The interval excluded zero at
  12 of 12 period-depth points. But the two memoryless nulls differ by about 10 points at both
  places. So 84% of the unconditional gap, and 51% of the 3-ATR gap, is drift and volatility
  alone.
- **Why qualified.** Context clearly matters. Most of its effect, though, is the plain difference
  between the days in an uptrend and the other days, not information about structure. The residual
  at depth is suggestive, and the lab did not test it formally.

### H4. A break of structure, not depth, separates breakdowns from detours

`hypothesis_structure_break_marks_breakdown` · **untested** · L2 · tests [[philo_acb_principle]],
[[philo_market_system_of_rules]], [[philo_evidence_changes]],
[[principle_02_context_before_movement]], [[principle_07_respond_methodically]] · helps answer
[[question_define_conditions]], [[question_repeatable_behaviors]]

- **Claim.** Take the paths that touch C before B. Those on which a defined structural
  invalidation came first reach B less often than the memoryless null. The invalidation here is a
  daily close below the last confirmed swing low before A ([[concept_market_structure]],
  [[concept_support_resistance]]). Paths whose structure stayed intact reach B at least as often
  as the null.
- **Refuted if.** Out of sample, the broken-structure paths are never below the null, or the
  intact-minus-broken difference includes zero at every depth. Structure would then add nothing to
  depth.
- **Evidence.** Not yet tested. This is the question S1 left open. The design is study S8 in the
  research program.

---

## Conditional probability and recurrence (Sections V, VI)

Section VI ([[philo_conditional_probability]]) asks for a probability that names its conditions.
Section V ([[philo_recurring_storyline]]) adds that recurrence is not repetition. Principle 4
([[principle_04_conditional_probability]]) is the rule that follows from both.

### H5. Defined conditions change the odds

`hypothesis_conditioning_changes_odds` · **qualified** · L2 · tests
[[philo_conditional_probability]], [[philo_recurring_storyline]],
[[principle_04_conditional_probability]] · helps answer [[question_define_conditions]],
[[question_repeatable_behaviors]]

- **Claim.** Conditioning on trend regime, realised-volatility tercile and one simple recurring
  pattern (three lower closes) moves the 5-day outcome away from the unconditional baseline in
  more cells than chance would.
- **Refuted if.** The number of in-sample "found" cells is no larger than a null without
  conditional structure produces.
- **Evidence (S2).** 11 of 74 judged cells differed in-sample, where about 4 would by chance.
  Eleven or more would happen with probability 0.0011 if the tests were independent. They are not
  independent: cells are nested, and the two metrics are correlated. 15 of 52 cells per metric
  had too few blocks to judge.
- **Why qualified.** The excess over chance is suggestive, not established. The test that would
  settle it, a permutation null that respects the nesting, has not been run.

### H6. A conditional tendency has to be re-earned in each period

`hypothesis_conditional_tendencies_decay` · **supported** · L8 · tests
[[philo_recurring_storyline]], [[philo_conditional_probability]],
[[principle_04_conditional_probability]], [[principle_03_future_is_uncertain]] · helps answer
[[question_survives_regime_change]], [[question_repeatable_behaviors]]

- **Claim.** Most conditional differences found in one period do not hold in the next. Fewer
  than half of the in-sample "found" cells keep their sign, with an interval excluding zero, out
  of sample.
- **Refuted if.** Half or more of them hold.
- **Evidence (S2).** Of the 11 found cells, 1 held: `^GSPC` after three down closes, mean 5-day
  return. The other 10 weakened, and none reversed. Even the unconditional baselines moved
  between periods. `^GSPC` P(up) went from 55.4% to 60.7% (+5.3 points [+1.9, +8.7]) and `^NDX`
  rose by +3.9 points [+0.2, +7.5]. For `EURUSD=X` and `GC=F` the change was within noise.
- **Why supported.** The data fit Section V's distinction between recurrence and repetition. A
  tendency measured in one period is a starting estimate for the next, not a law. One held cell out
  of 74 tests is itself weak evidence that anything recurs.

---

## Evidence, samples and selection (Sections VI, VII, XVII, XIX)

Section VI's law-of-large-numbers passage, Section VII's mathematics
([[philo_mathematics_sword]]) and Section XVII's warning about rules fitted to the past turn into
five claims about what a record can establish. Principle 5
([[principle_05_mathematical_justification]]) is the common thread.

### H7. A few dozen trades cannot confirm a thin edge

`hypothesis_small_samples_cannot_confirm` · **supported** · L0 · tests
[[philo_conditional_probability]], [[philo_mathematics_sword]],
[[principle_04_conditional_probability]], [[principle_05_mathematical_justification]] · helps
answer [[question_estimate_reliability]], [[question_repeatable_behaviors]]

- **Claim.** Take a real but thin edge: a 55% win rate, 1:1 payoff and 0.05R cost, for a true
  expectancy of +0.05R. Roughly a third of samples of 30 to 100 independent trades still show a
  non-positive expectancy, and only thousands of trades separate the edge from zero.
- **Refuted if.** The exact share of losing-looking samples is under 10%, or fewer than 1,000
  trades give 80% power. Empirically, it would also be refuted if real records converged faster
  than the independent-trade calculation assumes.
- **Evidence (S3).** 35.3% (exact 35.5%) of 30-trade samples and 30.7% of 100-trade samples looked
  like losing strategies. An interval that excludes zero needs about 1,522 trades on an average
  sample, and 3,109 for 80% power. The one empirical cell won 60.0% of 145 in-sample trades, with a
  Wilson interval of [51.9, 67.6]. Out of sample it won 48.6% of 37 trades.
- **Note.** This is mathematics about a hypothetical strategy ([[concept_expectancy]],
  [[concept_probabilistic_thinking]]). The same calculation for any setup is
  `python3 tools/philosophy/edge_lab.py sample --p <p> --rr <b> --cost <c>`.

### H8. My recorded probability estimates are calibrated

`hypothesis_estimates_are_calibrated` · **untested** · L8 · tests [[philo_journal]],
[[philo_conditional_probability]], [[principle_11_record_and_investigate]],
[[principle_04_conditional_probability]] · helps answer [[question_estimate_reliability]]

- **Claim.** The estimates frozen in the journal before each trade match what happened.
  `est_win_prob` agrees with the realised win rate bin by bin, and `est_ev_r` shows no systematic
  optimism against `result_r`.
- **Refuted if.** Over at least 100 closed trades, the mean of `est_ev_r − result_r` is more than
  two standard errors above zero. Or the realised win rate falls below the estimate's interval in
  two or more bins of 30 or more trades each. That is the contradiction Section XVI
  ([[philo_journal]]) predicts a journal may expose: calling a setup high probability without
  the evidence.
- **Evidence.** Not yet tested. `journal_review.py` already computes the calibration table.

### H9. Costs decide whether a selected short-horizon edge is worth trading

`hypothesis_edge_survives_costs` · **qualified** · L1 · tests [[philo_mathematics_sword]],
[[philo_scientific_method]], [[principle_05_mathematical_justification]] · helps answer
[[question_survives_costs]]

- **Claim.** Take a short-horizon edge chosen on in-sample daily data. Its out-of-sample
  break-even cost per side is below a realistic cost for the instrument, so it does not survive
  costs, even when it looked robust to them in-sample.
- **Refuted if.** At a cost assumption fixed before the run, the selected edge's out-of-sample
  net expectancy has mean − 1 SE > 0.
- **Evidence (S7).** The best in-sample cell (`^GSPC` · 3-down · other · high vol) had an
  in-sample break-even of 35.8 bp per side, far above the 1–10 bp tested. Out of sample its gross
  expectancy was already −25 bp per trade [−168, +117], so there was no break-even at all. Costs
  only deepened the loss, to −29 bp at 2 bp per side.
- **Why qualified.** The claim's conclusion held, but not for the claim's reason. The change of
  period, not the costs, removed the edge, so the specific question of whether costs turn a real
  edge into a loss was never exercised. Testing it needs an edge that is still positive before
  costs out of sample ([[concept_trade_execution]], [[concept_market_microstructure]]).

### H10. What wins in-sample loses most of its edge out of sample

`hypothesis_in_sample_winner_decays` · **supported** · L8 · tests [[philo_scientific_method]],
[[philo_recurring_storyline]], [[principle_05_mathematical_justification]],
[[principle_03_future_is_uncertain]] · helps answer [[question_survives_regime_change]],
[[question_repeatable_behaviors]]

- **Claim.** An advantage chosen as the best of many candidates in-sample is smaller out of
  sample. Its excess over the benchmark shrinks.
- **Refuted if.** Selections made in-sample keep, on average, at least their in-sample excess.
- **Evidence (S5, S7).** The S5 winner's Sharpe advantage over buy and hold went from 0.18 to
  −0.01. Its absolute Sharpe rose with the market, from 0.63 to 0.80, so the rule did not collapse;
  only its advantage over simply holding disappeared. The S7 cell went from +72 bp per trade to
  −25 bp before costs, while a 5-day long trade on every eligible day earned +27 bp.
- **Limit.** Each study is one split of one or two markets. The program replaces the single split
  with rolling windows.

### H11. Searching many rules manufactures an apparent edge

`hypothesis_search_manufactures_edges` · **supported** · L8 · tests [[philo_scientific_method]],
[[philo_research_foundations]], [[principle_05_mathematical_justification]] · helps answer
[[question_repeatable_behaviors]]

- **Claim.** On data with no exploitable structure, the best of a few hundred variants still
  beats buy and hold in-sample. An in-sample winner therefore counts as evidence only if it
  beats what the same search finds on no-signal data ([[concept_overfitting_validation]],
  [[paper_deflated_sharpe_2014]]).
- **Refuted if.** On permuted copies of the data, the best variant does no better than holding.
- **Evidence (S5).** On 20 no-signal copies, the best of 238 rules averaged a Sharpe of 0.52
  against 0.46 for holding, an advantage of up to 0.25 from selection alone. The real winner's
  advantage of 0.18 sat inside that range. Its deflated Sharpe was 0.78 and the permutation
  p-value 0.14.
- **Limit.** Twenty permutations is a small number. The deflated Sharpe treats 238 correlated
  variants as independent trials, which makes it conservative.

---

## Risk and survival (Section XIV)

### H12. Bet size, not the edge, decides survival

`hypothesis_ruin_set_by_size` · **supported** · L6 · tests [[philo_capital_preservation]],
[[principle_09_protect_capital]] · helps answer [[question_consistent_execution]]

- **Claim.** Hold a positive-expectancy edge fixed. The chance of a 50% drawdown within 250
  trades rises from near zero at 1% risk per trade to near certainty at 10%. Beyond full Kelly,
  more risk lowers even the median outcome ([[concept_risk_of_ruin_drawdown]],
  [[concept_kelly_criterion_optimal_f]]).
- **Refuted if.** The ruin probability does not rise with risk, or the median keeps rising past
  full Kelly.
- **Evidence (S4).** The same edge (p = 0.35 at 2.5R, EV +0.175R) hit a 50% drawdown in 1 of
  10,000 simulated paths at 1% risk, and in 9,997 of 10,000 at 10%. Past its Kelly fraction of
  6.8%, the median final equity fell from 3.54 at 5% risk to 2.67 at 10%. The owner's own
  arithmetic in Section XIV holds as well: a 50% loss needs +100% to recover.
- **Note.** This is mathematics with known, constant parameters. Real estimates are uncertain
  (H7), which argues for sizing below these levels, not above them.

---

## Decisions, outcomes and the trader (Sections IX–XIII, XVI)

These claims concern the decision-maker more than the market. Section XI ([[philo_being_wrong]])
and Section XIII ([[philo_decisions_not_money]]) separate a decision from its result. Section IX
([[philo_step_back]]) treats waiting as a decision. Section XII ([[philo_protect_process]]) names
the emotions that bend a method. Section XVI ([[philo_journal]]) admits that a journal "cannot
eliminate hindsight bias by itself." All but H13 must be tested on the owner's own journal.

### H13. Short-run results are a weak verdict on a decision

`hypothesis_outcomes_misjudge_decisions` · **supported** · L8 · tests [[philo_being_wrong]],
[[philo_decisions_not_money]], [[philo_mathematics_sword]],
[[principle_08_decision_quality_not_outcome]], [[principle_12_process_not_money]] · helps answer
[[question_estimate_reliability]]

- **Claim.** Over 20 to 100 trades, the sign of the running P&L poorly separates the +$7 strategy
  of Section VII from a −$4 twin with the same payoffs. One is behind, or the other ahead, more
  than 20% of the time at every horizon up to 100 trades.
- **Refuted if.** Either probability is below 10% after 20 trades.
- **Evidence (S6).** After 20 trades the +$7 strategy is behind 40.4% of the time, and the −$4
  twin is ahead 41.4%. The two chances stay below 5% only from 663 and 2,060 trades respectively.
  For this page, the 20% bound was also checked at every horizon from 1 to 100 trades with the
  same exact binomial; the lowest values were 23.1% and 30.3%.

### H14. Good decisions earn more over a large sample, though not trade by trade

`hypothesis_good_decisions_earn_more` · **untested** · L8 · tests [[philo_being_wrong]],
[[philo_source_of_opportunity]], [[principle_08_decision_quality_not_outcome]],
[[principle_11_record_and_investigate]] · helps answer [[question_consistent_execution]],
[[question_repeatable_behaviors]]

- **Claim.** Positions graded good decisions earn a higher mean net R than positions graded poor
  decisions, once each group is large enough. A good decision means all three gate scores at 2,
  size within the rules and execution per plan. The grade is set from the frozen pre-trade fields,
  never from the result.
- **Refuted if.** With at least 50 positions per group, the interval for the difference (good
  minus poor) lies at or below zero. An interval that still includes zero means "not yet shown":
  detecting a 0.3R difference needs about 175 positions per group.
- **Evidence.** Not yet tested. This is the journal's version of H13. If decisions graded good
  do not earn more over a large sample, the protocol's definition of a good decision is wrong.

### H15. Stepping back leaves fewer, better-justified trades

`hypothesis_step_back_selects_better_trades` · **untested** · L7 · tests [[philo_step_back]],
[[philo_source_of_opportunity]], [[principle_06_do_not_force]],
[[principle_01_understand_before_acting]] · helps answer [[question_consistent_execution]],
[[question_define_conditions]]

- **Claim.** Candidates set aside because a gate failed would have earned less than the trades
  taken. Here a gate failure means any score below 2, an unclear regime, or over-watching. The
  counterfactual result is measured mechanically from the planned entry, stop and target. So
  standing aside raises the expectancy per trade while cutting the number of trades.
- **Refuted if.** With at least 50 counterfactual skips and 100 takes, the takes' advantage has
  an interval whose upper bound is below +0.1R. The filter would then be removing trades no worse
  than the ones it keeps.
- **Evidence.** Not yet tested. The journal template allows mechanical counterfactuals for
  research only, never for grading a skip. A daily-data proxy that skips mixed-signal days is
  also in the program.

### H16. The frozen journal record removes hindsight from the review

`hypothesis_journal_reduces_hindsight` · **untested** · L8 · tests [[philo_journal]],
[[philo_being_wrong]], [[principle_11_record_and_investigate]],
[[principle_08_decision_quality_not_outcome]] · helps answer [[question_estimate_reliability]],
[[question_consistent_execution]]

- **Claim.** Asked to recall a past decision after seeing its outcome, I remember a higher win
  probability after wins and a lower one after losses than I actually wrote down. Reviewing from
  the frozen record removes that shift.
- **Refuted if.** Over at least 60 recalled decisions, the outcome-dependent shift has an
  interval that includes zero with an upper bound below 3 points. Memory would then not be bent
  by outcomes, and the frozen record would add rigour but remove no bias.
- **Evidence.** Not yet tested. It needs a short recall exercise at the weekly review, kept
  outside the journal.

### H17. A loss degrades the next decision

`hypothesis_losses_impair_next_decision` · **untested** · L7 · tests [[philo_protect_process]],
[[philo_decisions_not_money]], [[principle_10_emotional_independence]],
[[principle_12_process_not_money]] · helps answer [[question_consistent_execution]]

- **Claim.** Decisions taken right after a loss, or in an amber or red state, follow the plan less
  often and earn less than decisions after a win or a scratch in a green state. This holds even
  with the protocol's post-loss pause. Section XII describes this pressure: after a loss, the urge
  to recover can outgrow the commitment to the method.
- **Refuted if.** With at least 50 post-loss decisions and 50 others, plan adherence differs by
  less than 5 points, and the result difference lies within ±0.1R. If so, either the pause works
  or the effect is absent for this trader.
- **Evidence.** Not yet tested. `journal_review.py` already splits results after a win from
  results after a loss and groups them by emotion colour. Prospect theory
  ([[paper_kahneman_tversky_1979]]) is the behavioural prior.

### H18. Pre-defined exits prevent riding losers and cutting winners

`hypothesis_predefined_exits_curb_disposition` · **untested** · L5 · tests
[[philo_evidence_changes]], [[philo_protect_process]], [[principle_07_respond_methodically]],
[[principle_10_emotional_independence]] · helps answer [[question_consistent_execution]]

- **Claim.** Exits outside the plan show the disposition pattern described by Shefrin and Statman
  ([[paper_shefrin_statman_1985]]): winners closed before target more often than losers closed
  before stop, and losses running past −1R. Exits by stop, invalidation, evidence change, time
  stop or pre-written management show neither pattern. Section X ([[philo_evidence_changes]])
  says to manage the risk first and investigate second. This is the measurable version.
- **Refuted if.** With at least 30 discretionary exits, the early-exit rates of winners and
  losers differ by less than 10 points, and discretionary losses are no worse than rule-based ones.
- **Evidence.** Not yet tested.

---

## Value and price (Section XV)

### H19. A gap between price and value is not an edge by itself

`hypothesis_value_gap_not_edge` · **untested** · L3 · tests [[philo_value_vs_price]],
[[philo_price_expression]], [[principle_05_mathematical_justification]],
[[principle_04_conditional_probability]] · helps answer [[question_repeatable_behaviors]],
[[question_survives_costs]], [[question_define_conditions]]

- **Claim.** On daily bars, a close far from a defined value estimate does not by itself give a
  positive expectancy after costs out of sample. Far means more than 2 ATR. The estimate is a
  20-day volume-weighted price, or the 200-day average where volume is missing
  ([[concept_vwap]], [[concept_mean_reversion]], [[concept_auction_market_theory]]). Any reversion
  toward value shows up only under stated conditions. Section XV ends on this point: "The existence
  of a perceived discrepancy is the beginning of an investigation, not proof of an edge."
- **Refuted if.** The unconditional gap trade earns mean − 2 SE > 0 net of costs, out of sample,
  in at least three of four markets: the gap alone would then be an edge. Also refuted if
  conditioning on regime does no better than not conditioning.
- **Evidence.** Not yet tested. This is study S9 in the program. A statistical value estimate is
  a narrow stand-in for the valuations Section XV has in mind. A fundamental version needs
  valuation data that the cache does not hold.

---

## The method's own instruments (Sections X, XI)

### H20. The losing-run check tells ordinary variance from a broken edge

`hypothesis_losing_run_check_calibrated` · **untested** · L8 · tests [[philo_being_wrong]],
[[philo_evidence_changes]], [[principle_07_respond_methodically]],
[[principle_08_decision_quality_not_outcome]] · helps answer
[[question_survives_regime_change]], [[question_estimate_reliability]]

- **Claim.** Section XI asks for a way to tell whether a losing run is ordinary variation or a
  sign that the strategy's assumptions no longer hold. `consistency_check` in `edge_lab.py` is
  that way. The claim is that it raises a flag on no more than 10% of 40-trade runs drawn from the
  strategy itself, and on at least half of the runs from a version whose win rate has fallen from
  55% to 40%.
- **Refuted if.** The false-alarm rate in seeded simulation is above 10% (or above 2% for the
  "inconsistent" verdict), or the detection rate is below 50%.
- **Evidence.** Not yet tested. The "unusual" verdict uses the smallest raw p-value of several
  tests, so its false-alarm rate should exceed 5%. Whether it stays under 10% is the open question.
  The simulation needs no market data and can run first.

---

## Summary

| hypothesis | status | evidence |
|---|---|---|
| H1 An adverse move weakens the hypothesis without settling it (`hypothesis_acb_detour_not_verdict`) | supported | S1: OOS, a 1-ATR detour cut P(B) from 69.3% to 56.1% (uptrend) and 57.4% to 40.7% (other); after 3 ATR still 36.2% / 17.6% |
| H2 A deep enough adverse move signals a breakdown (`hypothesis_depth_signals_breakdown`) | not-supported | S1: no depth up to 3 ATR below the memoryless null in both periods, either regime, with or without futures |
| H3 The context at A shapes the whole detour curve (`hypothesis_context_at_a_shapes_path`) | qualified | S1: OOS gap +12 points [+3, +20], +19 at 3 ATR; 84% and 51% of it reproduced by the nulls |
| H4 A break of structure, not depth, separates breakdowns from detours (`hypothesis_structure_break_marks_breakdown`) | untested | not yet tested (proposed S8) |
| H5 Defined conditions change the odds (`hypothesis_conditioning_changes_odds`) | qualified | S2: 11 of 74 cells differed in-sample vs about 4 by chance; tests not independent |
| H6 A conditional tendency has to be re-earned in each period (`hypothesis_conditional_tendencies_decay`) | supported | S2: 1 of 11 found cells held OOS, 10 weakened; `^GSPC` and `^NDX` baselines moved beyond noise |
| H7 A few dozen trades cannot confirm a thin edge (`hypothesis_small_samples_cannot_confirm`) | supported | S3: a +0.05R edge looks like a loser in 35% of 30-trade samples; 3,109 trades for 80% power |
| H8 My recorded probability estimates are calibrated (`hypothesis_estimates_are_calibrated`) | untested | not yet tested (journal) |
| H9 Costs decide whether a selected short-horizon edge is worth trading (`hypothesis_edge_survives_costs`) | qualified | S7: IS break-even 35.8 bp/side; OOS gross already −25 bp, so costs were not the deciding factor |
| H10 What wins in-sample loses most of its edge out of sample (`hypothesis_in_sample_winner_decays`) | supported | S5: edge over buy and hold 0.18 → −0.01; S7: +72 → −25 bp per trade |
| H11 Searching many rules manufactures an apparent edge (`hypothesis_search_manufactures_edges`) | supported | S5: no-signal best 0.52 vs 0.46 holding; DSR 0.78; permutation p = 0.14 |
| H12 Bet size, not the edge, decides survival (`hypothesis_ruin_set_by_size`) | supported | S4: 50% drawdown in 1 of 10,000 paths at 1% risk vs 9,997 of 10,000 at 10% |
| H13 Short-run results are a weak verdict on a decision (`hypothesis_outcomes_misjudge_decisions`) | supported | S6: after 20 trades the +$7 strategy is behind 40.4%, the −$4 twin ahead 41.4% |
| H14 Good decisions earn more over a large sample (`hypothesis_good_decisions_earn_more`) | untested | not yet tested (journal) |
| H15 Stepping back leaves fewer, better-justified trades (`hypothesis_step_back_selects_better_trades`) | untested | not yet tested (journal; daily-data proxy proposed) |
| H16 The frozen journal record removes hindsight from the review (`hypothesis_journal_reduces_hindsight`) | untested | not yet tested (recall protocol) |
| H17 A loss degrades the next decision (`hypothesis_losses_impair_next_decision`) | untested | not yet tested (journal) |
| H18 Pre-defined exits prevent riding losers and cutting winners (`hypothesis_predefined_exits_curb_disposition`) | untested | not yet tested (journal) |
| H19 A gap between price and value is not an edge by itself (`hypothesis_value_gap_not_edge`) | untested | not yet tested (proposed S9) |
| H20 The losing-run check tells ordinary variance from a broken edge (`hypothesis_losing_run_check_calibrated`) | untested | not yet tested (simulation) |

**Count:** 7 supported, 3 qualified, 1 not-supported, 9 untested.

### Which hypotheses bear on which open question

| Open question (Section XIX) | Hypotheses |
|---|---|
| [[question_repeatable_behaviors]] | H4, H5, H6, H7, H10, H11, H14, H19 |
| [[question_define_conditions]] | H2, H3, H4, H5, H15, H19 |
| [[question_estimate_reliability]] | H7, H8, H13, H16, H20 |
| [[question_survives_costs]] | H9, H19 |
| [[question_survives_regime_change]] | H6, H10, H20 |
| [[question_consistent_execution]] | H12, H14, H15, H16, H17, H18 |

## How a status changes

1. **A new study is pre-registered first.** Its parameters, its verdict rule and the refuting
   observation are fixed in code before the first run, as in the evidence lab. Anything changed
   after seeing results is logged as a deviation.
2. **Out-of-sample data are used once.** An out-of-sample period that has guided a change is no
   longer out of sample for that change.
3. **Journal hypotheses wait for their sample.** Below the minimum stated in each entry, a journal
   result is an anecdote and the status stays "untested". The protocol's rule holds here too: one
   trade can never revise anything.
4. **A refuted hypothesis stays in the registry.** Its status becomes not-supported, and the
   evidence says what happened. If the philosophy's wording seems to be at stake, the case is
   raised with the owner as a suggestion. The philosophy text is never edited.

## What this page does not show

That any strategy is profitable, or that the philosophy is. The supported hypotheses concern
method: how evidence, samples, selection and size behave. That is what Section XIX means when it
separates internal coherence from proof of profitability. The market claims rest on two periods,
a handful of daily series and one simple version of each idea. Half the registry is untested, and
most of that half can only be tested by the owner's own journal.
