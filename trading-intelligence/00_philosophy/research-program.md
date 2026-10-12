---
id: synthesis_research_program
type: synthesis
title: "Research Program — what the philosophy still needs to prove"
partition: 00_philosophy
layer: L8
related: [philosophy_relationship, philo_open_questions, philo_research_foundations, synthesis_philosophy_hypotheses, synthesis_evidence_lab, framework_trading_journal]
status: synthesized
---

# Research Program — what the philosophy still needs to prove

> **Education, not financial advice. Not a trading signal.** This is a plan for testing ideas.
> Nothing here recommends trading any instrument, setup or size. Every example number is either
> copied from the evidence lab or computed by `tools/philosophy/edge_lab.py` from hypothetical
> inputs, and is labelled as such.

Section XIX ([[philo_open_questions]]) separates a philosophy that is internally coherent from one
that is shown to work, and asks six questions that only research and testing can answer. The
owner calls these questions "the next stage of its development." Section XX
([[philo_research_foundations]]) names the fields to draw on: microstructure, probability and
inference, behavioural finance, backtest overfitting, and risk management.

This page turns the six questions into a research program. For each question it gives:

- what the evidence lab ([[synthesis_evidence_lab]]) has already answered;
- which of the twenty hypotheses ([[synthesis_philosophy_hypotheses]]) bear on it;
- the next studies, with the commands to run them;
- the data each study needs;
- success and failure criteria, fixed now, before any of these studies is run;
- a reading list.

The page ends with a 12-week plan. It runs from the philosophy to one method that has been
tested on history, run forward under the decision protocol ([[framework_decision_protocol]]) and
recorded in the trading journal ([[framework_trading_journal]]).

---

## Ground rules for every study

These are the evidence lab's own rules, applied to everything that follows.

1. **Pre-register.** Fix the parameters, the verdict rule and the refuting observation in code
   before the first run (a `PARAMS` block, as at the top of `studies.py`). Log anything changed
   after seeing a result as a deviation, with the reason.
2. **Keep development and evaluation apart.** Daily-data studies reuse the lab's split: in-sample
   up to 2012-12-31, out-of-sample from 2013-01-01, with outcome windows purged at the boundary.
   The 2013–2026 period has already been looked at, by the lab and by anyone who watched those
   markets. So bars after 2026-09-30, and the forward journal, are the only data nobody has seen.
   Treat them as the final holdout.
3. **Count every try.** Report the number of variants tested. Correct a pre-registered family of
   tests with the Holm method. Give any rule search a deflated Sharpe ratio
   ([[paper_deflated_sharpe_2014]]) and a permutation test.
4. **Fix costs before the run.** Use at least two cost levels, one of them pessimistic. In the
   journal, use the measured `cost_r`, never an assumption.
5. **Respect dependence.** Use non-overlapping trades, or a block bootstrap, for every interval.
6. **Statuses change only by rule.** A hypothesis moves from "untested" only after a
   pre-registered study, or a journal review that meets its stated sample. The rules are in
   `hypotheses.md`.
7. **The journal stays honest.** Live, forward (paper) and backtest rows go in separate files.
   Pre-trade fields are frozen at `decided_at`. One trade never revises a setup.

## Tools: what exists and what is proposed

| Command | State | Use |
|---|---|---|
| `python3 tools/philosophy/market_data.py [SYMBOLS] [--refresh]` | exists | Download and cache daily bars (git-ignored cache). The current cache holds `^GSPC`, `^NDX`, `GC=F`, `CL=F`, `EURUSD=X`, `ES=F`, `NQ=F`, `^VIX` and `BTC-USD`. |
| `python3 tools/philosophy/studies.py [--refresh]` | exists | Run S1–S7 and regenerate `evidence-lab.md` and `figures/`. |
| `python3 tools/philosophy/edge_lab.py {ev,breakeven,wilson,streak,ruin,sample,kelly,recover}` | exists | Expected value, intervals, sample plans, streaks, ruin, Kelly under uncertainty, recovery. |
| `python3 tools/philosophy/journal_review.py JOURNAL.csv --out PRIVATE.md [--window N] [--min-ref N] [--gate-min N]` | exists | Calibration, conditional results, decision-quality matrix, plan adherence, after-win and after-loss results, emotion bands, consistency of recent results. |
| `python3 -m pytest -q tools/philosophy/tests` | exists | The toolkit's test suite. Run it before trusting any new result. |
| Studies S8–S15 below | **proposed** | To be added to `studies.py`, each with its own pre-registered `PARAMS` entry, and run by the existing `studies.py` command. None of them exists yet. |

