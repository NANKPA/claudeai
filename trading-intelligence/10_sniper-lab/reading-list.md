---
id: synthesis_sniper_reading_list
type: synthesis
title: "Reading List — precise entries, short-term systems and small accounts"
partition: 10_sniper-lab
layer: L8
aliases: [sniper reading list, scalping books, price action books, intraday books, small account books, day trading books]
tags: [books, reading-list, price-action, scalping, order-flow, systematic, validation, small-account]
as_of: 2026-10-20
related: [philosophy_relationship, framework_decision_protocol, framework_source_tiers, synthesis_sniper_entries, synthesis_small_account_venues, synthesis_sniper_backtests, synthesis_evidence_lab, formula_sheet, framework_trading_journal, principle_04_conditional_probability, principle_05_mathematical_justification, principle_06_do_not_force, principle_09_protect_capital, principle_11_record_and_investigate, philo_mathematics_sword, philo_scientific_method, philo_conditional_probability, philo_capital_preservation, concept_price_action, concept_scalping, concept_order_flow, concept_volume_profile, concept_auction_market_theory, concept_market_microstructure, concept_breakout_trading, concept_mean_reversion, concept_trend_following, concept_market_structure, concept_market_regimes, concept_support_resistance, concept_liquidity_sweep_reversal, concept_vwap, concept_trading_sessions_killzones, concept_smart_money_concepts, concept_fair_value_gap, concept_premium_discount_ote, concept_backtesting, concept_overfitting_validation, concept_performance_metrics, concept_position_sizing, concept_leverage_margin, concept_risk_of_ruin_drawdown, concept_risk_reward_r_multiples, concept_expectancy, concept_trade_management, concept_trade_execution, concept_trading_plan, concept_trading_journal_review, book_reading_price_charts_bar_by_bar, book_crabel_opening_range, book_street_smarts, book_long_term_secrets_short_term_trading, book_trading_sardines, book_mastering_the_trade, book_building_winning_algo_systems, book_quantitative_trading_chan, book_algorithmic_trading_chan, book_systematic_trading, book_trading_systems_and_methods, book_evidence_based_ta, book_definitive_guide_position_sizing, book_mathematics_of_money_management, book_markets_in_profile, book_mind_over_markets, book_trades_about_to_happen, book_trading_and_exchanges, book_market_microstructure_in_practice, book_ta_multiple_timeframes, book_day_swing_trading_currency, book_art_science_technical_analysis, book_advances_financial_ml, mathbook_bouchaud_trades_quotes_prices, mathbook_cartea_algorithmic_hft, mathbook_hasbrouck_empirical_microstructure, paper_deflated_sharpe_2014, paper_bailey_pbo_2017, paper_white_2000, paper_barber_odean_2000, person_al_brooks, person_ernest_chan, person_robert_carver, person_larry_connors, person_perry_kaufman, person_michael_huddleston, person_linda_raschke, person_toby_crabel, strategy_vincent_desiano_break_retest, strategy_gala_trades_price_action, strategy_carmine_rosato_lvn, strategy_forrest_knight_volume_profile, strategy_fabio_valentini_amt_order_flow, strategy_abraham_perez_ict_orderflow, strategy_nbb_trader_po3_ote_adr, strategy_lance_breitstein_mean_reversion, concept_kelly_criterion_optimal_f, concept_liquidity, concept_machine_learning_finance, concept_moving_averages, concept_multi_timeframe_analysis, concept_oscillators_momentum, concept_pivot_points, concept_probabilistic_thinking, concept_probability_fat_tails, concept_time_series_statistics, concept_trendlines, concept_volatility, paper_mclean_pontiff_2016, principle_03_future_is_uncertain]
status: researched
---

# Reading List — precise entries, short-term systems and small accounts

> **Education, not financial advice.** This is a list of things to read and
> test, not a list of edges. Bibliographic facts (publisher, year, chapter
> titles) are cited to the page where they were read on **2026-10-20**; source
> keys like [R4] point to the list at the end. A description of *what a book
> teaches* is Claude's paraphrase (**T5**) unless a source key follows it.
> No win rate or P&L figure here is a fact. Performance figures from authors,
> vendors or replications are labelled **T4** ([[framework_source_tiers]]).
> The machine-readable list of the new books is `10_sniper-lab/books-sniper.yaml`.

## 1. Why this list, and why it starts with validation

The sniper lab has already answered three questions, and they decide what is
worth reading next:

- **Almost nothing survives, and what does is not yet trusted.** Of 128 codified
  configurations, none on crypto is positive after costs out of sample. Three on
  forex and gold (1h/4h) pass Gate 4, but the best of all has a deflated-Sharpe
  probability of only 0.24 once the number of trials is counted
  ([[synthesis_sniper_backtests]]). So their records are provisional until forward
  trades confirm them.
- **Costs decide at short horizons.** On a regular-fee venue, 5-minute sniper
  entries are untradeable at any account size ([[synthesis_sniper_entries]]).
- **At $20 the realistic rhythm is one to three trades a day on 1-hour or
  4-hour structure**, with maker entries and every fee journaled in R
  ([[synthesis_small_account_venues]]).

So the bot does not need more entry ideas first. It needs (1) better ways to
tell a real edge from a lucky backtest, (2) stop and sizing methods that work
at a $20 minimum-order scale, and only then (3) entry logic precise enough to
code, with the conditions under which it is supposed to work. The list is
ordered that way in §9.

