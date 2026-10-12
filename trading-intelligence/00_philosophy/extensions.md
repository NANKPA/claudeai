---
id: synthesis_philosophy_extensions
type: synthesis
title: "Beyond the Philosophy — what the knowledge base adds, sharpens and challenges"
partition: 00_philosophy
layer: L0
related: [philosophy_relationship, synthesis_blueprint_map, synthesis_philosophy_hypotheses]
status: synthesized
---

# Beyond the Philosophy

> **Education, not financial advice. Not a trading signal.** No number on this page is the win
> rate or P&L of a real account, trader or strategy. Playbook rules are paraphrased from
> first-party Chart Fanatics pages (T2); any performance figure from them is self-reported (T4).
> Worked numbers marked *illustrative* are arithmetic on hypothetical inputs.

The owner asked the knowledge base to show "more than I can even know or tell". This page
collects what the rest of the knowledge base knows that [[philosophy_relationship]] does not yet
say. That includes the ideas that push against it. The philosophy text is unchanged. Every
amendment below is a suggestion written in the owner's voice, for the owner to accept, reword or
reject.

**How the list was built.** Mapping agents read the philosophy and the partitions and proposed 24
candidates. Each one was checked against the concept notes, playbooks, book entries and formulas
it cites. Near-duplicates were merged: three Kelly candidates became one, and so did the pairs on
Monte Carlo bands, edge decay, counting trials, fat tails, emotion, and reflexivity/invalidation.
Two areas the candidates missed were added as their own entries: base rates and calibration, and
costs and market impact. Adverse selection, the correlation of trades, variance drag, the time
average versus the ensemble average, over-watching, and the role of position management were
folded into the entries where they belong. The result is 18 entries.

**Key.**
- **EXTENDS**: the knowledge base covers ground the philosophy does not.
- **SHARPENS**: it makes one of the philosophy's claims more precise, measurable or testable.
- **CHALLENGES**: it offers evidence or an argument against a claim as the philosophy states it.

Section and principle links follow [[synthesis_blueprint_map]]. Several of the claims below are
already set up as falsifiable hypotheses in [[synthesis_philosophy_hypotheses]].

## At a glance