Always pass `--out` to a private path when reviewing a real journal. The default output path is
inside the knowledge base.

### Proposed studies

| Study | What it tests | Hypotheses | Data |
|---|---|---|---|
| S8 Structure break versus depth | Whether a pre-defined break of swing structure tells breakdowns from detours, where depth did not | H4 | Cached daily bars (S1 markets, plus `ES=F` and `NQ=F`) |
| S9 Value gap | Whether a large gap from a defined value estimate is an edge on its own, or only conditionally | H19 | Daily bars with volume (`^GSPC`, `^NDX`, `ES=F`, `NQ=F`); SMA proxy for `GC=F` |
| S10 Rolling persistence | S2 cells and S5 rules re-selected and re-evaluated in rolling windows (select on 10 years, evaluate on the next 3, step 1 year) | H6, H10 | Cached daily bars |
| S11 Consistency-check calibration | False-alarm and detection rates of `consistency_check` | H20 | None (simulation) |
| S12 Search robustness | S5 with 1,000 permutations, a Reality Check bootstrap ([[paper_white_2000]]) and the probability of backtest overfitting ([[paper_bailey_pbo_2017]]) | H11 | `^GSPC`, `ES=F` |
| S13 Unclear-regime proxy | Whether skipping mixed-signal days (trend filters disagree) raises expectancy per trade | H15 | Cached daily bars |
| S14 Costs on a surviving edge | S7's cost grid applied to an edge that is still positive out of sample before costs, on a tradable series | H9 | `ES=F`, `NQ=F` (roll-aware returns), journal `cost_r` |
| S15 Conditioning, done properly | A block-permutation null for the number of "found" S2 cells, and a direct test of whether one pattern behaves differently across contexts | H5 | S2 markets; `^VIX` as a pre-registered extra condition |

---

## Question 1 — [[question_repeatable_behaviors]]

*Which market behaviours are genuinely repeatable?*

**What the lab already answered.** So far, no behaviour has been shown to repeat in a form anyone
could trade. Of 11 conditional cells found in-sample, one held out of sample (S2: `^GSPC` after
three lower closes, mean 5-day return). That is a statistical tendency, not a setup, and one cell
in 74 tests is weak evidence. The best of 238 trend rules kept its Sharpe ratio but lost its
advantage over buy and hold (S5: 0.18 to −0.01). The best conditional cell lost its edge before
costs (S7: +72 to −25 bp per trade). The lab also showed how much a search can manufacture on its
own: on no-signal data, the best of 238 rules beat holding by up to 0.25 Sharpe (S5).

**Hypotheses.** H4, H5, H6, H7, H10, H11, H14, H19.

**Next studies.**

1. **S10.** Re-test the one held cell and every S2 cell in rolling windows, on the original
   markets and on `ES=F` and `NQ=F`, which did not help find them.
2. **S12.** Rerun S5's search with 1,000 permutations, a Reality Check and the probability of
   backtest overfitting.
3. **S8 and S9.** Two new candidate behaviours, each pre-registered with at most two variants.
4. **J2 and J3** (journal). The owner's own setup, judged on forward and live rows only.

```bash
python3 tools/philosophy/market_data.py ES=F NQ=F      # make sure the extra series are cached
python3 tools/philosophy/studies.py                    # after S8-S10 and S12 are added
python3 -m pytest -q tools/philosophy/tests
```

**Data needed.** The cached daily bars. `ES=F` and `NQ=F` are continuous front-month series
without back-adjustment, so S10 and S14 must handle the roll jumps (drop the roll day, or build
roll-aware returns). The lab's caveat on `GC=F` and `CL=F` applies here too.

**Decided in advance.**