The philosophy ([[philosophy_relationship]]) frames all of it. An entry idea is *understanding*; it is not
yet *evidence* or *mathematics* (Section VIII). [[principle_05_mathematical_justification]]
asks for expected value after costs. [[principle_04_conditional_probability]]
asks under which regime, session and market a probability was measured
([[philo_conditional_probability]]).
[[principle_06_do_not_force]] is the selectivity that Volman and Brooks teach
bar by bar. [[principle_09_protect_capital]] governs the sizing books, and
[[principle_11_record_and_investigate]] is what Bellafiore's playbook and
Sweeney's adverse-excursion records put into practice
([[philo_mathematics_sword]], [[philo_scientific_method]]).

On the owner's wish to stop *waiting for 60%*: several of these books make
the same point the lab does. A low hit rate is fine if the payoff and costs
work. Brooks writes it as a trader's equation (§3, Trading Ranges). The
break-even line after costs is in [[formula_sheet]] and in
[[synthesis_sniper_entries]] (a 2R bracket at 0.13R cost breaks even at 37.7%).

## 2. The list at a glance

19 new books, 1 non-book course and 4 research papers (5 papers counting the
companion study). The books already in the KB that belong beside them are in §8.

| # | Title | Author | Year | Type | In KB? | Main concepts | Bot priority |
|---|---|---|---|---|---|---|---|
| 1 | *The Evaluation and Optimization of Trading Strategies* (2nd ed.) | Robert Pardo | 2008 | book | no | backtesting, overfitting | **first** |
| 2 | *Testing and Tuning Market Trading Systems* | Timothy Masters | 2018 | book | no | overfitting, permutation tests | **first** |
| 3 | *Entry and Exit Confessions of a Champion Trader* | Kevin J. Davey | 2019 | book | no | entry isolation tests | **first** |
| 4 | *Maximum Adverse Excursion* | John Sweeney | 1997 | book | no | stop placement from data | **first** |
| 5 | *Leveraged Trading* | Robert Carver | 2019 | book | no | leverage, small-account sizing, costs | **first** |
| 6 | *The Trading Game* | Ryan Jones | 1999 | book | no | fixed-ratio sizing | second |
| 7 | *Trading Price Action Trends* | Al Brooks | 2011 | book | no | price action, pullbacks | second |
| 8 | *Trading Price Action Trading Ranges* | Al Brooks | 2012 | book | no | failed breakouts, trader's equation | second |
| 9 | *Trading Price Action Reversals* | Al Brooks | 2012 | book | no | reversals, sweeps | second |
| 10 | *Understanding Price Action* | Bob Volman | 2014 | book | no | 5m price action, selectivity | second |
| 11 | *Forex Price Action Scalping* | Bob Volman | 2011 | book | no | scalping, break setups | third |
| 12 | *YTC Price Action Trader* | Lance Beggs | c.2012 | e-book course | no | multi-timeframe process | third |
| 13 | *The Logical Trader* | Mark B. Fisher | 2002 | book | no | opening range (ACD), pivots | second |
| 14 | *Short Term Trading Strategies That Work* | Larry Connors & Cesar Alvarez | 2008 | book | no | short-term mean reversion | second |
| 15 | *Machine Trading* | Ernest P. Chan | 2017 | book | no | intraday microstructure, bitcoin | second |
| 16 | *How to Day Trade for a Living* | Andrew Aziz | 2016 | book | no | stocks in play, ORB, VWAP | third |
| 17 | *The PlayBook* | Mike Bellafiore | 2013 | book | no | setup documentation, review | third |
| 18 | *Trading by the Minute* | Joe Ross | 1997 | book | no | intraday signals, stop rules | third |
| 19 | *Volume Profile: The Insider's Guide to Trading* | Trader Dale | 2018 | book | no | volume profile levels | third |
| 20 | 2022 ICT Mentorship (YouTube) | Michael J. Huddleston | 2022 | **non-book** video course | concept note only | sweeps, FVG, OTE, sessions | read as source, not evidence |
| 21 | Intraday Patterns in the Cross-Section of Stock Returns | Heston, Korajczyk, Sadka | 2010 | paper | no | time-of-day effects | second |
| 22 | Market Intraday Momentum | Gao, Han, Li, Zhou | 2018 | paper | cited in [[synthesis_sniper_entries]] | intraday momentum | second |
| 23 | A Profitable Day Trading Strategy for the U.S. Equity Market | Zarattini, Barbon, Aziz | 2024 | paper | cited in [[synthesis_sniper_entries]] | ORB, stocks in play | second |
| 24 | Day Trading for a Living? (+ Barber, Lee, Liu, Odean 2014) | Chague, De-Losso, Giovannetti | 2019 | paper | no | base rates for day traders | **first** |

## 3. Price action and precise entries

**Al Brooks, the price-action trilogy (Wiley, 2011–2012)** — `book_trading_price_action_trends`,
`book_trading_price_action_trading_ranges`, `book_trading_price_action_reversals`. New to the KB;
only his earlier [[book_reading_price_charts_bar_by_bar]] is in it ([[person_al_brooks]]).

- *What it is.* Brooks split his method into three books: trends, trading ranges
  and reversals. The publisher says he trades only 5-minute charts [R1]. The
  *Trading Ranges* volume also covers breakouts, order management and the
  mathematics of trading [R2]; *Reversals* is about spotting and trading trend
  reversals [R2].
- *Why it matters for the bot.* Brooks is the most detailed source on the
  difference between *the same pattern in two regimes*. A breakout in a trend
  and a breakout from a range are different trades with different odds (T5).
  That is exactly the regime conditioning the lab already applies
  ([[concept_market_regimes]], [[principle_04_conditional_probability]]).
  His bar counting (the second pullback attempt in a trend) and his rule that
  a reversal usually needs a trendline break and then a failed test of the
  extreme are precise enough to code on OHLCV (T5). The trader's equation
  (chance of winning × reward must exceed chance of losing × risk) is the
  same gate as [[concept_expectancy]].