| # | Extension | Relation | Touches most |
|---|---|---|---|
| 1 | [Name the counterparty](#1-name-the-counterparty) | SHARPENS | VIII, I, P1 |
| 2 | [Shared models are part of the market, and stops are one of them](#2-shared-models-are-part-of-the-market-and-stops-are-one-of-them) | CHALLENGES | II, I, X, P3, P7 |
| 3 | [Observed interaction: a rung between price and inference](#3-observed-interaction-a-rung-between-price-and-inference) | EXTENDS | IV, I, P1 |
| 4 | [Value is what the auction accepts](#4-value-is-what-the-auction-accepts) | SHARPENS | XV, IV |
| 5 | [Every edge is perishable](#5-every-edge-is-perishable) | EXTENDS | V, VI, XXI, Q1, Q5 |
| 6 | [Fat tails slow the law of large numbers](#6-fat-tails-slow-the-law-of-large-numbers) | CHALLENGES | VI, VII, P3, P9, Q3 |
| 7 | [Count every trial, then deflate the winner](#7-count-every-trial-then-deflate-the-winner) | SHARPENS | VI, XVII, XX, P4, Q1, Q3 |
| 8 | [Start from a sceptical base rate, then score your calibration](#8-start-from-a-sceptical-base-rate-then-score-your-calibration) | SHARPENS | VI, XVI, P4, Q3 |
| 9 | [A ready vocabulary of measurable conditions](#9-a-ready-vocabulary-of-measurable-conditions) | EXTENDS | V, P2, P4, Q2 |
| 10 | [Edges that need no story](#10-edges-that-need-no-story) | CHALLENGES | III, VIII, P1 |
| 11 | [Costs are set by the relationship, not a constant](#11-costs-are-set-by-the-relationship-not-a-constant) | SHARPENS | VII, VIII, P5, Q4 |
| 12 | [Expected value is not growth: size is part of the edge](#12-expected-value-is-not-growth-size-is-part-of-the-edge) | SHARPENS | VII, XIV, P5, P9 |
| 13 | [Graded conviction instead of trade / no trade](#13-graded-conviction-instead-of-trade--no-trade) | EXTENDS | VIII, XIV, P6, P9 |
| 14 | [Correlation: of positions, of strategies, of trades](#14-correlation-of-positions-of-strategies-of-trades) | EXTENDS | XIV, VI, P9 |
| 15 | [Record the trade's path, not only its verdict](#15-record-the-trades-path-not-only-its-verdict) | EXTENDS | XVI, VII, P5, P11 |
| 16 | [Expected-range bands: normal variance or a broken edge](#16-expected-range-bands-normal-variance-or-a-broken-edge) | EXTENDS | X, XI, XVII, P7, P8, Q5 |
| 17 | [Emotion is a state to measure, with structural stops](#17-emotion-is-a-state-to-measure-with-structural-stops) | CHALLENGES | XII, IX, P10, Q6 |
| 18 | [Stepping back has a cost: define it in advance and log it](#18-stepping-back-has-a-cost-define-it-in-advance-and-log-it) | CHALLENGES | IX, P6, Q6 |

---

## A. The market and the relationship (Sections I, II, IV, XV)

### 1. Name the counterparty

**Relation:** SHARPENS · **Touches:** [[philo_source_of_opportunity]] (VIII), [[philo_market_is_relationship]] (I), [[principle_01_understand_before_acting]]

**The idea.** Section VIII asks for "a defensible explanation" but never says what makes an
explanation defensible. The knowledge base offers one test: say who is on the other side of the
trade, and why they are willing to be there. Section I already notes that people trade for
different reasons. Some have a view, some are hedging, and some simply need to transact now. The
edge note turns that into a checklist of causes: forced liquidation, hedging flow, clustered stops,
a behavioural bias, a risk premium, or a lag in information. If a counterparty and its motive can
be named, the understanding leg of Section VIII can be checked rather than just believed.

The test also has a darker side. Microstructure theory says that market makers widen the spread
to protect themselves from better-informed traders. A resting limit order fills most reliably on
exactly the trades that keep running through it. Harris stresses the zero-sum nature of short-term
trading once costs are counted. So if no one can be named who willingly pays the trader, the sensible
default is that the trader may be the one paying, either for someone else's information or for
immediacy. Naming the cause brings a further benefit, as Matteo Conti's framework notes: the trader
can tell when the cause has stopped operating.

**Where the knowledge base carries it**
- [[concept_edge]]: an edge is made of a cause (someone is on the other side for a structural reason), a detector, an execution path and a survival layer.
- [[synthesis_unified_framework]]: layer L0 opens with the question of who is on the other side, and why.
- [[book_trading_and_exchanges]]: who trades and why (informed, liquidity-providing, utilitarian and parasitic traders), the adverse-selection part of the spread, and the zero-sum nature of short-term trading once costs are counted.
- [[concept_market_microstructure]], [[mathbook_ohara_microstructure_theory]]: Glosten-Milgrom (the spread pays for adverse selection) and Kyle (informed flow hides in noise).
- [[concept_trade_execution]]: anticipatory limit orders at a zone suffer adverse selection.
- [[strategy_matteo_conti_institutional]]: every model is tied to a cause, such as early-session order imbalance or institutional VWAP execution, and knowing the cause shows when it stops applying.

**Suggested amendment** *(for the owner to accept, reword or reject)*
> "Before I call an explanation defensible, I will name who is likely to be on the other side of
> my trade and why they are willing to be there. If I cannot, I will assume that I may be the one
> paying for someone else's information or urgency."

### 2. Shared models are part of the market, and stops are one of them

**Relation:** CHALLENGES · **Touches:** [[philo_market_system_of_rules]] (II), [[philo_market_is_relationship]] (I), [[philo_evidence_changes]] (X), [[principle_03_future_is_uncertain]], [[principle_07_respond_methodically]]

**The idea.** Section II says that "the market exists independently of my understanding of it."
For one small trader's private model, that holds, and it is a sound rule of humility. Soros, building
on Popper's fallibilism, argues something stronger about the crowd. Participants' biased
perceptions change the fundamentals they are trying to price, and the changed fundamentals then
feed back into perception. That loop produces boom and bust.

The knowledge base shows the same loop at the scale of a single session. Models that many traders
share become orders. Stops pile up beyond obvious swing highs and lows, equal highs and lows,
session extremes and round numbers. Stops are dormant market orders, so a triggered cluster
cascades. Crowded positioning is future supply or demand. The model the crowd uses is therefore
part of the system the philosophy studies.

The knowledge base is careful on one point. Nobody hunts an individual retail stop. Stops matter
as liquidity in aggregate, and Andrea Cimitan calls stop runs liquidity events rather than
deliberate hunting.

This matters most for Section X. A predefined invalidation placed at the most obvious level sits
where everyone else's invalidation sits. Price can run it on the way to B, which is an A → C → B
detour produced by order flow. Sweep-reversal playbooks respond in a consistent way. They wait for
the failure to be confirmed, put the stop beyond the sweep extreme, and cut size rather than
tighten the stop when the dollar risk is too large. The knowledge base has no data on how often
structural stops are swept before the target is reached, so this remains a hypothesis to measure.

**Where the knowledge base carries it**
- [[concept_reflexivity]], [[book_alchemy_of_finance]], [[media_soros_ceu_lectures]], [[person_karl_popper]]: perceptions change fundamentals; fallibilism as method.
- [[concept_liquidity]]: where stops cluster, why a large participant needs them to fill, and the warning that a pool can be a target rather than a reversal point.
- [[concept_market_sentiment]]: positioning creates fuel; crowded longs are future sellers.
- [[concept_liquidity_sweep_reversal]], [[strategy_candace_lau_nq_sweep_reversal]], [[strategy_dhesi_liquidity_inversion]]: wait for the failure to be confirmed; stop beyond the sweep extreme; change size, not the stop.
- [[strategy_andrea_cimitan_amt]], [[synthesis_consensus_conflicts]]: stop runs are liquidity events; the "smart money is hunting your stop" claim does not survive scrutiny.

**Suggested amendment**
> "My private model does not move the market, but models that many traders share do. Where the
> crowd places its stops and how it is positioned are part of the system I study. Before I set my
> invalidation, I will ask where everyone else's sits, and I will put mine where my hypothesis is
> wrong, not where the obvious level is."

### 3. Observed interaction: a rung between price and inference

**Relation:** EXTENDS · **Touches:** [[philo_price_expression]] (IV), [[philo_market_is_relationship]] (I), [[principle_01_understand_before_acting]]

**The idea.** Section IV's ladder runs from observation ("price has risen substantially") straight
to interpretation ("buying pressure may be increasing"). In markets with a central order book and
real volume, the knowledge base supplies quantities that observe the interaction itself rather than
only its result:

- which side was aggressive (time and sales, footprint);
- net aggression (delta, cumulative delta);
- whether aggression moved price or was absorbed, which is Wyckoff's "effort versus result";
- price impact per unit of order flow (Kyle's lambda).

Andrea Cimitan and Carmine Rosato both reduce the read to one question: when one side pushes, does
price follow (acceptance) or stall (absorption)? Their view is that urgency moves price, not a
larger number of buyers.

This adds a rung, *observed interaction*, between observation and interpretation. It makes some
interpretations testable. "Buyers were aggressive and price did not rise" is a record, not a guess.
It does not reveal intent. Section IV's caution stands: the trader still sees what happened, not
why.

**Limits.** These reads work on centralised futures, not on spot FX, which has no consolidated
volume. The knowledge base holds no tick or order-book data, so none of these reads has been
tested here.

**Where the knowledge base carries it**
- [[concept_order_flow]]: instruments (tape, DOM, footprint, delta, CVD) and core reads (absorption, exhaustion, trapped traders).
- [[concept_wyckoff_method]]: effort versus result is the ancestor of absorption.
- [[paper_kyle_1985]], [[concept_market_microstructure]]: price impact per unit of net order flow.
- [[mathbook_bouchaud_trades_quotes_prices]], [[mathbook_hasbrouck_empirical_microstructure]]: order-book dynamics, price discovery and the information carried by trades.
- [[strategy_andrea_cimitan_amt]], [[strategy_carmine_rosato_orderflow_masterclass]]: accepted versus absorbed aggression, and reading price's response to delta rather than delta alone.

**Suggested amendment**
> "Where the market reports who traded aggressively and whether price responded, I will record that
> as its own step, observed interaction, between what price did and what I infer about
> participants. Intent remains an inference."

### 4. Value is what the auction accepts

**Relation:** SHARPENS · **Touches:** [[philo_value_vs_price]] (XV), [[philo_price_expression]] (IV)

**The idea.** Section XV separates price from "my estimate of value" but never says how value is
measured. The knowledge base uses the word in three working senses and has no note that reconciles
them. Naming them gives Section XV operational content.

1. **Auction value.** This is where trade is accepted over time and volume: the value area and the
   point of control. Value can migrate. Time and volume at a new price mean acceptance; a fast
   excursion on thin volume means rejection. This separates a new value from a failed probe.
2. **Event-defined fair price.** JJ Simon anchors fair price to the event now driving the market,
   such as the session open or the price just before scheduled news. After unexpected news he lets
   the next consolidation become the new fair price. After repeated failed reversions he drops the
   old one: value has moved.
3. **Anchored or fundamental value.** Lance Breitstein scores a stretched move as more likely to
   revert when no fundamental change explains it. He treats a quantifiable anchor, such as a bond
   at maturity or cash flows, as making reversion more reliable.

Pedersen explains the persistence Section XV warns about ("the difference may persist"). Gaps
survive because closing them costs money and capital is limited: the limits to arbitrage. A gap
is therefore an opportunity only if one can say why others have not already closed it.

**Where the knowledge base carries it**
- [[concept_auction_market_theory]], [[book_mind_over_markets]], [[concept_volume_profile]]: balance and imbalance, acceptance and rejection, value area and POC.
- [[concept_vwap]]: VWAP as both an execution benchmark and a session fair value.
- [[strategy_jj_simon_fair_pricing]]: event-defined fair price, reset after news, dropped once value has moved.
- [[strategy_lance_breitstein_mean_reversion]]: no-fundamental-change scoring and value anchors.
- [[book_efficiently_inefficient]]: inefficiencies exist because of costs and limits to arbitrage.

**Suggested amendment**
> "When I speak of value, I will say which kind I mean: where the auction is accepting trade, the
> price set by the event now driving the market, or an estimate anchored in cash flows. I will treat
> a gap between price and value as tradable only after asking what stops others from closing it."

---

## B. Probability and evidence (Sections V, VI, XVII, XIX)

### 5. Every edge is perishable

**Relation:** EXTENDS · **Touches:** [[philo_recurring_storyline]] (V), [[philo_conditional_probability]] (VI), [[philo_manifesto]] (XXI), [[question_repeatable_behaviors]], [[question_survives_regime_change]]

**The idea.** Sections V, VI and XIX allow that "a relationship that worked in one period may
weaken or disappear in another." The knowledge base goes further and treats decay as the default
case. It also supplies a mechanism. Its working model of market efficiency is Lo's adaptive
markets view: efficiency varies with the mix of participants, so edges appear, attract capital,
get crowded, and decay.

Pavel's playbook gives two practical consequences. Edges in very liquid markets on very low
timeframes face the most professional competition and decay fastest. A small trader should
therefore prefer less contested markets and horizons, and research never stops. The knowledge
base also stresses selection. A strategy presented in public is the survivor of an invisible
selection process, so it may already be crowded.

The knowledge base's own pre-registered study points the same way (`evidence-lab.md`, study S2).
Of the conditional cells on daily index data that differed in-sample, only one held its difference
out of sample; most weakened, vanished or reversed. The knowledge base has no data on how fast an
edge decays after it is published, so that remains an open question rather than a finding.

The philosophy already asks for re-checking. What it lacks is a schedule for re-validation and a
rule for retiring a strategy.

**Where the knowledge base carries it**
- [[book_adaptive_markets]], [[person_andrew_lo]], [[concept_random_walk_efficient_markets]]: efficiency is ecological; edges appear, crowd and decay; assume most patterns are noise.
- [[concept_edge]]: edges decay as they are crowded; monitor them through the journal.
- [[strategy_pavel_first_principles]]: choose the playground before the setup; lower-timeframe edges decay fastest; keep researching.
- [[concept_trading_journal_review]]: a monthly or quarterly check for edge decay against backtest expectations.
- [[concept_time_series_statistics]]: structural breaks; prefer rolling or walk-forward estimates.
- [[synthesis_consensus_conflicts]]: resolves the efficient-versus-exploitable conflict with the adaptive view that edges exist, decay and need re-validating.

**Suggested amendment**
> "I will treat every edge as perishable. Each one gets a stated cause, a scheduled re-validation
> and a retirement rule, written down before I trade it. I will prefer markets and horizons where
> fewer professionals compete for the same behaviour."

### 6. Fat tails slow the law of large numbers

**Relation:** CHALLENGES · **Touches:** [[philo_conditional_probability]] (VI), [[philo_mathematics_sword]] (VII), [[principle_03_future_is_uncertain]], [[principle_09_protect_capital]], [[question_estimate_reliability]]

**The idea.** Section VI relies on the law of large numbers "under appropriate assumptions." The
fat-tail sources say those assumptions often fail in markets. Return distributions have power-law
tails, and their variance may be unstable. Under such tails, sample means and variances converge
slowly, and a historical Sharpe ratio can rest on a handful of observations. Even under the
friendliest assumption, independent trades, the knowledge base's simulation (`evidence-lab.md`,
study S3) shows how slow learning is. A genuine edge of +0.05R looked like a losing strategy in
about a third of 30-trade samples, and roughly 3,000 trades were needed before the evidence
reliably separated it from zero. Fat tails and regime changes make that harder, not easier.

Two more consequences reach Section VII's expected-value formula, which uses averages.

- **Hidden tail risk.** A high-win-rate, negatively skewed strategy can look excellent for months
  before one loss reveals its true average. The expectancy note's blow-up-prone mean reverter is
  the illustration.
- **Stops are not guarantees.** A stop becomes a market order when triggered, so gaps and fast
  markets fill it beyond the planned price. The loss that defines risk in Section XIV is a floor,
  not a ceiling.

The pre-trade checklist's minimum of 30 logged instances is therefore a reason to start looking,
not a reason to trust.

**Where the knowledge base carries it**
- [[concept_probability_fat_tails]], [[mathbook_statistical_consequences_fat_tails]]: sample statistics converge slowly; size for the tail, not the average; a win rate is a posterior belief.
- [[book_misbehavior_of_markets]], [[mathbook_mandelbrot_fractals_scaling]], [[person_benoit_mandelbrot]]: fractal, fat-tailed prices; Gaussian finance understates risk.
- [[book_black_swan]]: rare, high-impact events dominate outcomes and are underestimated.
- [[concept_performance_metrics]]: on a short sample, a very high Sharpe is more likely luck or hidden tail risk; negative skew with a high Sharpe is the short-volatility signature.
- [[concept_trade_management]], [[concept_trade_execution]]: stops slip in gaps and fast markets.
- [[synthesis_pre_trade_checklist]]: the 30-instance gate, read here as a minimum, not a proof.

**Suggested amendment**
> "I will not assume that my sample's average loss is the loss I face. For every record I will look
> at the skew and the largest losses, size for a gap through my stop rather than a clean fill, and
> widen my uncertainty whenever a few trades carry most of the result."

### 7. Count every trial, then deflate the winner

**Relation:** SHARPENS · **Touches:** [[philo_conditional_probability]] (VI), [[philo_scientific_method]] (XVII), [[philo_research_foundations]] (XX.4), [[principle_04_conditional_probability]], [[question_repeatable_behaviors]], [[question_estimate_reliability]]

**The idea.** Section XVII warns against "repeatedly adjusting its rules until they fit the past."
The knowledge base makes the warning quantitative. If N strategies with no skill are tried, the
best of them is expected to show a Sharpe ratio that grows roughly like √(2 ln N). The evidence
for any winner must therefore be discounted by the number of attempts behind it. That is what the
deflated Sharpe ratio, the probability of backtest overfitting, and the data-snooping-robust tests
in Aronson do.

Principle 4 creates a hidden tension here. The more finely the conditions are defined, the more
cells are tested. Three trend states, three volatility bands and two sessions already make 18
cells, and slicing a journal by setup, session and regime is the same multiple testing. In the
knowledge base's own study, 11 of 74 conditional cells differed in-sample where chance alone would
produce about 4, and only one of the 11 held out of sample (`evidence-lab.md`, S2). The systematic playbooks build the
discount into their method:

- generate many candidates and then try to break them;
- freeze the rules before the out-of-sample test;
- prefer few rules, because every extra condition is another way to overfit.

None of this works unless the number of trials is recorded, and the philosophy does not yet ask for
that.

**Where the knowledge base carries it**
- [[concept_overfitting_validation]], [[formula_sheet]]: the expected best Sharpe of N trials with no skill; DSR; PBO; walk-forward; parameter plateaus.
- [[paper_deflated_sharpe_2014]], [[person_marcos_lopez_de_prado]], [[book_advances_financial_ml]]: correcting the Sharpe ratio for the number of trials, skew and kurtosis.
- [[book_evidence_based_ta]], [[mathbook_all_of_statistics]]: data-snooping corrections and multiple testing.
- [[strategy_naoufel_taief_algorithmic]]: thousands of generated strategies are reduced to a few dozen by tests designed to break them.
- [[strategy_matteo_conti_institutional]]: develop in-sample, freeze, then test on unseen data.
- In this repository, `tools/philosophy/edge_lab.py` already provides `expected_max_sharpe` and `deflated_sharpe_ratio`.

**Suggested amendment**
> "I will keep a research log of every condition and variant I test, including the ones I discard.
> I will judge the best of them against what chance alone would produce from that many tries."

### 8. Start from a sceptical base rate, then score your calibration

**Relation:** SHARPENS · **Touches:** [[philo_conditional_probability]] (VI), [[philo_journal]] (XVI), [[principle_04_conditional_probability]], [[question_estimate_reliability]]

**The idea.** Section VI frames a probability estimate as a question: given these conditions, what
happened, how often, and how reliably? The knowledge base adds two disciplines that the philosophy
does not name.

The first is a prior. The knowledge base's working view is that most candidate patterns are noise,
and Aronson's tests found that most technical rules fail rigorous testing. A new pattern should
therefore start near "no edge", and the evidence must move it from there. Bayesian updating is the
formal version. A win rate is a posterior that widens or narrows with the sample, not a constant to
read off a backtest. At 50 trades and a 50% observed rate, one standard error is about 7 points, so
a 95% interval spans roughly 36% to 64%.

The second is calibration. Section XVI already asks the trader to record the probability estimate
behind each trade. Those records make a check possible that the philosophy does not yet request:
did the trades labelled about 70% win about 70% of the time? The knowledge base flags the absence
of a calibration tool (a reliability table or Brier score) as a gap. The hypotheses page sets the
check up as a test.

**Where the knowledge base carries it**
- [[concept_probabilistic_thinking]]: Bayesian updating of the edge estimate; a 30-trade win rate has a wide interval.
- [[concept_probability_fat_tails]], [[mathbook_jaynes_probability_logic]], [[person_et_jaynes]]: probability as extended logic; a win rate is a posterior belief.
- [[concept_random_walk_efficient_markets]], [[book_evidence_based_ta]]: assume most patterns are noise and demand evidence.
- [[formula_sheet]]: the standard error of an estimated win rate.
- [[book_thinking_in_bets]]: express beliefs as probabilities and judge the process, not the result.
- In this repository, `edge_lab.py` provides `wilson_interval` and `beta_posterior`.

**Suggested amendment**
> "I will start every new pattern from the assumption that it is probably noise and let the evidence
> move me. Every so often I will check whether the probabilities I wrote down came true about as
> often as I said they would."

### 9. A ready vocabulary of measurable conditions

**Relation:** EXTENDS · **Touches:** [[philo_recurring_storyline]] (V), [[principle_02_context_before_movement]], [[principle_04_conditional_probability]], [[question_define_conditions]]

**The idea.** The philosophy asks for conditions that are "measurable and consistently
identifiable" (open question 2) but names none. The knowledge base already has a working list:

- **Regime grid.** Trend versus range, crossed with low versus high volatility. The same setup can
  have opposite expectancy in different cells.
- **Auction state.** Balance versus imbalance, value migration, day type, initial balance.
- **Structure.** Clean higher highs and higher lows versus overlapping swings.
- **Statistics.** ADX, the Hurst exponent, the variance ratio, Kaufman's efficiency ratio,
  realised-volatility or ATR percentile, and formal regime-switching models.
- **Practitioner gates.** Moving-average alignment, as in TG Capital's stacked-EMA gate. Anthony
  Crudele's daily Bollinger Bands at 3 standard deviations, which sort the market into
  consolidation, expansion or mean reversion. Fabio Valentini's two models, one for out of balance
  and one for back in balance.
- **Session and time of day,** and order-flow persistence from one session to the next (Andrea
  Cimitan; T2, untested).

Two warnings come with the list. Each added detector multiplies the number of trials (entry 7).
And the knowledge base fixes no standard set or thresholds, so the owner has to choose a small set
and freeze the definitions before looking at results.

**Where the knowledge base carries it**
- [[concept_market_regimes]]: the 2×2 grid and its detectors.
- [[concept_time_series_statistics]], [[concept_volatility]], [[formula_sheet]]: Hurst, variance ratio, volatility clustering, ATR.
- [[concept_auction_market_theory]], [[book_mind_over_markets]]: balance, imbalance and day types.
- [[mathbook_hamilton_time_series]]: regime-switching models.
- [[strategy_anthony_crudele_futures_trend]]: the daily Bollinger environment sets the posture before any setup.
- [[strategy_andrea_cimitan_amt]]: order-flow autocorrelation as a bias input.

**Suggested amendment**
> "My default conditions will be a short, fixed list: trend versus range, volatility percentile,
> balance versus imbalance, and session. Each will be defined by a number before I look at
> results, so that 'similar conditions' means the same thing every time."

### 10. Edges that need no story

**Relation:** CHALLENGES · **Touches:** [[principle_01_understand_before_acting]], [[philo_source_of_opportunity]] (VIII), [[philo_acb_principle]] (III)

**The idea.** Principle 1 says: "Do not enter a trade merely because the price is moving." Trend
following does exactly that. It buys the break of an N-day high, names no destination, and leaves
when a trailing rule says so. Its returns come from a few large trends that pay for many small
losses. The knowledge base calls time-series momentum one of the best-supported anomalies,
documented across a century of futures data, with lumpy and sometimes crowded returns.

The risk-premium sources explain returns of this kind in a different way. They see them as
compensation for bearing risk, or as the result of costs and limits to arbitrage, not as a reading
of the current relationship between participants.

Seen this way, trend following goes further than Section III. It agrees that B is only a hypothesis,
and it then does without B altogether: the exit rule, not a forecast, ends the trade. That
challenges the philosophy's account of understanding. Section VIII asks for "a defensible
explanation of the circumstances I am observing." A trend follower can give a defensible
explanation of why a *class* of movement pays on average without explaining this one. Unless the
philosophy allows that second kind of understanding, it rules out one of the most tested families
of strategy in the knowledge base.

**Where the knowledge base carries it**
- [[concept_trend_following]], [[book_trend_following_covel]]: price-based entries, rule-based exits, positive skew, few large winners.
- [[concept_random_walk_efficient_markets]]: time-series momentum and trend premia as the counter-evidence to the weak-form EMH.
- [[book_expected_returns]]: momentum alongside value, carry and volatility as risk premia.
- [[book_efficiently_inefficient]]: strategies exist because of costs and limits to arbitrage.
- [[person_cliff_asness]], [[media_fwm_cliff_asness]]: value and momentum factor research, and time-series momentum.

**Suggested amendment**
> "Understanding can also mean a tested reason why a class of movement pays on average, such as a
> risk premium or slow adjustment. A rule that enters because price is moving can satisfy
> Principle 1, provided that reason and its evidence are written down."

---

## C. Mathematics, costs and size (Sections VII, VIII, XIV)

### 11. Costs are set by the relationship, not a constant

**Relation:** SHARPENS · **Touches:** [[philo_mathematics_sword]] (VII), [[philo_source_of_opportunity]] (VIII), [[principle_05_mathematical_justification]], [[question_survives_costs]]

**The idea.** Section VII subtracts trading costs as one flat figure ($5 a trade). The knowledge
base treats cost as one more expression of the relationship, so it varies with the conditions the
trader is in:

- The spread is the price of immediacy, and it widens in fast markets and around news.
- A stop becomes a market order in a book that is often thinning, which is why slippage is worst
  on the trades that hurt.
- Impact grows with size relative to volume: roughly with its square root, so doubling size raises
  impact by about 41%.
- Anticipatory limit orders save the spread but suffer adverse selection.
- Trading frequency multiplies both the edge and the costs. Measured per unit of time, expectancy
  favours small, frequent edges only until costs are counted.

Pavel uses the ratio of cost to expected move as a first test of a market. In his illustrative
example (T4), round-trip costs of about 0.2% take half of a 0.4% edge per trade but only about 13%
of a 1.5% edge. Because Harris treats short-term trading as zero-sum once costs are counted, costs
often decide the question outright. The knowledge base has no measured cost data per
instrument or session, so the owner would have to collect it, starting with the journal's
slippage field.

**Where the knowledge base carries it**
- [[concept_optimal_execution_market_impact]], [[mathbook_bouchaud_trades_quotes_prices]], [[paper_almgren_chriss_2000]]: temporary and permanent impact, the square-root law, and cost against risk in execution.
- [[concept_market_microstructure]], [[book_trading_and_exchanges]]: the spread as the cost of immediacy; transaction-cost measurement.
- [[concept_trade_execution]]: order types, stop slippage in gaps, and the costs to log.
- [[strategy_pavel_first_principles]]: expectancy against costs as a test of the playground.
- [[concept_expectancy]], [[formula_sheet]]: expectancy per unit time; cost = half the spread + commission + slippage.

**Suggested amendment**
> "I will estimate costs for the conditions I actually trade in, including fast markets, news,
> stop fills and my own size, rather than as one average figure. I will prefer edges whose expected
> move is large next to those costs."

### 12. Expected value is not growth: size is part of the edge

**Relation:** SHARPENS · **Touches:** [[philo_mathematics_sword]] (VII), [[philo_capital_preservation]] (XIV), [[principle_05_mathematical_justification]], [[principle_09_protect_capital]]

**The idea.** Section VII's expected value is an average over many trades, as if many separate
accounts each took one. A real account takes them one after another and compounds. What it earns
over time is the growth rate of capital, roughly μ − σ²/2. The σ²/2 term, known as volatility or
variance drag, depends on how much is risked. This is the difference between the ensemble average
and the time average: a positive average across many accounts does not guarantee growth along the
one path a trader actually lives.

Kelly's result makes the difference concrete. A growth-maximising bet fraction exists, and betting
more than about twice that fraction gives negative long-run growth, even with an edge. Section
XIV's asymmetry, where a 50% loss needs a 100% gain, is the same mathematics viewed from the
losing side. Sections VII and XIV are therefore two halves of one result: positive EV is necessary,
and it is enough only at a suitable size.

*Illustrative, our arithmetic.* Take Section VII's own hypothetical strategy with costs folded into
each outcome: win $95, lose $125, 60% wins, still +$7 a trade. Treat each trade as a repeated bet
and assume the estimates are exact. The growth-maximising choice is then to lose about 7% of the
account on a losing trade. At about 15%, expected long-run growth falls to zero. Above that, the
account is expected to shrink even though every trade still has +$7 expected value. Half the Kelly
fraction keeps about three-quarters of the growth.

The estimates are never exact, and Kelly over-bets whenever the edge is overstated. That is why the
knowledge base recommends a quarter to a half of Kelly and shading down further for small samples
and fat tails. One more definition matters: in a prop account, the bankroll is the trailing
drawdown limit, not the nominal account size. The knowledge base's simulation of a single +EV edge
(`evidence-lab.md`, S4) shows the stakes. At 1% risk, a 50% drawdown was close to impossible. At
10% risk, it was close to certain.

**Where the knowledge base carries it**
- [[concept_kelly_criterion_optimal_f]], [[paper_kelly_1956]], [[mathbook_kelly_capital_growth]], [[book_fortunes_formula]]: maximising expected log wealth; more than 2× Kelly gives negative growth; fractional Kelly.
- [[concept_stochastic_processes]], [[formula_sheet]]: g ≈ μ − σ²/2; f* = p − q/b; g* = SR²/2.
- [[book_mathematics_of_money_management]]: leverage drives both growth and ruin.
- [[concept_risk_of_ruin_drawdown]]: recovery arithmetic and streak damage, 1 − (1 − f)^k.
- [[concept_prop_firm_risk_rules]]: treat the drawdown limit as the bankroll.
- Further listening: the knowledge base's [[podcast_econtalk]] feed lists an episode on risk, ruin and ergodicity (show notes only).
- In this repository, `edge_lab.py` provides `kelly_fraction` and `kelly_under_uncertainty`, which sizes from a pessimistic quantile of the win-rate estimate.

**Suggested amendment**
> "A positive expected value justifies a trade only at a size where my capital is still expected to
> grow. I will choose my risk fraction from the growth rate, discounted for how uncertain my
> estimates are, and never above the point where the same edge would shrink the account."

### 13. Graded conviction instead of trade / no trade

**Relation:** EXTENDS · **Touches:** [[philo_source_of_opportunity]] (VIII), [[philo_capital_preservation]] (XIV), [[principle_06_do_not_force]], [[principle_09_protect_capital]]

**The idea.** Section VIII treats an opportunity as present when its three elements agree and
absent when they do not. Several sources instead size the position by how strong the evidence is.

- **Jeff Holden (SMB)** allocates the daily stop by grade: up to 80% for A+, 30% for A, 15% for B,
  5% for C. He calls a C trade with A+ risk "hope with leverage."
- **Candace Lau and Lance Breitstein** size by the number and quality of confluences. Breitstein
  trades a single-candle panic entry at smaller size because its risk is less well defined.
- **Naoufel Taief** may raise exposure when independent strategies built on different logic point
  the same way.
- **Meta-labeling** makes this systematic: a secondary model sizes a discretionary signal by its
  estimated probability of success.
- **Kelly** gives the theory: bet size should rise with edge.

Together these would turn Principles 5, 6 and 9 from yes-or-no rules into graded ones. Unclear
evidence still means no trade. Partial agreement could mean a small trade.

There is a catch. The playbooks that grade trades leave the grading criteria unspecified. Jared
Tendler lists promoting average setups to A+ as one of the warning signs of tilt. A grade is only
as good as its written criteria and its track record.

**Where the knowledge base carries it**
- [[strategy_jeff_holden_momentum_model]]: grade the trade before sizing it.
- [[strategy_candace_lau_nq_sweep_reversal]], [[strategy_lance_breitstein_mean_reversion]]: size scaled to setup quality.
- [[strategy_naoufel_taief_algorithmic]]: ensemble agreement as a reason to scale.
- [[concept_machine_learning_finance]], [[concept_position_sizing]]: meta-labeled sizing in proportion to estimated probability.
- [[concept_kelly_criterion_optimal_f]]: bet size proportional to edge.
- [[strategy_jared_tendler_psychology]]: inflated grades as a warning sign.

**Suggested amendment**
> "When understanding, evidence and mathematics agree only partly, I may act at reduced size rather
> than choose between all or nothing. The grade must come from criteria I wrote before entry, and
> my journal must show that higher grades really did perform better."

### 14. Correlation: of positions, of strategies, of trades

**Relation:** EXTENDS · **Touches:** [[philo_capital_preservation]] (XIV), [[philo_conditional_probability]] (VI), [[principle_09_protect_capital]]

**The idea.** The philosophy reasons about one strategy's sequence of trades. The knowledge base
adds three layers of correlation.

- **Positions.** Five correlated positions at 1% each are one 5% bet. Diversification bottoms out
  at the average correlation, not at the number of positions. In a crisis, correlations move
  toward one, which is LTCM's lesson about leverage, correlation and liquidity. The Turtles capped
  units per market, per correlated group and per direction. The knowledge base suggests a cap on
  total open risk, or "portfolio heat."
- **Strategies.** Matteo Conti suggests three or four uncorrelated strategies for a retail trader,
  such as momentum alongside mean reversion. Pavel combines less-correlated edges and rebalances
  between them. Dalio argues that many uncorrelated return streams reduce risk far more than they
  reduce return. Grinold and Kahn's "breadth" counts independent bets, not trades.
- **Trades.** The law of large numbers in Section VI needs observations that are roughly
  independent. Volatility clusters, holding periods overlap, and losing runs bunch inside regimes.
  The effective sample is therefore smaller than the trade count, which is why the knowledge base's
  own studies use non-overlapping trades and block resampling.

**Where the knowledge base carries it**
- [[concept_correlation_portfolio_risk]], [[mathbook_markowitz_portfolio_selection]]: portfolio variance, correlation limits, portfolio heat, stress correlations.
- [[concept_position_sizing]]: correlated positions add up to one bet.
- [[mathbook_grinold_kahn_active_pm]]: information ratio ≈ skill × √breadth.
- [[person_ray_dalio]], [[strategy_matteo_conti_institutional]], [[strategy_pavel_first_principles]]: portfolios of uncorrelated strategies.
- [[book_when_genius_failed]], [[book_way_of_the_turtle]]: correlation and liquidity overwhelming models; limits per correlated group.
- [[concept_time_series_statistics]]: volatility clustering (autocorrelated squared returns).

**Suggested amendment**
> "I will measure risk across everything I hold, not trade by trade. I will cap my total open risk
> and treat correlated positions as one bet. When I count observations, I will count independent
> ones, not overlapping or clustered trades."

---

## D. Process, review and the trader (Sections IX to XII, XVI)

### 15. Record the trade's path, not only its verdict

**Relation:** EXTENDS · **Touches:** [[philo_journal]] (XVI), [[philo_mathematics_sword]] (VII), [[principle_05_mathematical_justification]], [[principle_11_record_and_investigate]]

**The idea.** Section VII asks for "the complete distribution of its outcomes," as if the average
win and average loss belonged to the setup. The knowledge base shows that they are largely
produced by management rules.

- Moving the stop to breakeven early turns losers into scratches, but it also cuts winners that
  retest.
- Scaling out smooths equity but lowers the average R. Pyramiding concentrates size in the trades
  that are already working.
- A time stop adds a third way for a trade to end. Triple-barrier labelling defines each outcome by
  which barrier is hit first.
- Planned R:R is a hypothesis. Realised R depends on how often the target comes before the stop.
- Even the meaning of "a win" varies. Dhesi counts a runner stopped at breakeven as a successful
  trade, so win rates from different sources are often not comparable.

The unit to test is therefore setup plus management. Candace Lau's playbook makes this explicit:
choose the profit-taking method in advance, then test which one works. The journal needs each
trade's maximum adverse and favourable excursion (MAE and MFE) to make that test possible.

Section XVI uses the journal mainly to expose contradictions. Two review habits in the knowledge
base would widen it. Steenbarger reviews what one does well as rigorously as the mistakes. Jeff
Holden works on one recurring mistake at a time, finds its root cause with the five whys, and fixes
risk mistakes before exit mistakes.

**Where the knowledge base carries it**
- [[concept_trade_management]]: breakeven, scaling, trailing and time stops, and their effect on the win/loss distribution.
- [[concept_risk_reward_r_multiples]], [[concept_trading_journal_review]]: planned versus realised R; MAE and MFE to tune stops and targets; the review cadence.
- [[concept_machine_learning_finance]]: triple-barrier labels that match how a trade actually resolves.
- [[strategy_candace_lau_nq_sweep_reversal]], [[strategy_dhesi_liquidity_inversion]]: profit-taking decided in advance; a partial plus a runner, and what counts as success.
- [[book_daily_trading_coach]], [[person_brett_steenbarger]]: build on strengths.
- [[strategy_jeff_holden_momentum_model]]: the one-mistake root-cause loop, risk mistakes first.

**Suggested amendment**
> "My journal will record how each trade travelled: its largest adverse and favourable moves and
> every management action. That way I test a setup together with the way I manage it. I will
> review what I do well as carefully as my mistakes."

### 16. Expected-range bands: normal variance or a broken edge

**Relation:** EXTENDS · **Touches:** [[philo_evidence_changes]] (X), [[philo_being_wrong]] (XI), [[philo_scientific_method]] (XVII), [[principle_07_respond_methodically]], [[principle_08_decision_quality_not_outcome]], [[question_survives_regime_change]]

**The idea.** Sections X and XI ask whether results fall "within its expected range of outcomes"
and say that a trader "needs a way to determine" this, but give no procedure. Two systematic
playbooks supply one.

1. **Build the bands.** Resample the strategy's own trade list. Shuffling the order shows how much
   drawdown and losing streaks depend on sequence. Drawing with replacement gives distributions of
   drawdown, the longest losing streak and the chance of a given loss. Naoufel Taief ranks these
   Monte Carlo drawdowns above the single backtest drawdown for setting expectations.
2. **Monitor against them.** Matteo Conti compares live results with the bands. A breach triggers a
   review; it is not automatic proof that the strategy is broken.
3. **Bench, do not delete.** When drawdown nears its expected maximum, or underperformance lasts,
   cut size sharply or move the strategy back to simulation. Keep it on file, and promote a
   replacement from an incubation pool running on new data.

JJ Simon's three-loss rule is a session-scale version: three failed reversions in a row suggest
that value has moved. Both systematic playbooks leave the key thresholds open, namely which
percentile counts as a breach and what happens after a review. Resampling single trades also
assumes they are interchangeable. If losses cluster by regime (entry 14), the bands come out too
narrow, and resampling blocks of consecutive trades is the safer variant. Lo's point (entry 5) is
the reason the bands themselves need re-estimating as the market adapts.

**Where the knowledge base carries it**
- [[strategy_matteo_conti_institutional]]: shuffle and resampling Monte Carlo; live monitoring against simulated ranges; a breach means review.
- [[strategy_naoufel_taief_algorithmic]]: Monte Carlo drawdown as the expected maximum; bench, incubate, replace.
- [[concept_risk_of_ruin_drawdown]], [[concept_backtesting]]: losing streaks are normal; estimate ruin by resampling the R-multiple distribution.
- [[strategy_jj_simon_fair_pricing]]: the three-loss rule for reversion trades.
- [[book_adaptive_markets]]: why yesterday's bands may not describe tomorrow.
- In this repository, `edge_lab.py`'s `consistency_check` already tests recent results against reference behaviour, including a bootstrap percentile for drawdown.

**Suggested amendment**
> "Before I trade a strategy live, I will write down its expected range of drawdowns and losing
> streaks, taken from resampling its own record. A breach will mean cutting size and investigating,
> not concluding that the strategy has failed. I will keep benched strategies on file rather than
> delete them."

### 17. Emotion is a state to measure, with structural stops

**Relation:** CHALLENGES · **Touches:** [[philo_protect_process]] (XII), [[philo_step_back]] (IX), [[principle_10_emotional_independence]], [[question_consistent_execution]]

**The idea.** Section XII and Principle 10 treat fear, greed, frustration and excitement as
interference to keep out of decisions. The psychology sources in the knowledge base challenge that
framing in four ways.

- **Emotion is energy, not only noise.** Tendler's inverted U aims for the middle. Too little
  emotion makes a trader flat and hesitant; too much shuts down thinking progressively.
- **It can be measured.** Warning signs fall into triggers, thoughts, physical cues and perception
  shifts, and they can be logged for a few weeks to build a map. Frustration left over from
  yesterday counts as risk carried into today, even when one feels fine. Tendler weighs the
  emotional expected value of the next trade, which is poor when one's state is poor, so a reset
  with a limit comes first, and breaking that limit ends the session.
- **It is a size signal.** Umar Ashraf reads being overwhelmed by emotion as a sign that size is
  too large.
- **It is partly physiology.** Coates links cycles of testosterone and cortisol to swings in risk
  appetite, which no resolution fully overrides.

The practical answer is structural. Check state before the session. Use behavioural stops set in
advance, such as Dhesi's two losses ending the day and prop-firm daily loss limits. Cut size when
emotion runs high. These carry the discipline that willpower alone cannot.

**Limits.** All of this is practitioner heuristics (T4). The knowledge base has no data linking
emotion tags to outcomes.

**Where the knowledge base carries it**
- [[strategy_jared_tendler_psychology]], [[book_mental_game_of_trading]]: the zone map, warning signs, carryover, emotional expected value, the reset with a hard limit.
- [[strategy_umar_ashraf_5_stage]]: if emotions take over, you are trading too big; size grows stage by stage.
- [[strategy_dhesi_liquidity_inversion]], [[concept_prop_firm_risk_rules]]: two losses end the day; daily loss limits force a stop rule.
- [[book_hour_between_dog_wolf]]: trader physiology drives risk-taking cycles.
- [[concept_trading_psychology]]: guardrails such as a mandatory break after N losses and size reduction after a drawdown.

**Suggested amendment**
> "I will treat my emotional state as an input to measure, not only a force to resist. I will check
> it before each session, cut size when emotion runs high, and follow session stop rules that I set
> while calm."

### 18. Stepping back has a cost: define it in advance and log it

**Relation:** CHALLENGES · **Touches:** [[philo_step_back]] (IX), [[principle_06_do_not_force]], [[question_consistent_execution]]

**The idea.** Section IX says "not trading is a decision," and the knowledge base agrees. It adds
that the decision has a cost, and the cost can be large.

- Curtis Faith reports that most Turtles who failed did so by not taking every signal, which
  destroyed the distribution their edge depended on. Trend payoffs come from a few outliers, so
  skipping the wrong few can erase the edge.
- The probabilistic-thinking note says that skipping valid setups after losses destroys the sample.
- Pavel argues that waiting for confirmation gives up part of the edge. The knowledge base lists
  anticipation versus confirmation as a genuine, unresolved trade-off between price and win rate,
  to be measured rather than assumed.

The knowledge base also offers a structural cure for the over-watching that Section IX warns about.
Fix the windows in advance and ignore price outside them. Marco Trades watches only the chosen
session, and no setup inside it means no trade. Candace Lau and the kill-zone playbooks trade set
hours.

The challenge to Section IX is about timing. A decision to step back made in the moment, on a
feeling that things are "unclear," works as an untested discretionary filter whose cost no one ever
sees. The knowledge base's journal has no field for trades not taken, so that cost cannot be
measured yet.

**Where the knowledge base carries it**
- [[book_way_of_the_turtle]], [[concept_trend_following]]: failed Turtles skipped signals; a few outlier trends carry the results.
- [[concept_probabilistic_thinking]]: execute every valid setup; skipping destroys the sample.
- [[strategy_pavel_first_principles]], [[concept_trade_execution]], [[synthesis_consensus_conflicts]]: the cost of confirmation, and anticipation versus confirmation as an open conflict.
- [[strategy_marco_trades_liquidity_grab]], [[concept_trading_sessions_killzones]]: fixed watching windows.
- [[concept_market_regimes]]: detectors that could make "unclear" a written condition.

**Suggested amendment**
> "I will define in advance what makes conditions unclear, and I will watch only the windows my
> method uses. I will log each valid setup I skip, with what happened afterwards, so that I know
> what stepping back costs as well as what it saves."

---

## Proposed additions to the Practical Doctrine

> **Suggestions only.** These are candidate principles drawn from the entries above, written for
> the owner to accept, reword or reject. They are not part of the philosophy unless the owner adds
> them.

- **Principle 13 (suggested): Name the other side.** Before calling an explanation defensible,
  state who is likely to be on the other side of the trade and why. If no one can be named, assume
  you may be paying for someone else's information. *(entry 1)*
- **Principle 14 (suggested): Know where the crowd's stops sit.** Shared models act on the market.
  Put invalidation where the hypothesis is wrong, not where the obvious level is, and adjust size
  rather than the stop. *(entry 2)*
- **Principle 15 (suggested): Count every attempt.** Record every condition and variant tested,
  and judge the best of them against what chance would produce from that many tries. *(entries 7, 9)*
- **Principle 16 (suggested): Start sceptical, and score your own probabilities.** Begin each new
  pattern near "no edge", update with evidence, and check that your recorded probabilities are
  calibrated. *(entry 8)*
- **Principle 17 (suggested): Treat every edge as perishable.** Give each edge a cause, a
  re-validation schedule and a retirement rule; bench rather than delete. *(entries 5, 16)*
- **Principle 18 (suggested): Know the expected range before trading live.** Write down the
  resampled bands for drawdowns and losing streaks. A breach means cut size and investigate.
  *(entry 16)*
- **Principle 19 (suggested): Size for growth and for the tail.** Choose the risk fraction from the
  growth rate, the uncertainty in the estimate and the worst plausible loss, including a gap
  through the stop, never from the average trade. *(entries 6, 12, 13)*
- **Principle 20 (suggested): Measure risk across everything held.** Cap total open risk, and treat
  correlated positions as one bet. *(entry 14)*
- **Principle 21 (suggested): Price costs as the market charges them.** Estimate costs for the
  conditions and size actually traded, not as one average. *(entry 11)*
- **Principle 22 (suggested): Test the setup together with its management.** Average win and loss
  come from the exit rules, so record each trade's path. *(entry 15)*
- **Principle 23 (suggested): Define "unclear" before the session, and count what waiting costs.**
  Watch fixed windows and log skipped setups with their outcomes. *(entry 18)*
- **Principle 24 (suggested): Let structure carry discipline.** Use state checks, session stops and
  size limits set while calm, and read emotional overload as a sign that size is too large.
  *(entry 17)*

## What this page does not do

- It does not change, soften or reinterpret the philosophy. Where the knowledge base disagrees,
  the disagreement is stated and attributed for the owner to weigh.
- It does not test anything. Test designs and current verdicts are in
  [[synthesis_philosophy_hypotheses]], `research-program.md` and `evidence-lab.md`.
- It does not claim any strategy is profitable. Practitioner rules cited here are T2 paraphrases
  with self-reported (T4) performance, and the order-flow and psychology claims are untested in
  this knowledge base.