- *Success.* A behaviour counts as repeatable only if all four of these hold:
  1. its rule was written before the test;
  2. its effect has the same sign in at least 70% of the rolling evaluation windows;
  3. its pooled out-of-sample interval excludes zero after Holm correction across the family;
  4. it holds in at least one market that played no part in finding it.

  For a tradable setup, add the protocol's evidence rule (Gate 5.4): mean R − 2 SE > 0 after
  costs on forward and live records, with n ≥ 30.
- *Failure.* The behaviour is recorded as not repeatable if the same sign appears in 50% of
  windows or fewer, or the pooled interval includes zero. If the held S2 cell fails S10, H6's
  conclusion extends to the only cell that had survived.

**Reading.**

- [[book_evidence_based_ta]]: the scientific method and data-snooping corrections applied to
  chart rules.
- [[book_non_random_walk]]: what statistical tests of return predictability can and cannot show.
- [[mathbook_campbell_lo_mackinlay]]: the econometrics behind the same tests.
- [[paper_white_2000]]: a bootstrap test for the best of many models.
- [[paper_harvey_liu_zhu_2016]]: why a discovery found among many tests needs a higher bar than
  the usual t of 2.
- [[paper_mclean_pontiff_2016]]: evidence that published return predictors weaken out of sample
  and after publication.
- [[book_encyclopedia_chart_patterns]]: one practitioner's way of counting pattern outcomes. Read
  it for the counting method, not for its percentages.
- [[book_random_walk_down_wall_street]]: the null hypothesis, stated by its advocate.

---

## Question 2 — [[question_define_conditions]]

*How should the relevant conditions be defined and measured?*

**What the lab already answered.**

- A simple trend filter shifted the whole detour curve. Most of that shift came from the regimes'
  different drift and volatility, not from anything specific to structure (S1, H3).
- The depth of an adverse move, on its own, carried no breakdown information (S1, H2).
- Conditions built from trend and volatility moved the odds in more cells than chance would, but
  most differences were within noise (S2, H5).
- Every added condition splits the sample. Fifteen of 52 S2 cells per metric had too few
  independent blocks to judge. Conditions defined too finely run out of data before they run out
  of meaning.

**Hypotheses.** H2, H3, H4, H5, H15, H19.

**Next studies.**

1. **S8.** Structure as a condition, with the swing rule fixed in advance and confirmed only with
   past bars.
2. **S15.** A permutation null that respects the nesting of cells, a direct test of whether one
   pattern behaves differently across the six contexts, and `^VIX` as one pre-registered
   alternative to realised volatility.
3. **S13.** Mixed-signal days as a mechanical version of "unclear".
4. **J8** (journal). A labelling-agreement check: once a month, re-label the `regime_tag` of 50
   random past rows without looking at the original labels, then compare.

**Data needed.**

- Cached daily bars, and `^VIX`.
- For session-level conditions (the journal's `session` column and kill-zone ideas,
  [[concept_trading_sessions_killzones]]): intraday bars, which the cache does not hold. Those
  conditions stay journal-only until intraday data are added.
- Journal columns `regime_tag`, `session`, `evidence_score` and `evidence_against`.

**Decided in advance.** A condition is accepted only if it is:

1. computable from data available at decision time by a written rule;
2. reproducible: two runs label the same days identically, and a discretionary tag reaches at
   least 80% agreement in J8;
3. informative: out of sample, the conditional estimate differs from the baseline with a
   Holm-adjusted interval that excludes zero;
4. adequately sampled: at least 10 bootstrap blocks, or 30 trades, per cell.

*Failure.* A condition that fails test 3 in two separate studies is removed from the setup cards.
A discretionary tag with less than 60% agreement is rewritten as a rule, or dropped.

**Reading.**

- [[mathbook_hamilton_time_series]]: regime-switching models, a formal version of "conditions".
- [[mathbook_tsay_financial_time_series]]: volatility models and how to measure volatility.
- [[book_systematic_trading]]: writing conditions as rules, and the cost of adding too many.
- [[mathbook_isl]]: the bias–variance trade-off, and cross-validation for choosing how many
  conditions to use.