- *KB concepts.* [[concept_price_action]], [[concept_trend_following]],
  [[concept_market_structure]], [[concept_breakout_trading]],
  [[concept_mean_reversion]], [[concept_liquidity_sweep_reversal]],
  [[concept_trendlines]], [[concept_risk_reward_r_multiples]].
- *Links.* The failed-breakout logic is the same mechanism as spec S1
  (sweep and reclaim) and S5 (break and retest) in [[synthesis_sniper_entries]],
  and as the playbooks [[strategy_vincent_desiano_break_retest]] and
  [[strategy_gala_trades_price_action]].
- *Caveat.* Practitioners describe the writing as dense; forum readers often
  suggest Volman first [R6][R7]. Brooks's numbers on how often things fail are
  his own estimates, not measured tests (T5).

**Bob Volman, *Understanding Price Action* (Light Tower Publishing, 2014)** — `book_understanding_price_action`, new.

- *What it is.* Six straight months of real EUR/USD 5-minute charts, with
  hundreds of annotated examples, aimed at trading from the bare chart [R3][R4].
- *Why it matters for the bot.* It is a training set for *when not to trade*.
  Volman judges whether a build-up has real pressure behind it and skips most
  setups that look similar but lack it (T5). For a bot, that is a filter, the
  piece the lab's specs are weakest on. It also gives labelled examples a
  developer can turn into test cases.
- *KB concepts.* [[concept_price_action]], [[concept_scalping]],
  [[concept_support_resistance]], [[concept_breakout_trading]],
  [[concept_market_structure]], [[concept_trade_management]].
- *Caveat.* A study of one pair on one timeframe; its transfer to crypto is a
  hypothesis.

**Bob Volman, *Forex Price Action Scalping* (Light Tower Publishing, 2011)** — `book_forex_price_action_scalping`, new.

- *What it is.* A scalping method built on a 70-tick EUR/USD chart; reviewers
  note a 30-second chart can approximate it in the liquid London and New York
  hours [R5]. Readers single it out as a strong pick for scalping [R6].
- *Why it matters for the bot.* Volman names a small set of break setups (a
  build-up of small bars near a short moving average, then a break) with a fixed
  small target and stop (T5; check the exact set and bracket in the book).
  These are among the most codeable discretionary setups in print.
- *The $20 problem.* A fixed small bracket on a tick chart is where cost in R
  explodes. [[synthesis_small_account_venues]] found 1-minute scalps not viable
  on any venue checked. Read it for the entry logic and test it only at the
  low-fee tier, or on 15-minute bars and above.
- *KB concepts.* [[concept_scalping]], [[concept_price_action]],
  [[concept_breakout_trading]], [[concept_moving_averages]],
  [[concept_trade_execution]].

**Lance Beggs, *YTC Price Action Trader* (self-published e-book course, six volumes)** — `book_ytc_price_action_trader`, new.

- *What it is.* Six PDF volumes, about 590 pages, sold by Your Trading Coach;
  a reseller describes it as aimed at experienced intraday traders (T4,
  seller page) [R8]. Forum users praise its checklists and trading-plan
  template and find it easier to read than Brooks [R7]. The original release
  year is not confirmed; the earliest dated mention found is a 2012 forum
  post [R7].
- *Why it matters for the bot.* Its structure suits code. The higher timeframe
  decides *where* to look, and the lower timeframe's swing strength decides
  *when* to enter. Setups are named by what price does at a level: test,
  breakout failure, breakout pullback, pullback (T5). That maps directly onto
  [[concept_multi_timeframe_analysis]] and the lab's level-then-trigger design.
- *KB concepts.* [[concept_price_action]], [[concept_multi_timeframe_analysis]],
  [[concept_support_resistance]], [[concept_trading_plan]],
  [[concept_trading_journal_review]].

**Joe Ross, *Trading by the Minute* (Ross Trading International, 1997)** — `book_trading_by_the_minute`, new.

- *What it is.* Ross sets out major, minor and intermediate intraday signals and
  explains both the initial stop and the stop that protects profit [R9].
- *Why it matters for the bot.* Ross is one of the older sources for explicit
  rules on stop placement and trailing in intraday trading. His wider method
  (the 1-2-3 formation and the Ross hook) is a structure-break entry that
  resembles the market-structure-shift trigger in spec S3 (T5).
- *Caveat.* Old, futures-pit era, thinly documented online. Whether this
  particular book centres on the hook is unconfirmed [R9]. Third priority.
- *KB concepts.* [[concept_price_action]], [[concept_market_structure]],
  [[concept_trade_management]].

## 4. Intraday playbooks

**Mark B. Fisher, *The Logical Trader* (Wiley, 2002)** — `book_logical_trader`, new.

- *What it is.* The ACD method. Price points are plotted relative to the
  opening range; the A and C levels are entry references and the B and D
  levels are stops. Pivot ranges are combined with it to size positions and
  limit risk [R10].
- *Why it matters for the bot.* It is a fully rule-based opening-range method
  with an *offset* (do not enter at the range edge; enter once price has
  cleared it by a set amount). That is a cheap, testable variant of spec S4
  (`sniper_orb_retest`), and it sits in the same lineage as
  [[book_crabel_opening_range]] ([[person_toby_crabel]]). Crypto has no opening
  bell, so the test needs a defined session open (00:00 UTC, London, or New
  York) ([[concept_trading_sessions_killzones]]).
- *KB concepts.* [[concept_breakout_trading]], [[concept_pivot_points]],
  [[concept_trading_sessions_killzones]], [[concept_position_sizing]].
- *Caveat.* Third-party ACD scripts disagree on offsets; take parameters from
  the book itself [R10].

**Andrew Aziz, *How to Day Trade for a Living* (self-published, 2016)** — `book_how_to_day_trade_for_a_living`, new.