- [[book_advances_financial_ml]]: labelling events and purging overlap between training and test
  data.
- [[book_art_science_technical_analysis]]: chart conditions defined so that they can be counted.
- [[paper_lo_adaptive_markets_2004]]: why the relevant conditions themselves can change.

---

## Question 3 — [[question_estimate_reliability]]

*How reliable are the probability estimates?*

**What the lab already answered.** For thin edges, an estimate from a realistic personal sample is
not reliable enough to tell an edge from zero.

- A true +0.05R edge looks like a loser in 35.3% of simulated 30-trade samples (35.5% exact), and
  separating it from zero with 80% power takes about 3,109 trades (S3, H7).
- The lab's one empirical cell won 60.0% of 145 trades in-sample, with a Wilson interval of
  [51.9, 67.6]. Out of sample it won 48.6% of 37 trades.
- Even with the parameters known exactly, the +$7 strategy of Section VII is behind after 20
  trades 40.4% of the time (S6, H13).

The decision protocol already acts on this. Its floor is n ≥ 30, and its sizing rule uses mean −
1 SE and mean − 2 SE, so a thin edge has to earn its sample (Gates 5.4 and 6.2).

**Hypotheses.** H7, H8, H13, H16, H20.

**Next studies.**

1. **S11.** The false-alarm and detection rates of `consistency_check`. It needs no data, so it
   can run first, and it can run today with the existing API:

   ```python
   # run from the repository root; seeds fixed; nothing here is a trading result
   import sys; sys.path.insert(0, "tools/philosophy")
   import numpy as np
   from edge_lab import consistency_check, VERDICT_WITHIN, VERDICT_INCONSISTENT
   rng = np.random.default_rng(20261012)
   def run(p, n, cost=0.05):                      # 1:1 payoff, cost in R
       return np.where(rng.random(n) < p, 1.0, -1.0) - cost
   ref = run(0.55, 300)                           # reference record for the drawdown bootstrap
   ref_mean, ref_sd = 0.55 * 2 - 1 - 0.05, 2 * (0.55 * 0.45) ** 0.5
   def rates(p, runs=10_000, n=40):
       v = [consistency_check(run(p, n), 0.55, ref_mean, ref_sd, ref_results=ref,
                              n_boot=2000, seed=i).verdict for i in range(runs)]
       return {"flagged": np.mean([x != VERDICT_WITHIN for x in v]),
               "inconsistent": np.mean([x == VERDICT_INCONSISTENT for x in v])}
   print("false alarms:", rates(0.55)); print("detection:", rates(0.40))
   ```

2. **J1** (journal). Calibration of `est_win_prob` and `est_ev_r` against outcomes (H8), run
   with `journal_review.py`.
3. **J4** (journal). The weekly recall exercise for hindsight (H16).
4. **At every monthly review**, for each setup card, write down how many trades the current
   estimate would need. The examples below use hypothetical inputs:

   ```bash
   python3 tools/philosophy/edge_lab.py sample --p 0.45 --rr 2 --cost 0.05
   #   +0.300R, sd 1.492R: 96 trades on an average sample, 195 for 80% power
   python3 tools/philosophy/edge_lab.py wilson --wins 18 --n 30 --threshold 0.5
   #   18/30: Wilson 95% CI 42.3%-75.4%; P(p > 0.5) = 0.859 under a uniform prior
   python3 tools/philosophy/edge_lab.py kelly --p 0.45 --rr 2 --cost 0.05 --wins 45 --n 100 --quantile 0.05
   #   plug-in Kelly 0.1465; conservative (5% quantile) 0.0305; half of that 0.0153
   ```

**Data needed.** None for S11. For J1 and J4: at least 100 closed take rows with frozen
estimates, and 30 per probability bin before that bin is read.

**Decided in advance.**

- *Success.*
  - J1: mean(`est_ev_r` − `result_r`) within ±2 SE of zero over 100 or more trades, and no more
    than one bin of 30 or more trades outside its Wilson interval.
  - S11: no more than 10% of runs flagged at 40 trades (no more than 2% "inconsistent"), and at
    least 50% detection of a fall in win rate from 55% to 40%.
  - J4: a hindsight shift whose interval includes zero with an upper bound below 3 points.
- *Failure.*
  - J1 optimistic: replace each setup card's `est_win_prob` with the 5% posterior quantile until
    calibration recovers. This is the conservative input that `kelly_under_uncertainty` already
    uses.
  - S11 over-alarms: pre-register a multiplicity-adjusted "unusual" rule, then rerun.
  - J4 shows a shift: keep the frozen-record rule (it is the remedy), and add the recall exercise
    to the monthly review.

**Reading.**

- [[mathbook_all_of_statistics]]: confidence intervals, the bootstrap and testing, in one place.
- [[mathbook_casella_berger]]: the theory of estimators and of how uncertain they are.
- [[mathbook_blitzstein_intro_probability]]: conditional probability and the binomial at the
  level this program needs.
- [[mathbook_jaynes_probability_logic]]: probability as updating beliefs on evidence, the logic
  behind the Beta posterior.
- [[mathbook_feller_probability]]: runs and streaks, the mathematics of a losing run.
- [[mathbook_statistical_consequences_fat_tails]]: why fat tails make sample averages converge
  more slowly.
- [[book_fooled_by_randomness]]: the same problem told through traders' careers.
- [[book_thinking_in_bets]]: judging a decision by its quality rather than its result.

---

## Question 4 — [[question_survives_costs]]

*Does the advantage survive trading costs?*

**What the lab already answered.** Not yet, in the sense the question intends.

- S7's best in-sample cell could have absorbed 35.8 bp per side in-sample, far more than the 1–10
  bp tested. Out of sample it had no gross edge left, so costs only deepened a loss that the
  change of period had already produced (H9, qualified).
- The lab's costs were flat assumptions, applied to index levels that cannot be traded directly.

**Hypotheses.** H9, H19.

**Next studies.**

1. **S14.** Apply S7's cost grid to an edge that is still positive out of sample before costs.
   Candidates: the S5 winner re-run on `ES=F` and `NQ=F`, or the 12-week setup's backtest. Use
   roll-aware returns and two pre-set cost levels.
2. **J7** (journal). Cost drift: mean `cost_r` against mean `est_cost_r` each month, using the
   journal review's cost-drift line.
3. **Every setup card.** Express cost in R for the planned stop. The same price cost weighs more
   on a tight stop (Gate 5.6).

```bash
python3 tools/philosophy/edge_lab.py breakeven --rr 2 --cost 0.05     # 35.00% break-even at 2:1 and 0.05R
python3 tools/philosophy/edge_lab.py ev --p 0.6 --win 100 --loss 120 --cost 5   # the owner's +$7 example
python3 tools/philosophy/journal_review.py JOURNAL.csv --out PRIVATE.md
```

**Data needed.**

- Continuous futures series (`ES=F`, `NQ=F`) with the roll dates identified.
- Measured fills from the journal (`cost_r`, slippage noted in `lesson`).
- Spread and commission data are not in the cache. Until they are, record the cost assumption on
  each setup card and test it against the journal.

**Decided in advance.**

- *Success.* Out-of-sample net expectancy at the pre-set realistic cost has mean − 1 SE > 0, and
  the break-even cost is at least twice that realistic cost, as a margin for error. In the
  journal: mean `cost_r` at or below `est_cost_r` plus 1 SE, and mean net `result_r` − 2 SE > 0.
- *Failure.* A break-even cost below the realistic cost means the edge cannot be traded at that
  horizon. Retire it, or move to a longer holding period, which counts as a new setup version. If
  measured costs run more than 1 SE above estimate for two months in a row, raise `est_cost_r`
  and re-score Gate 5.

**Reading.**

- [[book_trading_and_exchanges]]: where spreads, impact and slippage come from.
- [[mathbook_hasbrouck_empirical_microstructure]]: how to measure trading costs from data.
- [[paper_madhavan_2000]]: the survey of microstructure that Section XX itself names.
- [[paper_almgren_chriss_2000]]: the trade-off between market impact and timing risk when
  executing.