- *What it is.* A popular beginner's book on US-stock day trading: risk rules,
  stock selection and core price-action strategies, per a practitioner
  review [R11]. The setup list includes opening-range breakouts, VWAP and
  moving-average trades (T5).
- *Why it matters for the bot.* Its central filter, trading only the few names
  with unusual activity that day, was later tested by Aziz himself with
  Zarattini and Barbon (§7, [R20]). Book and paper together show an idea moving
  from playbook to test. For crypto, the analogue is ranking coins by
  relative volume in the first bars of a session ([[concept_vwap]]).
- *KB concepts.* [[concept_vwap]], [[concept_breakout_trading]],
  [[concept_position_sizing]], [[concept_risk_reward_r_multiples]].
- *Caveat.* The author runs a trading-education community; the book is T2 for
  method, and any performance claim around it is T4.

**Mike Bellafiore, *The PlayBook* (FT Press, 2013)** — `book_the_playbook`, new.

- *What it is.* New traders at SMB Capital walk through real trades and get
  critiqued. Plays include support plays, flags, opening drives, intraday
  levels, bounce and fade trades, pullbacks and scalps [R12]. At SMB, traders
  record one play at the end of each session and review it [R13].
- *Why it matters for the bot.* It is the prop-desk version of what this KB
  already does with Chart Fanatics playbooks. Each play has a context, levels,
  an entry, an exit and a size. That is the schema a bot needs for every
  setup, plus a review loop ([[framework_trading_journal]],
  [[principle_11_record_and_investigate]]).
- *KB concepts.* [[concept_trading_plan]], [[concept_trading_journal_review]],
  [[concept_trade_execution]], [[concept_trade_management]].
- *Caveat.* The SMB blog review is a promotional reprint [R13]; the year varies
  between 2013 (catalogues) and 2014 (copyright page) [R12].

**Trader Dale, *Volume Profile: The Insider's Guide to Trading* (independently published, 2018)** — `book_volume_profile_insiders_guide`, new.

- *What it is.* A short practitioner book (about 196 pages, per a marketplace
  listing) on trading from volume-at-price zones [R14].
- *Why it matters for the bot.* Volume profile is one of the few order-flow
  tools a crypto bot *can* compute: Binance publishes trade-level history, so
  point of control, value area and low-volume nodes can be built without a paid
  feed. It turns [[strategy_carmine_rosato_lvn]] and
  [[strategy_forrest_knight_volume_profile]] into level definitions to test,
  and gives the levels that [[strategy_fabio_valentini_amt_order_flow]] trades from.
  Spec S12 (LVN absorption) still needs true bid/ask data and is not codeable
  on OHLCV ([[synthesis_sniper_entries]]).
- *KB concepts.* [[concept_volume_profile]], [[concept_auction_market_theory]],
  [[concept_order_flow]], [[concept_liquidity]].
- *Caveat.* Self-published and verified here only through a listing (T3).
  For the theory, read [[book_mind_over_markets]] and [[book_markets_in_profile]]
  first; this book adds level-placement habits, not evidence.

## 5. Systematic short-term trading and entry/exit research

**Larry Connors & Cesar Alvarez, *Short Term Trading Strategies That Work* (TradingMarkets, 2008)** — `book_short_term_trading_strategies_that_work`, new.

- *What it is.* The book behind the 2-period RSI pullback: buy sharp
  short-term weakness only while price is above its 200-day average, and exit
  on the first rebound [R15][R16]. The seller blurb mentions 16 strategies;
  its backtest claims are T4 [R15].
- *Why it matters for the bot.* It is the cleanest published family of
  high-hit-rate, short-holding mean-reversion rules, the opposite profile to
  the lab's 2R sniper brackets. It suits the owner's wish to trade often. It
  also brings the risk of that profile: many small wins and occasional large
  losses ([[concept_probability_fat_tails]]). The book argues stops hurt this
  style, which the lab should test, not accept ([[person_larry_connors]];
  same author as [[book_street_smarts]]).
- *Test.* RSI(2) extremes with a 200-period trend filter on 1-hour crypto
  bars, net of maker/taker costs, out of sample.
- *KB concepts.* [[concept_mean_reversion]], [[concept_oscillators_momentum]],
  [[concept_moving_averages]], [[concept_market_regimes]],
  [[strategy_lance_breitstein_mean_reversion]].
- *Caveat.* Built on daily US equities before 2008; the edge may have decayed
  after publication (see [[paper_mclean_pontiff_2016]]).

**Kevin J. Davey, *Entry and Exit Confessions of a Champion Trader* (independently published, 2019)** — `book_entry_exit_confessions`, new.

- *What it is.* 41 entry ideas and 11 exit ideas, each in plain English and
  TradeStation code [R17][R18]. A summary notes they are components, not
  complete strategies [R18].
- *Why it matters for the bot.* The method matters more than the catalogue.
  Test an entry on its own, with a neutral exit (for example a fixed number of
  bars), before adding stops and targets (T5). If the entry has no edge alone,
  no exit will rescue it honestly. The lab's specs mix entry, stop and target
  in one result; this book shows how to separate them. Pair it with Davey's
  [[book_building_winning_algo_systems]], already in the KB.
- *KB concepts.* [[concept_backtesting]], [[concept_trade_execution]],
  [[concept_trade_management]], [[concept_overfitting_validation]].

**Ernest P. Chan, *Machine Trading* (Wiley, 2017)** — `book_machine_trading`, new ([[person_ernest_chan]]).

- *What it is.* A practitioner's guide to algorithmic trading with MATLAB
  code. Chapter 6 is *Intraday Trading and Market Microstructure* and
  chapter 7 is *Bitcoins* [R19].