- [[mathbook_kissell_optimal_trading]]: transaction-cost analysis in practice.
- [[mathbook_johnson_algorithmic_dma]]: order types and execution algorithms.
- [[mathbook_bouchaud_trades_quotes_prices]]: how price impact scales with size.
- [[paper_barber_odean_2000]]: evidence that the most active individual investors earned lower
  net returns.

---

## Question 5 — [[question_survives_regime_change]]

*Does the strategy survive changing market conditions?*

**What the lab already answered.** Across one split, relationships found in the earlier period
mostly did not carry into the later one at their earlier strength.

- 1 of 11 found cells held out of sample, and even the unconditional baselines of `^GSPC` and
  `^NDX` moved beyond noise (S2, H6).
- The S5 winner's advantage over holding fell to zero (0.18 to −0.01 Sharpe), and the S7 cell's
  point estimate turned negative (+72 to −25 bp per trade before costs, with a wide out-of-sample
  interval) (H10).

Two periods are a thin test. Persistence has to be measured as a distribution, not inferred from
a single split.

**Hypotheses.** H6, H10, H20.

**Next studies.**

1. **S10.** Rolling selection and evaluation. Report, for each candidate, the share of windows in
   which it kept its sign and the median share of its in-sample excess that it kept.
2. **S11.** Know how often the live check will raise false alarms before relying on it (see
   Question 3).
3. **J5** (journal). Each month, compare `result_r` by `regime_tag` and by month, and run the
   consistency check per setup. Both are built into `journal_review.py`, whose `--window` sets
   the number of recent trades compared.

```bash
python3 tools/philosophy/journal_review.py JOURNAL.csv --out PRIVATE.md --window 20 --min-ref 30
```

**Data needed.** Cached daily bars for S10. For J5, the journal, with enough months to compare
regimes, and a setup reference record of at least 30 trades from out-of-sample or forward data.

**Decided in advance.**

- *Success.* In S10, a candidate keeps its sign in at least 70% of windows and keeps at least
  half of its in-sample excess in the median window.
- *Failure.* A median kept share at or below zero confirms H10 for that candidate, and it is
  retired.
- *In the journal.* An "inconsistent" verdict means half risk and a review (protocol 8.3). Two
  monthly reviews in a row that end "inconsistent" mean `retire:`, by the journal's update
  ladder.

**Reading.**

- [[paper_lo_adaptive_markets_2004]] and [[book_adaptive_markets]]: market efficiency as
  something that varies over time and between environments.
- [[paper_mclean_pontiff_2016]]: how return predictors decay once they are known.
- [[paper_bailey_pbo_2017]]: measuring how likely a backtest is to be overfit.
- [[paper_deflated_sharpe_2014]]: correcting a Sharpe ratio for selection and non-normality.
- [[mathbook_ml_asset_managers]]: how to design out-of-sample tests.
- [[mathbook_hamilton_time_series]]: models in which the regime itself changes.
- [[book_mastering_market_cycle]]: a practitioner's account of how conditions rotate.
- [[book_expected_returns]]: long-run evidence on which premia persisted, and when they did not.

---

## Question 6 — [[question_consistent_execution]]

*Can the trader execute the strategy consistently?*

**What the lab already answered.** Nothing about this trader. Only the journal can answer this
question. The lab did establish two facts the answer depends on.

- Excessive size alone can ruin a positive-expectancy edge: a 50% drawdown in 1 of 10,000 paths
  at 1% risk, against 9,997 of 10,000 at 10% (S4, H12).
- Short-run P&L is too noisy to grade execution by (S6, H13). Consistency has to be judged on
  process fields such as `executed_per_plan`, `exit_reason` and the gate scores, not on results.

**Hypotheses.** H12, H14, H15, H16, H17, H18.

**Next studies** (journal, live and forward rows, at least three months):

1. **J2.** Decision quality against results, using the four cells (H14).
2. **J3.** Counterfactuals of skipped candidates against takes (H15). S13 is its daily-data proxy.
3. **J5.** Decisions after a loss, and by emotion colour, against the rest (H17).
4. **J6.** Discretionary against rule-based exits, and the disposition pattern (H18).
5. **J4.** Weekly recall of past decisions (H16).

```bash
python3 tools/philosophy/journal_review.py JOURNAL.csv --out PRIVATE.md
python3 tools/philosophy/edge_lab.py streak --p-loss 0.55 --streak 8 --trades 100
#   hypothetical: P(at least one run of 8+ losses in 100 trades at a 45% win rate) = 0.3068
```

**Data needed.** The journal's 39 columns, filled as the template requires, including skips and
waits. Paper rows test the protocol's mechanics but carry little emotional load, so J5 counts live
rows only.

**Decided in advance.** These thresholds are this program's choices, set now.

- *Success.* `executed_per_plan` = `y` on at least 90% of positions. No takes with failing
  scores in a month. Plan adherence after a loss within 5 points of the overall rate. Over a
  large sample, positions graded good decisions earn more than those graded poor (H14).
- *Failure.* Adherence below 80% for two months means the method cannot be executed as written
  by this trader. Simplify the plan, or trade less often, before any further judgement of the
  edge. A worse result after losses means the post-loss pause gets longer, and the effect is
  measured again.

**Reading.**

- [[paper_kahneman_tversky_1979]]: prospect theory, Section XX's starting point; losses weigh
  more than gains.
- [[paper_shefrin_statman_1985]]: the disposition to sell winners early and hold losers.
- [[paper_barber_odean_2000]]: overtrading and what it costs individual investors.
- [[book_thinking_fast_slow]]: heuristics, overconfidence and hindsight.
- [[book_trading_in_the_zone]]: accepting risk before the trade, and thinking in probabilities.
- [[book_mental_game_of_trading]]: tilt, fear and greed treated as problems to fix.
- [[book_daily_trading_coach]]: self-coaching built on the journal.
- [[book_psychology_of_trading_steenbarger]]: how a trader's state affects decisions.
- [[book_hour_between_dog_wolf]]: the physiology of risk-taking under stress.
- [[book_best_loser_wins]]: training the behaviour of losing well.

---

## The 12-week plan: from the philosophy to one tested, journaled method

**The goal.** By week 12, have one setup that:

- is defined by written rules;
- has been tested on history with a pre-registered split and costs;
- has been run forward under the decision protocol, with every decision journaled;
- has been reviewed against its own hypotheses.

**What the goal is not.** It is not proof of an edge. Section VI's arithmetic sets the limit. A
setup with an average 0.3R edge and an sd of 1.5R needs about 96 trades before its interval
excludes zero even on an average sample (`edge_lab.py sample --p 0.45 --rr 2 --cost 0.05`).
Twelve weeks will rarely deliver that many forward trades. The plan builds the instrument and
produces the first honest reading. Ending at week 12 with "not yet shown", or "retire", is a
successful outcome of the method.

**Choosing the setup.** Pick one candidate. Write it from the philosophy:

- a hypothesis about a relationship (Gate 1);
- the level at which it applies, and its invalidation (Gate 2, A → C → B);
- conditions that can be measured (Gate 3).

The 47 practitioner playbooks in `01_chart-fanatics/strategies/` are a source of candidates. Their
own claims are T2 at best ([[framework_source_tiers]]), so none is evidence. Choose the instrument
and timeframe so that the backtest shows at least 30 candidate decisions (takes plus skips)
expected between weeks 5 and 11. If it shows fewer, change the timeframe now, not later.