- *Why it matters for the bot.* The KB has Chan's two earlier books
  ([[book_quantitative_trading_chan]], [[book_algorithmic_trading_chan]]).
  This one adds the two chapters a crypto intraday bot needs most: what the
  order book and order flow can and cannot tell you at short horizons, and how
  bitcoin differs.
- *KB concepts.* [[concept_market_microstructure]], [[concept_order_flow]],
  [[concept_time_series_statistics]], [[concept_machine_learning_finance]].

## 6. Validation, stops and sizing (read these first)

**Robert Pardo, *The Evaluation and Optimization of Trading Strategies* (Wiley, 2nd ed., 2008)** — `book_evaluation_optimization_trading_strategies`, new.

- *What it is.* The standard practitioner text on walk-forward analysis, with
  chapters on walk-forward analysis, performance evaluation and the many faces
  of overfitting [R21]. It revises Pardo's 1992 book [R22].
- *Why it matters for the bot.* The lab uses one split (choose before 2024,
  judge after). Walk-forward rolls that split forward many times. It shows
  whether a configuration works only in one period, and gives a
  walk-forward efficiency to set beside the deflated Sharpe
  ([[paper_deflated_sharpe_2014]], [[paper_bailey_pbo_2017]]). The same
  logic runs through [[synthesis_evidence_lab]]'s overfitting tests.
- *KB concepts.* [[concept_backtesting]], [[concept_overfitting_validation]],
  [[concept_performance_metrics]].

**Timothy Masters, *Testing and Tuning Market Trading Systems* (Apress, 2018)** — `book_testing_tuning_trading_systems`, new.

- *What it is.* Statistical tests for trading systems with C++ code; chapter 7
  is on permutation tests [R23]. The publisher's pitch: "Seemingly good
  backtest performance isn't enough to justify trading real money." [R24]
- *Why it matters for the bot.* A Monte Carlo permutation test asks how often
  the same rule, run on shuffled versions of the price history, does as well
  as it did on the real one. That is the most direct check on whether a sniper
  spec found structure or noise. It complements [[paper_white_2000]] and the
  lab's deflated Sharpe ([[philo_scientific_method]]).
- *KB concepts.* [[concept_overfitting_validation]], [[concept_backtesting]],
  [[concept_time_series_statistics]], [[concept_probabilistic_thinking]].

**John Sweeney, *Maximum Adverse Excursion* (Wiley, 1997)** — `book_maximum_adverse_excursion`, new.

- *What it is.* The first full guide to MAE, a way to estimate a trade's loss
  point before entering by studying how far past trades moved against you
  [R25].
- *Why it matters for the bot.* A sniper entry lives or dies on its stop. At
  $20 the stop also sets whether the position clears the venue minimum
  ([[synthesis_small_account_venues]] §7.4). The lab already writes every trade
  to `10_sniper-lab/backtests/trades.csv.gz`. An MAE and MFE (maximum
  favourable excursion) histogram per spec is the next measurement, and it
  replaces guessed stops with measured ones.
- *KB concepts.* [[concept_trade_management]], [[concept_risk_reward_r_multiples]],
  [[concept_backtesting]].

**Robert Carver, *Leveraged Trading* (Harriman House, 2019)** — `book_leveraged_trading`, new ([[person_robert_carver]]).

- *What it is.* With leverage, losses and costs are magnified. The book's
  answer is a simple starter system on one instrument with one opening rule,
  sized for the right leverage and traded at a suitable frequency, expanded
  later and optionally combined with judgement (semi-automatic trading) [R26].
  The blurb's claim that a few hundred dollars or pounds is enough is publisher
  marketing (T4) [R26].
- *Why it matters for the bot.* This is the closest book to the $20 problem:
  costs set how often you may trade, and volatility sets size. It extends
  [[book_systematic_trading]] to the retail, leveraged, small-account case.
  Read it with [[concept_leverage_margin]] and §8 of
  [[synthesis_small_account_venues]].
- *KB concepts.* [[concept_leverage_margin]], [[concept_position_sizing]],
  [[concept_volatility]], [[concept_risk_of_ruin_drawdown]],
  [[concept_trade_execution]].

**Ryan Jones, *The Trading Game* (Wiley, 1999)** — `book_the_trading_game`, new.

- *What it is.* The source of fixed-ratio sizing. Size goes up one unit only
  after a set profit (the delta) per unit already traded. With a $3,000 delta,
  going from one to two contracts takes $3,000 of profit and from two to three
  another $6,000 [R27]. It was presented as an alternative to fixed-fractional
  sizing for small, unit-based accounts [R28].
- *Why it matters for the bot.* At $20 the minimum order is the binding
  constraint, so fixed-fractional risk often rounds to *one minimum unit or
  nothing*. Fixed ratio is one honest way to plan the step from one unit to two.
  Compare it against [[book_definitive_guide_position_sizing]] and
  [[concept_kelly_criterion_optimal_f]] ([[principle_09_protect_capital]]).
- *Caveat.* A forum user could not reproduce one online table of the formula;
  check the book [R28].

## 7. Non-book course and the research evidence

**ICT 2022 Mentorship (Michael J. Huddleston, Inner Circle Trader YouTube channel)** — non-book, free video course ([[person_michael_huddleston]]).

- *What it is.* A 41-video playlist titled *2022 ICT Mentorship* on the Inner
  Circle Trader channel (read 2026-10-20) [R29]; a summary site dates the
  episodes January to June 2022 [R30]. The KB already describes it in
  [[concept_smart_money_concepts]].
- *Why it matters for the bot.* It is the primary source for the sweep, fair
  value gap, OTE and session models behind specs S1, S2, S3 and S8
  ([[concept_liquidity_sweep_reversal]], [[concept_fair_value_gap]],
  [[concept_premium_discount_ote]], [[concept_trading_sessions_killzones]];
  [[strategy_abraham_perez_ict_orderflow]], [[strategy_nbb_trader_po3_ote_adr]]).
  Read it to get the rules exactly as taught, so the specs test what was
  actually said.
- *What it is not.* Evidence. [[synthesis_sniper_entries]] found no published
  controlled test supporting the ICT tools themselves, and in the lab FVG and
  OTE retraces were negative after costs out of sample. Treat it as T2 for
  method and T4 for any performance claim.

**Heston, Korajczyk & Sadka (2010), *Intraday Patterns in the Cross-Section of Stock Returns*, Journal of Finance 65(4)** [R31] — paper, not in KB.

- *Finding (T1).* Returns continue at half-hour intervals that are exact
  multiples of a trading day, for at least 40 days. Short-term reversal comes
  from liquidity imbalances lasting under an hour and from bid-ask bounce.
  Timing trades can save about the effective spread in execution costs.
- *For the bot.* Two tests. First, does crypto show the same *same time
  tomorrow* continuation on a 24-hour lag? Second, sub-hour reversal is partly
  bid-ask bounce, which a taker cannot capture after paying the spread
  ([[concept_market_microstructure]], [[mathbook_hasbrouck_empirical_microstructure]]).

**Gao, Han, Li & Zhou (2018), *Market Intraday Momentum*, Journal of Financial Economics 129(2)** [R32] — paper, cited in [[synthesis_sniper_entries]].

- *Finding (T1).* On SPY 1993–2013, the first half-hour return (measured from
  the previous close) predicts the last half-hour return. It is stronger on
  volatile, high-volume, recession and major-news days, and appears in ten
  other active ETFs.
- *For the bot.* The best-documented intraday timing effect; the crypto
  version (Shen, Urquhart and Wang) is already in the sniper evidence table.
  It is a candidate *context filter* (trade with the first-hour direction late
  in the session) rather than a sniper entry.

**Zarattini, Barbon & Aziz (2024), *A Profitable Day Trading Strategy for the U.S. Equity Market*, Swiss Finance Institute RP 24-98** [R20] — paper, cited in [[synthesis_sniper_entries]].

- *Finding.* A 5-minute opening-range breakout on more than 7,000 US stocks,
  2016–2023, works much better when limited to stocks with unusual activity
  that day; the paper also compares 15-, 30- and 60-minute ranges [R20].
- *Status.* The headline returns are the authors' backtest and are **T4**
  here, as in [[synthesis_sniper_entries]]. A QuantConnect replication
  reports a positive result (T4) [R33]; an MQL5 replication on indices reports
  net results near zero (T4, via [[synthesis_sniper_entries]]). The lab's own ORB retest on crypto was negative
  after costs out of sample ([[synthesis_sniper_backtests]]). The useful idea
  is the *relative-volume filter*, not the return figure.

**Chague, De-Losso & Giovannetti (2019/2020), *Day Trading for a Living?*** [R34][R35], with **Barber, Lee, Liu & Odean (2014), *The Cross-Section of Speculator Skill*, Journal of Financial Markets 18** [R34][R36] — papers, not in KB.

- *Finding (T1, regulator and exchange data).* Among Brazilians who began day
  trading mini-index futures in 2013–2015 and kept going for at least 300
  days, 97% lost money, only 0.4% earned more than a bank teller, and there was
  no evidence of learning [R35]. The authors conclude it is "virtually
  impossible for an individual to day trade for a living" [R34]. In Taiwan,
  Barber and co-authors found over 80% of day traders lost money after costs
  (2004 study), and fewer than 1% earned predictable profits after fees (2014
  paper) [R36][R37].
- *For the bot.* This is the base rate the sniper lab should assume until its
  own out-of-sample record says otherwise ([[principle_03_future_is_uncertain]],
  [[paper_barber_odean_2000]]). It is also why the lab's gate refuses every
  live signal today. That refusal is the system working, not failing
  ([[philo_capital_preservation]]).

## 8. Already in the KB: read these alongside

These are already in `05_books-top-100/books.yaml`, `06_mathematics-foundations/`
or the KB's paper ids. They are not repeated in `books-sniper.yaml`.

| In-KB id | Why for a sniper bot | Pairs with |
|---|---|---|
| [[book_reading_price_charts_bar_by_bar]] | Brooks's first statement of bar-by-bar reading | Brooks trilogy |
| [[book_crabel_opening_range]] | The original opening-range and narrow-range work behind spec S4 | Fisher, Zarattini et al. |
| [[book_street_smarts]] | Raschke & Connors's short-term patterns, including the Turtle Soup false-breakout entry behind spec S1 ([[person_linda_raschke]]) | Connors & Alvarez |
| [[book_trading_sardines]] | Raschke's short-term trading lessons | Street Smarts |
| [[book_long_term_secrets_short_term_trading]] | Larry Williams's volatility breakouts and short-term patterns | Fisher |
| [[book_mastering_the_trade]] | Carter's intraday setups and session habits | Aziz |
| [[book_ta_multiple_timeframes]] | Shannon on VWAP and moving averages across timeframes | Beggs |
| [[book_art_science_technical_analysis]] | Grimes's pullbacks and failure tests, with tested pattern statistics | Brooks |
| [[book_building_winning_algo_systems]] | Davey's full development and monitoring process | Entry and Exit Confessions |
| [[book_quantitative_trading_chan]], [[book_algorithmic_trading_chan]] | Chan's backtesting and mean-reversion foundations | Machine Trading |
| [[book_systematic_trading]] | Carver's framework for simple, cost-aware rules | Leveraged Trading |
| [[book_trading_systems_and_methods]] | Kaufman's encyclopedia of system types, including the efficiency ratio for regime filters ([[person_perry_kaufman]]) | Pardo |
| [[book_evidence_based_ta]] | Aronson on data-mining bias in rule testing | Masters |
| [[book_advances_financial_ml]] | Labelling with stop, target and time barriers, and meta-labelling to filter a rule's signals | Masters, Davey |
| [[book_definitive_guide_position_sizing]], [[book_mathematics_of_money_management]] | Position sizing and optimal f | The Trading Game |
| [[book_mind_over_markets]], [[book_markets_in_profile]], [[book_trades_about_to_happen]] | Auction market theory, profile and Wyckoff volume reading | Trader Dale |
| [[book_trading_and_exchanges]], [[book_market_microstructure_in_practice]] | How orders, spreads and fills work | Machine Trading ch. 6 |
| [[book_day_swing_trading_currency]] | FX sessions and intraday FX setups | Volman |
| [[mathbook_bouchaud_trades_quotes_prices]], [[mathbook_cartea_algorithmic_hft]] | Order-book dynamics and short-horizon market making, rigorously | Machine Trading |
| [[paper_deflated_sharpe_2014]], [[paper_bailey_pbo_2017]], [[paper_white_2000]] | Multiple-testing corrections the lab already uses | Pardo, Masters |