| Week | Stage | Work | Commands | Deliverable | Gate to the next stage |
|---|---|---|---|---|---|
| 1 | Instruments | Run the test suite. Add S11 to `studies.py` with its own pre-registered `PARAMS` entry (the snippet under Question 3 is its core), then regenerate the lab, to learn the consistency check's false-alarm rate before relying on it. Create the working journal from `journal-template.csv`. Write the trading-plan limits of Gate 6.3. | `python3 -m pytest -q tools/philosophy/tests`; `python3 tools/philosophy/studies.py` | Journal file; plan limits; S11 in `evidence-lab.md` | Tests pass; H20's status updated from the regenerated lab under the status rules |
| 2 | Setup card v1 | Write the setup card: observation, interpretation, hypothesis, invalidation, conditions, target and exit rules, all mechanical. Pre-register its backtest in a `PARAMS` block: at most 3 variants, two cost levels, the 2012/2013 split, and the refuting observation. | `edge_lab.py breakeven` and `sample` for the planned payoff | Setup card v1; pre-registration | Two independent codings of the rules give identical signals on a test month |
| 3 | In-sample test | Backtest the variants on in-sample data only. Pick one variant by the pre-registered rule, then compute its deflated Sharpe ratio across the variants tried. Check the signal frequency against the 30-decision target. | A backtest script for the card (to be written), built on `edge_lab` (`expectancy_from_results`, `conditional_stats`, `deflated_sharpe_ratio`) | In-sample report | In-sample mean R − 1 SE > 0 after costs; otherwise revise the card (v2) or drop it |
| 4 | Out-of-sample test | Run the chosen variant once on 2013–2026, with costs, regime splits, streak and drawdown statistics. Run S8 if the card's invalidation relies on structure (it informs Gate 2). | `edge_lab.py ruin` with the out-of-sample p and payoff; `wilson` on the out-of-sample record | Out-of-sample report; setup card estimates (`est_*`) taken from the out-of-sample record, never the in-sample one | Mean R − 1 SE > 0 out of sample after costs (Gate 5.4) to continue at full program pace; otherwise forward-test as a research card only, or retire |
| 5–7 | Forward test | Every candidate goes through Gates 0–8, and every decision (take, skip, wait) gets a journal row with frozen pre-trade fields. Paper only. Session reviews; weekly `journal_review.py`; weekly recall exercise (J4). Allowed: `observe:` and `propose:`. Not allowed: rule changes. | `journal_review.py JOURNAL.csv --out PRIVATE.md` | Forward journal; weekly reviews | Hygiene checks pass (EV formula, no impulse takes, skips without positions) |
| 8 | Monthly review 1 | Per setup and regime: realised statistics, mean − 1 SE and − 2 SE, calibration (J1), costs (J7), decision-quality cells (J2), adherence and emotion bands (J5, J6), the six open questions. Decide the pending `propose:` entries. Start S10 and S9 in parallel (research only, not the card). | `journal_review.py`; `edge_lab.py sample` with the updated estimates | Monthly review; updated card estimates | Adherence of at least 90%; no hygiene failures; any `revise:` creates v2, and its sample restarts from zero |
| 9–11 | Forward test continues | As weeks 5–7. If the owner chooses to trade live, Gate 6.2 sets the size from the evidence: no live trade unless mean R − 1 SE > 0 on out-of-sample and forward records, half risk between 1 and 2 SE. Live rows go in their own file. Live trading is not one of this plan's success criteria. | As weeks 5–7; `consistency_check` through the review's consistency section | Forward (and any live) journal | No limit breaches; any "inconsistent" verdict handled by protocol 8.3 |
| 12 | Final review | Monthly review 2. Pool out-of-sample and forward evidence (kept apart from live), compute the conservative estimates, and decide: continue, revise (v2 with a fresh sample), or retire. Update `hypotheses.yaml` only where a hypothesis met its stated sample; most journal hypotheses (H14–H18) will still read "untested", and that should be said plainly. Write a one-page method record: rules, out-of-sample result, forward record, calibration, adherence, open questions. | `journal_review.py`; `edge_lab.py wilson`, `sample`, `kelly --wins --n` | The tested, journaled method record; registry updates; next quarter's studies | The record states what the evidence supports, what it does not, and how many more trades each open claim needs |

**Stop rules that hold throughout.**

- A Gate 6.3 limit is never loosened mid-week.
- A drawdown of 10% from peak halves the base risk; 20% returns everything to paper. These are the
  protocol's example defaults, and they apply only if live trading was chosen.
- One trade never changes the setup card.
- If the forward record and the out-of-sample record disagree by more than 2 SE, the card goes on
  hold and the difference is investigated (Section X), not explained away.

## What this program does not promise

It does not promise a profitable strategy. The philosophy itself refuses that promise in Section
XIX, and Section XVII says the scientific approach guarantees only a disciplined way of deciding
whether beliefs deserve confidence. The success of the program is measured by whether each open
question gets an answer that can be checked, including the answer "no".