## 9. Suggested reading order for building the bot (suggestion)

1. **Base rates and validation:** Chague et al. and Barber et al. (§7), then
   Pardo, then Masters. Goal: walk-forward plus a permutation test on the
   lab's best configuration.
2. **Stops and sizing at $20:** Sweeney (MAE from the lab's trade file),
   Carver's *Leveraged Trading*, then Jones. Goal: measured stops and a sizing
   rule that respects the minimum order.
3. **Entry isolation:** Davey's *Entry and Exit Confessions*. Goal: re-run
   each spec with a neutral exit to see whether the entry carries any edge.
4. **Entry logic with its conditions:** Brooks (*Trading Ranges* first, for
   the trader's equation and failed breakouts), then Volman's *Understanding
   Price Action*. Goal: regime-conditioned variants of S1 and S5.
5. **Opening-range family:** Fisher, with [[book_crabel_opening_range]], Gao et
   al. and Zarattini et al. Goal: an ACD-offset variant of S4 with a
   relative-volume filter.
6. **Mean-reversion family:** Connors & Alvarez. Goal: RSI(2) with a trend
   filter on 1-hour crypto, net of costs.
7. **Microstructure for crypto:** Chan's *Machine Trading* chapters 6–7, then
   Trader Dale for volume-profile levels built from trade data.
8. **Source rules, not evidence:** the ICT 2022 mentorship, to check the specs
   match what is taught.

Each goal is a hypothesis for `00_philosophy/research-program.md`, to be judged
by [[framework_decision_protocol]] Gate 4 like every other spec.

## 10. What this list does not settle

- **No book here proves an edge after costs.** The evidence in §7 says the
  base rate for individual day traders is poor, and the lab's own record
  agrees so far.
- **Discretionary books lose context when coded.** Brooks, Volman and Beggs
  rely on judgement the bot does not have. Coding them is a test of a
  simplified version, and a negative result says nothing about the full
  discretionary skill.
- **Transfer is untested.** Most of these books come from US stocks, index
  futures or EUR/USD. Crypto runs 24 hours, has different costs and has no
  single open.
- **Self-published titles** (Beggs, Aziz, Davey's *Confessions*, Trader Dale)
  are T2 for method. Several were verified here only through listings or
  search summaries (marked in Sources).

## Sources

All read on 2026-10-20. *Opened* means the page itself was retrieved; *search
summary* means only a search result describing the page was read.

- [R1] Al Brooks, *Trading Price Action Trends*, Wiley 2011, publisher blurb via bookseller listing: https://tenlong.com.tw/products/9781118066515 (search summary). T1 for what the publisher says.
- [R2] O'Reilly listings for *Trading Price Action Trading Ranges* and *Reversals* (January 2012): https://www.oreilly.com/library/view/-/9781118172339/ and https://oreilly.com/library/view/trading-price-action/9781118172308 (search summary). T1.
- [R3] Bob Volman, *Understanding Price Action*, Light Tower Publishing 2014: https://www.abebooks.com/Understanding-Price-Action-Practical-Analysis-5-Minute/30325842905/bd (opened). T3 listing.
- [R4] Description of *Understanding Price Action* (six months of EUR/USD 5-minute charts): https://www.eltraderfinanciado.com/he/trading-books/understanding-price-action (search summary). T3.
- [R5] *Forex Price Action Scalping* (Light Tower Publishing, 11 October 2011; 70-tick chart, 30-second approximation): https://www.goodreads.com/book/show/13269524-forex-price-action-scalping and https://betterread.com.au/book/forex-price-action-scalping.do (search summary). T3.
- [R6] Practitioner forum, Volman versus Brooks reading order: https://forums.babypips.com/t/new-trader-studying-al-brook-price-action-books/82779 (search summary). T3.
- [R7] NexusFi threads on YTC and Brooks: https://nexusfi.com/showthread.php?p=233556 and https://nexusfi.com/showthread.php?p=908909 (search summary). T3.
- [R8] YTC Price Action Trader reseller page (six volumes, ~590 pages): https://globaltradingtools.com/?p=17029 (search summary). T4.
- [R9] Joe Ross, *Trading by the Minute*, 1997: https://abebooks.com/9789768108258/Trading-Minute-Ross-Joe-9768108258/plp (opened). T3.
- [R10] Mark Fisher, *The Logical Trader* (Wiley 2002) and the ACD method: https://nexusfi.com/a/strategies/acd-trading-method, https://biblio.es/9780471215516, https://www.luxalgo.com/library/concept/acd-method.md (search summary). T3.
- [R11] TraderLion review of *How to Day Trade for a Living*: https://traderlion.com/trading-books/how-to-day-trade-for-a-living/ (search summary). T3.
- [R12] *The PlayBook*, FT Press; library record and Pearson sample pages: https://discover.aclib.us/oreilly/ocn862826961 and https://ptgmedia.pearsoncmg.com/images/9780132937641/samplepages/0132937646.pdf (search summary). T1/T3.
- [R13] SMB Capital blog, review of *The PlayBook*: https://www.smbtraining.com/blog/ls-trades-reviews-the-playbook (search summary). T4 (promotional reprint).
- [R14] Trader Dale, *Volume Profile: The Insider's Guide to Trading*, 2018 listing: https://ebay.it/itm/363344849625 (search summary). T3.
- [R15] Connors & Alvarez, *Short Term Trading Strategies That Work*, TradingMarkets 2008: https://www.abebooks.com/Short-Term-Trading-Strategies-Work-Larry/31620720826/bd (opened). T3.
- [R16] RSI-2 rules as summarised: https://www.luxalgo.com/library/concept/rsi-2.md (search summary). T3.
- [R17] Davey, *Entry and Exit Confessions* editions (independently published, April 2019): https://www.goodreads.com/work/editions/70058912-entry-and-exit-confessions-of-a-champion-trader-52-ways-a-professional (search summary). T3.
- [R18] Summary of *Entry and Exit Confessions* (41 entries, 11 exits; components, not strategies): https://sobrief-staging.onrender.com/books/entry-and-exit-confessions-of-a-champion-trader and https://ebook.cam-ed.com/ebooks/entry-and-exit-confessions-of-a-champion-trader-52-ways-a-professional-speculator-gets-in-and-out-of-the-stock-futures-and-forex-markets (search summary). T3.
- [R19] Wiley-VCH, *Machine Trading* (2017), description and contents: https://www.wiley-vch.de/en/areas-interest/finance-economics-law/machine-trading-978-1-119-21960-6 (opened). T1.
- [R20] Zarattini, Barbon, Aziz, SFI Research Paper 24-98, abstract: https://ideas.repec.org/p/chf/rpseri/rp2498.html (opened). T1 for the method; performance figures T4.
- [R21] Wiley-VCH, Pardo, *The Evaluation and Optimization of Trading Strategies* (2nd ed.), description and contents: https://www.wiley-vch.de/en/areas-interest/finance-economics-law/the-evaluation-and-optimization-of-trading-strategies-978-0-470-12801-5 (opened). T1.
- [R22] Walk forward optimization: https://en.wikipedia.org/wiki/Walk_forward_optimization (search summary). T3.
- [R23] Masters, *Testing and Tuning Market Trading Systems*, catalogue with table of contents: https://ersearch2.cvtisr.sk/vufind/Record/240563/TOC (search summary). T1.
- [R24] Masters, publisher description (Apress 2018): https://www.abebooks.com/Testing-Tuning-Market-Trading-Systems-Timothy/32234804369/bd (opened). T1 for the publisher's text.
- [R25] Wiley-VCH, Sweeney, *Maximum Adverse Excursion* (January 1997, 176 pages): https://www.wiley-vch.de/en/areas-interest/finance-economics-law/maximum-adverse-excursion-978-0-471-14152-5 (opened). T1.
- [R26] Pan Macmillan, Carver, *Leveraged Trading* (Harriman House, 29 October 2019, 346 pages): https://www.panmacmillan.com/authors/robert-carver/leveraged-trading/9780857197221 (opened). T1 for the publisher's text; the few-hundred-dollars line is T4.
- [R27] Adaptrade, fixed ratio position sizing (Jones, *The Trading Game*, Wiley 1999): https://www.adaptrade.com/MSA/fixratio.htm (opened). T3.
- [R28] Fixed ratio summaries and a forum reproduction problem: https://www.luxalgo.com/library/concept/fixed-ratio/ and https://www.metalsmine.com/thread/72590-fixed-ratio-position-sizing-need-help (search summary). T3.
- [R29] YouTube playlist *2022 ICT Mentorship*, Inner Circle Trader channel, 41 videos: https://www.youtube.com/playlist?list=PLVgHx4Z63paYiFGQ56PjTF1PGePL3r69s (opened). T2.
- [R30] Episode dates for the 2022 mentorship: https://videohighlight.com/playlist/PLVgHx4Z63paYiFGQ56PjTF1PGePL3r69s (search summary). T3.
- [R31] Heston, Korajczyk, Sadka, abstract, Journal of Finance 65(4) 1369–1407: https://arxiv.org/abs/1005.3535 (opened). T1.
- [R32] Gao, Han, Li, Zhou, Journal of Financial Economics 129(2) 394–414, abstract: https://profiles.wustl.edu/en/publications/market-intraday-momentum/ (opened). T1.
- [R33] QuantConnect replication of the stocks-in-play ORB: https://www.quantconnect.com/research/18444/opening-range-breakout-for-stocks-in-play/ (search summary). T4.
- [R34] Chague, De-Losso, Giovannetti, working paper 2019, abstract and references: https://ideas.repec.org/p/spa/wpaper/2019wpecon47.html (opened). T1.
- [R35] Chague, De-Losso, Giovannetti, FGV version (2020-02), abstract: https://econpapers.repec.org/RePEc:fgv:eesptd:525 (opened). T1.
- [R36] CXO Advisory on Barber, Lee, Liu, Odean (2004 Taiwan study): https://www.cxoadvisory.com/individual-investing/do-day-traders-make-money/ (opened). T3 summary of a T1 paper.
- [R37] Barber, Lee, Liu, Odean (2014), *The Cross-Section of Speculator Skill*, Journal of Financial Markets 18: https://www.escholarship.org/uc/item/7k75v0qx (search summary). T1.
