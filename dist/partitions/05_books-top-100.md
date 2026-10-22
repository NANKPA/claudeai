# Partition 05_books-top-100


<!-- ===== FILE: trading-intelligence/05_books-top-100/README.md ===== -->

# Partition 05 — Top 100 Trading Books

| File | What |
|---|---|
| `books.yaml` → `top-100-trading-books.md` | Ranked list with author, year, category, one-line key idea, book-to-book lineage (`derived_from`), people featured, and the concepts each book covers |
| `summaries/` | Deep summaries of 13 foundational books, written in our own words and linked to concepts |

**Ranking method:** editorial (Claude, T5). Weighted by recurrence across
major best-of lists, citation by Market Wizards interviewees, and how many
later ideas descend from the book in the lineage graph. It is not a sales
ranking.

**Categories:** classics · interviews · technical_analysis · price_action ·
auction_market_theory · growth_momentum · trend_following · psychology ·
risk_money_management · randomness_risk · macro · microstructure_execution ·
options_volatility · quant_algorithmic · forex.

Mathematics texts live in `06_mathematics-foundations/` (some, such as Hull,
Harris, Vince, López de Prado, and Aronson, appear in both with a `same_as` link).


<!-- ===== FILE: trading-intelligence/05_books-top-100/books-qa-review.md ===== -->

# Book registry fact-check (Open Library, 2026-10-11)

`tools/scrapers/books_enrich.py` looked up every book in `books.yaml` and
`../06_mathematics-foundations/math-books.yaml` on Open Library. Raw flags are in
`books.qa.txt`; enrichment (ISBNs, subjects, covers) is in `books.enriched.yaml`.

**Verdict: no wrong years or authors in the registry. Two edition notes added.**

| Flag type | Count | Review |
|---|---|---|
| YEAR mismatch | 24 | 22 are false alarms: Open Library's `first_publish_year` comes from the record with the most editions, which is often a reprint (e.g. *Market Wizards* 2012 reissue vs 1989 original; *Technical Analysis of Stock Trends* 1992 vs 1948; *The Black Swan* 2005 is a mis-match). Two were real edition nuances and are now annotated: *Trading Systems and Methods* (1978 as *Commodity Trading Systems and Methods*; current title from 1998) and Kathy Lien's book (2005 as *Day Trading the Currency Market*; current title from 2008, so the registry year is now 2008). |
| NOT FOUND | 15 | Search misses for long or subtitle-heavy titles, specialist monographs, and edited volumes. These are not evidence the books are wrong. |

Re-run with `python3 tools/scrapers/books_enrich.py`.


<!-- ===== FILE: trading-intelligence/05_books-top-100/books.yaml ===== -->

```yaml
# Top 100 trading books — editorial canon.
# Ranking method (Claude, T5): weighted by (a) recurrence across major best-of lists
# (Tradezella 2026, TraderLion, Simpler Trading, HackerNoon, QuantStart), (b) citation by
# Market Wizards interviewees and the legends in people.yaml, (c) foundational position
# in the idea-lineage graph (books that many later ideas descend from rank higher).
# `covers` -> concept ids; `derived_from` -> earlier books this one builds on;
# `features` -> people interviewed/profiled. key_idea is a one-line paraphrase.

books:
  - {rank: 1, id: book_reminiscences_stock_operator, title: "Reminiscences of a Stock Operator", authors: [person_edwin_lefevre], author: "Edwin Lefèvre", year: 1923, category: classics, features: [person_jesse_livermore],
     key_idea: "Fictionalised Livermore: the market is never wrong, cut losses, sit tight in big moves, follow the line of least resistance.",
     covers: [concept_trend_following, concept_trading_psychology, concept_trade_management, concept_market_sentiment]}
  - {rank: 2, id: book_market_wizards, title: "Market Wizards", authors: [person_jack_schwager], author: "Jack D. Schwager", year: 1989, category: interviews,
     features: [person_michael_marcus, person_bruce_kovner, person_richard_dennis, person_paul_tudor_jones, person_ed_seykota, person_larry_hite, person_william_oneil, person_martin_schwartz, person_van_tharp],
     key_idea: "Top traders share no single method but universally share risk control, discipline, and a method that fits their personality.",
     covers: [concept_edge, concept_trading_psychology, concept_risk_of_ruin_drawdown, concept_trend_following]}
  - {rank: 3, id: book_trading_in_the_zone, title: "Trading in the Zone", authors: [person_mark_douglas], author: "Mark Douglas", year: 2000, category: psychology, derived_from: [book_disciplined_trader],
     key_idea: "Consistency comes from thinking in probabilities and fully accepting risk before each trade (the five fundamental truths).",
     covers: [concept_probabilistic_thinking, concept_trading_psychology, concept_edge]}
  - {rank: 4, id: book_ta_financial_markets, title: "Technical Analysis of the Financial Markets", authors: [person_john_murphy], author: "John J. Murphy", year: 1999, category: technical_analysis, derived_from: [book_ta_stock_trends, book_dow_theory_rhea],
     key_idea: "The standard reference for chart construction, trend, patterns, indicators, and intermarket principles.",
     covers: [concept_chart_patterns, concept_support_resistance, concept_moving_averages, concept_oscillators_momentum, concept_dow_theory, concept_intermarket_analysis]}
  - {rank: 5, id: book_new_market_wizards, title: "The New Market Wizards", authors: [person_jack_schwager], author: "Jack D. Schwager", year: 1992, category: interviews, derived_from: [book_market_wizards],
     features: [person_stanley_druckenmiller, person_linda_raschke, person_william_eckhardt, person_tom_basso, person_victor_sperandeo],
     key_idea: "Second round of interviews: macro, systematic, and psychology lessons (Eckhardt, Druckenmiller, Raschke, Basso).",
     covers: [concept_edge, concept_position_sizing, concept_trading_psychology]}
  - {rank: 6, id: book_how_to_make_money_in_stocks, title: "How to Make Money in Stocks", authors: [person_william_oneil], author: "William J. O'Neil", year: 1988, category: growth_momentum, derived_from: [book_how_to_trade_in_stocks, book_battle_for_investment_survival],
     key_idea: "CANSLIM: buy leading growth stocks breaking out of proper bases in a confirmed uptrend; cut losses at 7–8%.",
     covers: [concept_growth_momentum_canslim, concept_breakout_trading, concept_trade_management]}
  - {rank: 7, id: book_trade_like_stock_market_wizard, title: "Trade Like a Stock Market Wizard", authors: [person_mark_minervini], author: "Mark Minervini", year: 2013, category: growth_momentum, derived_from: [book_how_to_make_money_in_stocks, book_secrets_bull_bear_markets],
     key_idea: "SEPA: trend template, earnings catalysts, and VCP entries with tight, predefined risk.",
     covers: [concept_growth_momentum_canslim, concept_position_sizing, concept_volatility]}
  - {rank: 8, id: book_ta_stock_trends, title: "Technical Analysis of Stock Trends", authors: [person_robert_d_edwards, person_john_magee], author: "Robert D. Edwards & John Magee", year: 1948, category: technical_analysis, derived_from: [book_dow_theory_rhea],
     key_idea: "The original catalogue of chart patterns and trendline/support-resistance analysis.",
     covers: [concept_chart_patterns, concept_trendlines, concept_support_resistance, concept_dow_theory]}
  - {rank: 9, id: book_trade_your_way_financial_freedom, title: "Trade Your Way to Financial Freedom", authors: [person_van_tharp], author: "Van K. Tharp", year: 1998, category: risk_money_management,
     key_idea: "Expectancy in R-multiples and position sizing, not entries, drive results; design a system that fits you.",
     covers: [concept_expectancy, concept_position_sizing, concept_risk_reward_r_multiples, concept_trading_plan]}
  - {rank: 10, id: book_fooled_by_randomness, title: "Fooled by Randomness", authors: [person_nassim_taleb], author: "Nassim Nicholas Taleb", year: 2001, category: randomness_risk,
     key_idea: "Survivorship bias and luck masquerade as skill; judge decisions by their alternative histories.",
     covers: [concept_probability_fat_tails, concept_overfitting_validation, concept_probabilistic_thinking]}
  - {rank: 11, id: book_alchemy_of_finance, title: "The Alchemy of Finance", authors: [person_george_soros], author: "George Soros", year: 1987, category: macro,
     key_idea: "Reflexivity: perceptions change fundamentals, producing boom-bust sequences; includes a real-time trading diary.",
     covers: [concept_reflexivity, concept_fundamental_macro_analysis, concept_market_sentiment]}
  - {rank: 12, id: book_trend_following_covel, title: "Trend Following", authors: [person_michael_covel], author: "Michael W. Covel", year: 2004, category: trend_following,
     features: [person_ed_seykota, person_jerry_parker, person_larry_hite, person_richard_dennis],
     key_idea: "Price-based trend following with strict risk control is a durable, crisis-resilient strategy.",
     covers: [concept_trend_following, concept_position_sizing]}
  - {rank: 13, id: book_way_of_the_turtle, title: "Way of the Turtle", authors: [person_curtis_faith], author: "Curtis Faith", year: 2007, category: trend_following,
     key_idea: "The Turtle rules (Donchian breakouts, N-based sizing) and why most people can't follow them.",
     covers: [concept_trend_following, concept_position_sizing, concept_volatility, concept_breakout_trading]}
  - {rank: 14, id: book_japanese_candlestick_charting, title: "Japanese Candlestick Charting Techniques", authors: [person_steve_nison], author: "Steve Nison", year: 1991, category: technical_analysis,
     key_idea: "Candlestick patterns as readings of crowd psychology, best combined with Western technicals.",
     covers: [concept_candlestick_patterns, concept_price_action]}
  - {rank: 15, id: book_mind_over_markets, title: "Mind Over Markets", authors: [person_james_dalton, person_eric_jones, person_robert_dalton], author: "James F. Dalton, Eric T. Jones & Robert B. Dalton", year: 1990, category: auction_market_theory, derived_from: [book_markets_and_market_logic],
     key_idea: "Market Profile and auction market theory: value, day types, balance vs imbalance, and the auction's logic.",
     covers: [concept_auction_market_theory, concept_volume_profile, concept_market_regimes]}
  - {rank: 16, id: book_how_to_trade_in_stocks, title: "How to Trade in Stocks", authors: [person_jesse_livermore], author: "Jesse Livermore", year: 1940, category: classics,
     key_idea: "Pivotal points, timing, pyramiding, and the Livermore market key.",
     covers: [concept_trend_following, concept_breakout_trading, concept_trade_management]}
  - {rank: 17, id: book_trading_for_a_living, title: "Trading for a Living", authors: [person_alexander_elder], author: "Dr. Alexander Elder", year: 1993, category: technical_analysis,
     key_idea: "The three Ms (mind, method, money); Triple Screen multi-timeframe system; the 2% and 6% rules.",
     covers: [concept_multi_timeframe_analysis, concept_trading_psychology, concept_position_sizing, concept_oscillators_momentum]}
  - {rank: 18, id: book_disciplined_trader, title: "The Disciplined Trader", authors: [person_mark_douglas], author: "Mark Douglas", year: 1990, category: psychology,
     key_idea: "Mental frameworks are the bottleneck; traders must restructure beliefs about risk and being wrong.",
     covers: [concept_trading_psychology]}
  - {rank: 19, id: book_best_loser_wins, title: "Best Loser Wins", authors: [person_tom_hougaard], author: "Tom Hougaard", year: 2022, category: psychology, derived_from: [book_trading_in_the_zone],
     key_idea: "Winning traders are the best losers; train behaviour against instinct (add to winners, cut losers instantly).",
     covers: [concept_trading_psychology, concept_trade_management]}
  - {rank: 20, id: book_man_for_all_markets, title: "A Man for All Markets", authors: [person_ed_thorp], author: "Edward O. Thorp", year: 2017, category: interviews, derived_from: [book_beat_the_dealer],
     key_idea: "From card counting to hedge funds: measurable edge plus Kelly sizing plus risk discipline.",
     covers: [concept_edge, concept_kelly_criterion_optimal_f, concept_options_greeks]}
  - {rank: 21, id: book_principles_dalio, title: "Principles", authors: [person_ray_dalio], author: "Ray Dalio", year: 2017, category: macro,
     key_idea: "Radical transparency, believability-weighted decisions, and systematising lessons from mistakes.",
     covers: [concept_trading_journal_review, concept_correlation_portfolio_risk, concept_probabilistic_thinking]}
  - {rank: 22, id: book_reading_price_charts_bar_by_bar, title: "Reading Price Charts Bar by Bar", authors: [person_al_brooks], author: "Al Brooks", year: 2009, category: price_action,
     key_idea: "Every bar tells who controls the market; trade two-legged pullbacks and failed breakouts in context.",
     covers: [concept_price_action, concept_breakout_trading, concept_market_regimes]}
  - {rank: 23, id: book_street_smarts, title: "Street Smarts", authors: [person_linda_raschke, person_larry_connors], author: "Linda Bradford Raschke & Laurence A. Connors", year: 1995, category: price_action,
     key_idea: "Short-term setups including Turtle Soup (fading failed breakouts), the Holy Grail, and 80-20s.",
     covers: [concept_liquidity_sweep_reversal, concept_breakout_trading, concept_mean_reversion]}
  - {rank: 24, id: book_option_volatility_pricing, title: "Option Volatility & Pricing", authors: [person_sheldon_natenberg], author: "Sheldon Natenberg", year: 1988, category: options_volatility,
     key_idea: "Volatility is the key input; trade options as volatility positions managed through the Greeks.",
     covers: [concept_options_greeks, concept_volatility]}
  - {rank: 25, id: book_trading_and_exchanges, title: "Trading and Exchanges", authors: [person_larry_harris], author: "Larry Harris", year: 2003, category: microstructure_execution,
     key_idea: "Who trades, why, and how market structure, order types, and dealers shape prices and costs.",
     covers: [concept_market_microstructure, concept_trade_execution, concept_liquidity]}
  - {rank: 26, id: book_evidence_based_ta, title: "Evidence-Based Technical Analysis", authors: [person_david_aronson], author: "David Aronson", year: 2006, category: quant_algorithmic,
     key_idea: "Apply the scientific method and data-snooping corrections; most TA rules fail rigorous testing.",
     covers: [concept_overfitting_validation, concept_backtesting, concept_random_walk_efficient_markets]}
  - {rank: 27, id: book_man_who_solved_the_market, title: "The Man Who Solved the Market", authors: [person_gregory_zuckerman], author: "Gregory Zuckerman", year: 2019, category: interviews, features: [person_jim_simons],
     key_idea: "How Renaissance Technologies used scientists, data, and small statistical edges at scale.",
     covers: [concept_machine_learning_finance, concept_time_series_statistics, concept_edge]}
  - {rank: 28, id: book_stock_market_wizards, title: "Stock Market Wizards", authors: [person_jack_schwager], author: "Jack D. Schwager", year: 2001, category: interviews, derived_from: [book_market_wizards], features: [person_mark_minervini],
     key_idea: "Equity-focused wizards; common thread of risk control and adaptability.",
     covers: [concept_growth_momentum_canslim, concept_edge]}
  - {rank: 29, id: book_hedge_fund_market_wizards, title: "Hedge Fund Market Wizards", authors: [person_jack_schwager], author: "Jack D. Schwager", year: 2012, category: interviews, derived_from: [book_market_wizards], features: [person_ed_thorp, person_ray_dalio],
     key_idea: "Hedge-fund managers on process, risk, and adaptation; Schwager's 40 lessons.",
     covers: [concept_correlation_portfolio_risk, concept_edge, concept_risk_of_ruin_drawdown]}
  - {rank: 30, id: book_unknown_market_wizards, title: "Unknown Market Wizards", authors: [person_jack_schwager], author: "Jack D. Schwager", year: 2020, category: interviews, derived_from: [book_market_wizards],
     key_idea: "Individual traders with extraordinary audited records; edge comes in many forms.",
     covers: [concept_edge, concept_trading_psychology]}
  - {rank: 31, id: book_diary_professional_commodity_trader, title: "Diary of a Professional Commodity Trader", authors: [person_peter_brandt], author: "Peter L. Brandt", year: 2011, category: technical_analysis, derived_from: [book_ta_stock_trends],
     key_idea: "Classical charting run as a business: trade logs, risk rules, and why most signals fail.",
     covers: [concept_chart_patterns, concept_risk_reward_r_multiples, concept_trading_journal_review]}
  - {rank: 32, id: book_secrets_bull_bear_markets, title: "Secrets for Profiting in Bull and Bear Markets", authors: [person_stan_weinstein], author: "Stan Weinstein", year: 1988, category: growth_momentum,
     key_idea: "Stage analysis with the 30-week MA: buy Stage 2 breakouts, avoid Stage 4.",
     covers: [concept_growth_momentum_canslim, concept_moving_averages, concept_market_regimes]}
  - {rank: 33, id: book_how_i_made_2000000, title: "How I Made $2,000,000 in the Stock Market", authors: [person_nicolas_darvas], author: "Nicolas Darvas", year: 1960, category: classics, derived_from: [book_battle_for_investment_survival],
     key_idea: "Box theory: buy breakouts of price boxes in stocks with rising earnings; use stop-loss orders.",
     covers: [concept_breakout_trading, concept_growth_momentum_canslim]}
  - {rank: 34, id: book_psychology_of_trading_steenbarger, title: "The Psychology of Trading", authors: [person_brett_steenbarger], author: "Brett N. Steenbarger", year: 2003, category: psychology,
     key_idea: "Brief-therapy techniques applied to trading: change patterns through structured self-observation.",
     covers: [concept_trading_psychology, concept_trading_journal_review]}
  - {rank: 35, id: book_mathematics_of_money_management, title: "The Mathematics of Money Management", authors: [person_ralph_vince], author: "Ralph Vince", year: 1992, category: risk_money_management,
     key_idea: "Optimal f and the geometry of position sizing; leverage drives both growth and ruin.",
     covers: [concept_kelly_criterion_optimal_f, concept_position_sizing, concept_risk_of_ruin_drawdown]}
  - {rank: 36, id: book_long_term_secrets_short_term_trading, title: "Long-Term Secrets to Short-Term Trading", authors: [person_larry_williams], author: "Larry Williams", year: 1999, category: price_action,
     key_idea: "Short-term swings, volatility breakouts, and day-of-week/time patterns from a champion trader.",
     covers: [concept_trading_sessions_killzones, concept_volatility, concept_breakout_trading]}
  - {rank: 37, id: book_markets_in_profile, title: "Markets in Profile", authors: [person_james_dalton], author: "James F. Dalton", year: 2007, category: auction_market_theory, derived_from: [book_mind_over_markets],
     key_idea: "Market Profile meets behavioural finance across timeframes."
     , covers: [concept_auction_market_theory, concept_volume_profile, concept_market_sentiment]}
  - {rank: 38, id: book_trades_about_to_happen, title: "Trades About to Happen", authors: [person_david_weis], author: "David H. Weis", year: 2013, category: auction_market_theory, derived_from: [book_studies_in_tape_reading],
     key_idea: "Modern Wyckoff: reading springs, upthrusts, and effort vs result on bar charts and Weis waves.",
     covers: [concept_wyckoff_method, concept_liquidity_sweep_reversal]}
  - {rank: 39, id: book_studies_in_tape_reading, title: "Studies in Tape Reading", authors: [person_richard_wyckoff], author: "Rollo Tape (Richard D. Wyckoff)", year: 1910, category: classics,
     key_idea: "Reading the tape to infer the intentions of large operators: the root of order-flow analysis.",
     covers: [concept_order_flow, concept_wyckoff_method]}
  - {rank: 40, id: book_tape_reading_market_tactics, title: "Tape Reading and Market Tactics", authors: [person_humphrey_neill], author: "Humphrey B. Neill", year: 1931, category: classics, derived_from: [book_studies_in_tape_reading],
     key_idea: "Volume and price behaviour reveal supply and demand; follow the tape, not opinions.",
     covers: [concept_order_flow, concept_market_sentiment]}
  - {rank: 41, id: book_black_swan, title: "The Black Swan", authors: [person_nassim_taleb], author: "Nassim Nicholas Taleb", year: 2007, category: randomness_risk, derived_from: [book_fooled_by_randomness],
     key_idea: "Rare, high-impact events dominate outcomes and are systematically underestimated.",
     covers: [concept_probability_fat_tails, concept_risk_of_ruin_drawdown]}
  - {rank: 42, id: book_misbehavior_of_markets, title: "The (Mis)Behavior of Markets", authors: [person_benoit_mandelbrot, person_richard_hudson], author: "Benoit Mandelbrot & Richard L. Hudson", year: 2004, category: randomness_risk,
     key_idea: "Prices are fractal and fat-tailed; Gaussian finance underestimates risk.",
     covers: [concept_probability_fat_tails, concept_random_walk_efficient_markets, concept_volatility]}
  - {rank: 43, id: book_thinking_fast_slow, title: "Thinking, Fast and Slow", authors: [person_daniel_kahneman], author: "Daniel Kahneman", year: 2011, category: psychology,
     key_idea: "System 1/System 2, heuristics and biases, prospect theory and loss aversion.",
     covers: [concept_trading_psychology, concept_probabilistic_thinking]}
  - {rank: 44, id: book_thinking_in_bets, title: "Thinking in Bets", authors: [person_annie_duke], author: "Annie Duke", year: 2018, category: psychology,
     key_idea: "Separate decision quality from outcome; avoid 'resulting'.",
     covers: [concept_probabilistic_thinking, concept_trading_journal_review]}
  - {rank: 45, id: book_mental_game_of_trading, title: "The Mental Game of Trading", authors: [person_jared_tendler], author: "Jared Tendler", year: 2021, category: psychology,
     key_idea: "Diagnose greed, fear, tilt, confidence, and discipline problems and fix their root flaws.",
     covers: [concept_trading_psychology]}
  - {rank: 46, id: book_daily_trading_coach, title: "The Daily Trading Coach", authors: [person_brett_steenbarger], author: "Brett N. Steenbarger", year: 2009, category: psychology, derived_from: [book_psychology_of_trading_steenbarger],
     key_idea: "101 lessons for becoming your own trading coach.",
     covers: [concept_trading_psychology, concept_trading_journal_review]}
  - {rank: 47, id: book_encyclopedia_chart_patterns, title: "Encyclopedia of Chart Patterns", authors: [person_thomas_bulkowski], author: "Thomas N. Bulkowski", year: 2000, category: technical_analysis, derived_from: [book_ta_stock_trends],
     key_idea: "Statistical performance of dozens of chart patterns: failure rates, average moves, throwbacks.",
     covers: [concept_chart_patterns, concept_backtesting]}
  - {rank: 48, id: book_elliott_wave_principle, title: "Elliott Wave Principle", authors: [person_al_frost, person_robert_prechter], author: "A. J. Frost & Robert R. Prechter Jr.", year: 1978, category: technical_analysis,
     key_idea: "Markets unfold in 5-3 wave patterns related by Fibonacci ratios.",
     covers: [concept_elliott_wave, concept_fibonacci]}
  - {rank: 49, id: book_bollinger_on_bollinger_bands, title: "Bollinger on Bollinger Bands", authors: [person_john_bollinger], author: "John Bollinger", year: 2001, category: technical_analysis,
     key_idea: "Relative definitions of high and low via volatility bands; squeezes and band walks.",
     covers: [concept_bollinger_bands, concept_volatility]}
  - {rank: 50, id: book_new_concepts_technical_trading_systems, title: "New Concepts in Technical Trading Systems", authors: [person_welles_wilder], author: "J. Welles Wilder Jr.", year: 1978, category: technical_analysis,
     key_idea: "Introduced RSI, ATR, ADX/DMI, and Parabolic SAR.",
     covers: [concept_oscillators_momentum, concept_volatility, concept_market_regimes]}
  - {rank: 51, id: book_intermarket_analysis, title: "Intermarket Analysis", authors: [person_john_murphy], author: "John J. Murphy", year: 2004, category: macro,
     key_idea: "Bonds, stocks, commodities, and currencies move in linked cycles.",
     covers: [concept_intermarket_analysis, concept_fundamental_macro_analysis]}
  - {rank: 52, id: book_technical_analysis_explained, title: "Technical Analysis Explained", authors: [person_martin_pring], author: "Martin J. Pring", year: 1980, category: technical_analysis,
     key_idea: "Comprehensive TA with an emphasis on market cycles and momentum.",
     covers: [concept_oscillators_momentum, concept_market_regimes, concept_chart_patterns]}
  - {rank: 53, id: book_art_science_technical_analysis, title: "The Art and Science of Technical Analysis", authors: [person_adam_grimes], author: "Adam Grimes", year: 2012, category: technical_analysis,
     key_idea: "Statistically grounded price action: pullbacks, failure tests, and quantified edges.",
     covers: [concept_price_action, concept_backtesting, concept_market_structure]}
  - {rank: 54, id: book_mastering_the_trade, title: "Mastering the Trade", authors: [person_john_carter], author: "John F. Carter", year: 2005, category: price_action,
     key_idea: "Intraday and swing setups including the squeeze; psychology of the retail trader.",
     covers: [concept_bollinger_bands, concept_breakout_trading, concept_trading_sessions_killzones]}
  - {rank: 55, id: book_think_trade_like_champion, title: "Think & Trade Like a Champion", authors: [person_mark_minervini], author: "Mark Minervini", year: 2017, category: growth_momentum, derived_from: [book_trade_like_stock_market_wizard],
     key_idea: "Risk management and process for super-performance: progressive exposure, selling rules.",
     covers: [concept_position_sizing, concept_trade_management, concept_growth_momentum_canslim]}
  - {rank: 56, id: book_complete_turtletrader, title: "The Complete TurtleTrader", authors: [person_michael_covel], author: "Michael W. Covel", year: 2007, category: trend_following, derived_from: [book_trend_following_covel], features: [person_richard_dennis, person_william_eckhardt, person_jerry_parker],
     key_idea: "History of the Turtle experiment and what happened to the Turtles.",
     covers: [concept_trend_following]}
  - {rank: 57, id: book_following_the_trend, title: "Following the Trend", authors: [person_andreas_clenow], author: "Andreas F. Clenow", year: 2012, category: trend_following, derived_from: [book_way_of_the_turtle],
     key_idea: "A complete diversified futures trend-following model with year-by-year analysis.",
     covers: [concept_trend_following, concept_correlation_portfolio_risk]}
  - {rank: 58, id: book_systematic_trading, title: "Systematic Trading", authors: [person_robert_carver], author: "Robert Carver", year: 2015, category: quant_algorithmic,
     key_idea: "A framework for systematic rules, forecast scaling, volatility targeting, and avoiding overfitting.",
     covers: [concept_position_sizing, concept_overfitting_validation, concept_trend_following, concept_volatility]}
  - {rank: 59, id: book_quantitative_trading_chan, title: "Quantitative Trading", authors: [person_ernest_chan], author: "Ernest P. Chan", year: 2008, category: quant_algorithmic,
     key_idea: "Building and backtesting a retail quant business; Kelly sizing; pitfalls.",
     covers: [concept_backtesting, concept_kelly_criterion_optimal_f, concept_mean_reversion]}
  - {rank: 60, id: book_algorithmic_trading_chan, title: "Algorithmic Trading: Winning Strategies and Their Rationale", authors: [person_ernest_chan], author: "Ernest P. Chan", year: 2013, category: quant_algorithmic, derived_from: [book_quantitative_trading_chan],
     key_idea: "Mean-reversion (cointegration, pairs) and momentum strategies with statistical tests.",
     covers: [concept_mean_reversion, concept_time_series_statistics, concept_trend_following]}
  - {rank: 61, id: book_advances_financial_ml, title: "Advances in Financial Machine Learning", authors: [person_marcos_lopez_de_prado], author: "Marcos López de Prado", year: 2018, category: quant_algorithmic,
     key_idea: "Information bars, triple-barrier labels, meta-labeling, purged CV, and backtest-overfitting statistics.",
     covers: [concept_machine_learning_finance, concept_overfitting_validation, concept_backtesting]}
  - {rank: 62, id: book_inside_the_black_box, title: "Inside the Black Box", authors: [person_rishi_narang], author: "Rishi K. Narang", year: 2009, category: quant_algorithmic,
     key_idea: "Anatomy of a quant strategy: alpha, risk, transaction cost, and portfolio construction models.",
     covers: [concept_optimal_execution_market_impact, concept_edge]}
  - {rank: 63, id: book_building_winning_algo_systems, title: "Building Winning Algorithmic Trading Systems", authors: [person_kevin_davey], author: "Kevin J. Davey", year: 2014, category: quant_algorithmic,
     key_idea: "A champion trader's process for developing, validating, and monitoring systems.",
     covers: [concept_backtesting, concept_overfitting_validation]}
  - {rank: 64, id: book_trading_systems_and_methods, title: "Trading Systems and Methods", authors: [person_perry_kaufman], author: "Perry J. Kaufman", year: 1978, category: quant_algorithmic,
     edition_note: "First published 1978 as Commodity Trading Systems and Methods; current title since the 1998 3rd edition.",
     key_idea: "Encyclopedic reference of trading systems, indicators, and testing methods.",
     covers: [concept_trend_following, concept_backtesting, concept_market_regimes]}
  - {rank: 65, id: book_expected_returns, title: "Expected Returns", authors: [person_antti_ilmanen], author: "Antti Ilmanen", year: 2011, category: quant_algorithmic,
     key_idea: "A synthesis of risk premia: value, carry, momentum, volatility, and their evidence.",
     covers: [concept_carry_trade, concept_trend_following, concept_edge]}
  - {rank: 66, id: book_efficiently_inefficient, title: "Efficiently Inefficient", authors: [person_lasse_pedersen], author: "Lasse Heje Pedersen", year: 2015, category: quant_algorithmic,
     key_idea: "Markets are efficiently inefficient: hedge-fund strategies exist because of costs and limits to arbitrage.",
     covers: [concept_random_walk_efficient_markets, concept_trend_following, concept_carry_trade]}
  - {rank: 67, id: book_options_strategic_investment, title: "Options as a Strategic Investment", authors: [person_lawrence_mcmillan], author: "Lawrence G. McMillan", year: 1980, category: options_volatility,
     key_idea: "The comprehensive reference on options strategies and their risks.",
     covers: [concept_options_greeks]}
  - {rank: 68, id: book_dynamic_hedging, title: "Dynamic Hedging", authors: [person_nassim_taleb], author: "Nassim Nicholas Taleb", year: 1997, category: options_volatility,
     key_idea: "Practitioner's guide to managing vanilla and exotic option risk; tails and model risk.",
     covers: [concept_options_greeks, concept_probability_fat_tails]}
  - {rank: 69, id: book_options_futures_derivatives, title: "Options, Futures, and Other Derivatives", authors: [person_john_hull], author: "John C. Hull", year: 1989, category: options_volatility,
     key_idea: "Standard textbook on derivatives pricing and hedging.",
     covers: [concept_options_greeks, concept_stochastic_processes]}
  - {rank: 70, id: book_day_swing_trading_currency, title: "Day Trading and Swing Trading the Currency Market", authors: [person_kathy_lien], author: "Kathy Lien", year: 2008, category: forex,
     edition_note: "First published 2005 as Day Trading the Currency Market; retitled for the 2008 2nd edition.",
     key_idea: "FX-specific technical and fundamental strategies; session behaviour and macro drivers.",
     covers: [concept_fundamental_macro_analysis, concept_trading_sessions_killzones, concept_carry_trade, concept_news_trading]}
  - {rank: 71, id: book_inside_house_of_money, title: "Inside the House of Money", authors: [person_steven_drobny], author: "Steven Drobny", year: 2006, category: macro,
     key_idea: "Interviews with global macro managers on how they think and size trades.",
     covers: [concept_fundamental_macro_analysis, concept_position_sizing]}
  - {rank: 72, id: book_more_money_than_god, title: "More Money Than God", authors: [person_sebastian_mallaby], author: "Sebastian Mallaby", year: 2010, category: interviews, features: [person_george_soros, person_stanley_druckenmiller, person_paul_tudor_jones, person_jim_simons],
     key_idea: "History of hedge funds: Jones, Soros, Robertson, Tudor Jones, Renaissance.",
     covers: [concept_fundamental_macro_analysis, concept_reflexivity]}
  - {rank: 73, id: book_when_genius_failed, title: "When Genius Failed", authors: [person_roger_lowenstein], author: "Roger Lowenstein", year: 2000, category: randomness_risk,
     key_idea: "LTCM's collapse: leverage, correlation, and liquidity risk overwhelm brilliant models.",
     covers: [concept_risk_of_ruin_drawdown, concept_correlation_portfolio_risk, concept_probability_fat_tails]}
  - {rank: 74, id: book_big_debt_crises, title: "Big Debt Crises", authors: [person_ray_dalio], author: "Ray Dalio", year: 2018, category: macro,
     key_idea: "A template for deflationary and inflationary debt crises with case studies.",
     covers: [concept_fundamental_macro_analysis, concept_market_regimes]}
  - {rank: 75, id: book_most_important_thing, title: "The Most Important Thing", authors: [person_howard_marks], author: "Howard Marks", year: 2011, category: macro,
     key_idea: "Second-level thinking, risk, cycles, and contrarianism.",
     covers: [concept_market_sentiment, concept_market_regimes]}
  - {rank: 76, id: book_mastering_market_cycle, title: "Mastering the Market Cycle", authors: [person_howard_marks], author: "Howard Marks", year: 2018, category: macro, derived_from: [book_most_important_thing],
     key_idea: "Recognise where we are in economic, credit, and psychological cycles.",
     covers: [concept_market_regimes, concept_market_sentiment, concept_reflexivity]}
  - {rank: 77, id: book_pit_bull, title: "Pit Bull", authors: [person_martin_schwartz], author: "Martin Schwartz", year: 1998, category: interviews,
     key_idea: "A champion trader's memoir: moving averages, preparation, and emotional cost.",
     covers: [concept_moving_averages, concept_trading_psychology]}
  - {rank: 78, id: book_trader_vic, title: "Trader Vic: Methods of a Wall Street Master", authors: [person_victor_sperandeo], author: "Victor Sperandeo", year: 1991, category: technical_analysis, derived_from: [book_dow_theory_rhea],
     key_idea: "Dow Theory made practical; the 1-2-3 trend-change rule; risk-first speculation.",
     covers: [concept_dow_theory, concept_market_structure]}
  - {rank: 79, id: book_battle_for_investment_survival, title: "The Battle for Investment Survival", authors: [person_gerald_loeb], author: "Gerald M. Loeb", year: 1935, category: classics,
     key_idea: "Concentrate, cut losses, and treat speculation as a battle requiring constant attention.",
     covers: [concept_trade_management, concept_trading_psychology]}
  - {rank: 80, id: book_extraordinary_popular_delusions, title: "Extraordinary Popular Delusions and the Madness of Crowds", authors: [person_charles_mackay], author: "Charles Mackay", year: 1841, category: classics,
     key_idea: "Tulip mania, the South Sea Bubble, and crowd manias.",
     covers: [concept_market_sentiment, concept_reflexivity]}
  - {rank: 81, id: book_art_of_contrary_thinking, title: "The Art of Contrary Thinking", authors: [person_humphrey_neill], author: "Humphrey B. Neill", year: 1954, category: classics,
     key_idea: "When everyone thinks alike, everyone is likely to be wrong.",
     covers: [concept_market_sentiment]}
  - {rank: 82, id: book_dow_theory_rhea, title: "The Dow Theory", authors: [person_robert_rhea], author: "Robert Rhea", year: 1932, category: classics,
     key_idea: "Formal statement of Dow's tenets from Dow's and Hamilton's editorials.",
     covers: [concept_dow_theory, concept_market_structure, concept_trend_following]}
  - {rank: 83, id: book_beat_the_dealer, title: "Beat the Dealer", authors: [person_ed_thorp], author: "Edward O. Thorp", year: 1962, category: risk_money_management,
     key_idea: "Card counting proved a measurable edge exists; bet size proportional to edge.",
     covers: [concept_edge, concept_kelly_criterion_optimal_f]}
  - {rank: 84, id: book_fortunes_formula, title: "Fortune's Formula", authors: [person_william_poundstone], author: "William Poundstone", year: 2005, category: risk_money_management, features: [person_john_kelly, person_claude_shannon, person_ed_thorp],
     key_idea: "History of the Kelly criterion from Bell Labs to Vegas to Wall Street.",
     covers: [concept_kelly_criterion_optimal_f, concept_position_sizing]}
  - {rank: 85, id: book_against_the_gods, title: "Against the Gods", authors: [person_peter_bernstein], author: "Peter L. Bernstein", year: 1996, category: randomness_risk,
     key_idea: "The history of risk and probability from Pascal to modern finance.",
     covers: [concept_probability_fat_tails, concept_probabilistic_thinking]}
  - {rank: 86, id: book_random_walk_down_wall_street, title: "A Random Walk Down Wall Street", authors: [person_burton_malkiel], author: "Burton G. Malkiel", year: 1973, category: randomness_risk,
     key_idea: "The case for market efficiency and passive investing.",
     covers: [concept_random_walk_efficient_markets]}
  - {rank: 87, id: book_non_random_walk, title: "A Non-Random Walk Down Wall Street", authors: [person_andrew_lo, person_craig_mackinlay], author: "Andrew W. Lo & A. Craig MacKinlay", year: 1999, category: quant_algorithmic,
     key_idea: "Variance-ratio tests reject the random walk; markets have predictable components.",
     covers: [concept_random_walk_efficient_markets, concept_time_series_statistics]}
  - {rank: 88, id: book_adaptive_markets, title: "Adaptive Markets", authors: [person_andrew_lo], author: "Andrew W. Lo", year: 2017, category: randomness_risk, derived_from: [book_non_random_walk],
     key_idea: "Market efficiency is an evolving, ecological property; edges appear and decay.",
     covers: [concept_random_walk_efficient_markets, concept_market_regimes, concept_edge]}
  - {rank: 89, id: book_definitive_guide_position_sizing, title: "The Definitive Guide to Position Sizing", authors: [person_van_tharp], author: "Van K. Tharp", year: 2008, category: risk_money_management, derived_from: [book_trade_your_way_financial_freedom],
     key_idea: "Position sizing strategies to meet objectives; SQN and R-multiple simulation.",
     covers: [concept_position_sizing, concept_expectancy, concept_risk_of_ruin_drawdown]}
  - {rank: 90, id: book_trading_sardines, title: "Trading Sardines", authors: [person_linda_raschke], author: "Linda Bradford Raschke", year: 2019, category: interviews,
     key_idea: "A lifelong trader's memoir of markets, setups, and resilience.",
     covers: [concept_trading_psychology, concept_price_action]}
  - {rank: 91, id: book_crabel_opening_range, title: "Day Trading with Short Term Price Patterns and Opening Range Breakout", authors: [person_toby_crabel], author: "Toby Crabel", year: 1990, category: price_action,
     key_idea: "Opening range breakouts and narrow-range (NR4/NR7) volatility contraction patterns.",
     covers: [concept_breakout_trading, concept_volatility, concept_trading_sessions_killzones]}
  - {rank: 92, id: book_ta_multiple_timeframes, title: "Technical Analysis Using Multiple Timeframes", authors: [person_brian_shannon], author: "Brian Shannon", year: 2008, category: technical_analysis,
     key_idea: "Align timeframes; stages, moving averages, and VWAP for swing and day traders.",
     covers: [concept_multi_timeframe_analysis, concept_vwap, concept_moving_averages]}
  - {rank: 93, id: book_zurich_axioms, title: "The Zurich Axioms", authors: [person_max_gunther], author: "Max Gunther", year: 1985, category: classics,
     key_idea: "Twelve speculator's axioms: always bet meaningfully, take profits early, flee a sinking ship.",
     covers: [concept_trading_psychology, concept_trade_management]}
  - {rank: 94, id: book_customers_yachts, title: "Where Are the Customers' Yachts?", authors: [person_fred_schwed], author: "Fred Schwed Jr.", year: 1940, category: classics,
     key_idea: "A satire of Wall Street forecasting and incentives.",
     covers: [concept_random_walk_efficient_markets, concept_market_sentiment]}
  - {rank: 95, id: book_markets_and_market_logic, title: "Markets and Market Logic", authors: [person_peter_steidlmayer, person_kevin_koy], author: "J. Peter Steidlmayer & Kevin Koy", year: 1986, category: auction_market_theory,
     key_idea: "The original Market Profile text: the market as a self-organising auction of price, time, and value.",
     covers: [concept_auction_market_theory, concept_volume_profile]}
  - {rank: 96, id: book_one_up_on_wall_street, title: "One Up on Wall Street", authors: [person_peter_lynch], author: "Peter Lynch", year: 1989, category: macro,
     key_idea: "Invest in what you know; classify growth stories (fast growers, turnarounds, cyclicals).",
     covers: [concept_growth_momentum_canslim, concept_fundamental_macro_analysis]}
  - {rank: 97, id: book_antifragile, title: "Antifragile", authors: [person_nassim_taleb], author: "Nassim Nicholas Taleb", year: 2012, category: randomness_risk, derived_from: [book_black_swan],
     key_idea: "Seek convex payoffs that gain from volatility; barbell strategies.",
     covers: [concept_probability_fat_tails, concept_options_greeks]}
  - {rank: 98, id: book_hour_between_dog_wolf, title: "The Hour Between Dog and Wolf", authors: [person_john_coates], author: "John Coates", year: 2012, category: psychology,
     key_idea: "Trader physiology: testosterone and cortisol drive risk-taking cycles.",
     covers: [concept_trading_psychology]}
  - {rank: 99, id: book_market_microstructure_in_practice, title: "Market Microstructure in Practice", authors: [person_charles_albert_lehalle, person_sophie_laruelle], author: "Charles-Albert Lehalle & Sophie Laruelle (eds.)", year: 2013, category: microstructure_execution,
     key_idea: "Fragmentation after Reg NMS/MiFID, liquidity dynamics, and execution practice.",
     covers: [concept_market_microstructure, concept_optimal_execution_market_impact]}
  - {rank: 100, id: book_flash_boys, title: "Flash Boys", authors: [person_michael_lewis], author: "Michael Lewis", year: 2014, category: microstructure_execution,
     key_idea: "HFT, latency arbitrage, and how market structure can disadvantage slower orders.",
     covers: [concept_market_microstructure, concept_optimal_execution_market_impact]}
```


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/advances-financial-machine-learning.md ===== -->

---
id: book_advances_financial_ml
type: book
title: "Advances in Financial Machine Learning (López de Prado, 2018) — summary"
partition: 05_books-top-100
layer: L8
status: synthesized
---

# Advances in Financial Machine Learning — summary

See [[concept_machine_learning_finance]] and [[concept_overfitting_validation]].

| Part | Key tools |
|---|---|
| Data analysis | Dollar/volume/imbalance bars; fractional differentiation; CUSUM event sampling |
| Modelling | Triple-barrier labeling; **meta-labeling**; sample weights for overlapping labels; sequential bootstrap |
| Backtesting | Purged and embargoed CV; combinatorial purged CV; dangers of backtesting; synthetic data |
| Useful features | Structural breaks, entropy, microstructural features |
| HPC | Parallelisation recipes |

**Most transferable idea for discretionary traders:** meta-labeling. Keep
your setup as the "primary model" and learn *when to take it and how big*.


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/alchemy-of-finance.md ===== -->

---
id: book_alchemy_of_finance
type: book
title: "The Alchemy of Finance (Soros, 1987) — summary"
partition: 05_books-top-100
layer: L3
status: synthesized
---

# The Alchemy of Finance — summary

- **Reflexivity** as a theory of history and markets
  ([[concept_reflexivity]]).
- **Boom-bust model** with case studies: conglomerates, REITs,
  international lending, the "imperial circle" of 1980s US deficits and
  the dollar.
- **The real-time experiment:** a trading diary from 1985–86 in which Soros
  records his hypotheses, positions, and changes of mind. It is rare
  first-person documentation of macro decision-making
  ([[concept_trading_journal_review]]).
- **Fallibility as method:** form a hypothesis, invest on it, look for what
  is wrong ([[concept_probabilistic_thinking]]).


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/best-loser-wins.md ===== -->

---
id: book_best_loser_wins
type: book
title: "Best Loser Wins (Hougaard, 2022) — summary"
partition: 05_books-top-100
layer: L7
status: synthesized
---

# Best Loser Wins — summary

- **The edge is behavioural.** Most traders know the rules; few execute them
  because the brain resists doing so ([[concept_trading_psychology]]).
- **Lose well:** take small losses instantly and without drama
  ([[concept_trade_management]]).
- **Add to winners, not losers.** It is uncomfortable by design, and that
  discomfort is why it works ([[concept_trend_following]]).
- **Train the mind like an athlete:** awareness of impulses, deliberate
  practice, and accepting being wrong many times.
- Builds on Douglas's probabilistic mindset ([[concept_probabilistic_thinking]]).


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/fooled-by-randomness.md ===== -->

---
id: book_fooled_by_randomness
type: book
title: "Fooled by Randomness (Taleb, 2001) — summary"
partition: 05_books-top-100
layer: L0
status: synthesized
---

# Fooled by Randomness — summary

- **Survivorship bias:** we see the winners of a lottery and call it skill
  ([[concept_overfitting_validation]]).
- **Alternative histories:** judge a decision by the distribution of
  outcomes it could have produced ([[concept_probabilistic_thinking]]).
- **Asymmetry:** frequency of wins vs magnitude. A strategy can win often and
  still be a loser ([[concept_expectancy]]).
- **Rare events** dominate long-run outcomes. Strategies that sell tail risk
  blow up ([[concept_probability_fat_tails]]).
- **Noise vs signal:** looking at P&L too frequently mostly shows noise
  ([[concept_trading_psychology]]).


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/how-to-make-money-in-stocks.md ===== -->

---
id: book_how_to_make_money_in_stocks
type: book
title: "How to Make Money in Stocks (O'Neil, 1988) — summary"
partition: 05_books-top-100
layer: L4
status: synthesized
---

# How to Make Money in Stocks — summary

- Built from O'Neil's **study of the biggest winning stocks** and their
  characteristics before their major moves.
- **CANSLIM** criteria ([[concept_growth_momentum_canslim]]).
- **Chart bases:** cup-with-handle, double bottom, flat base; buy at the
  **pivot** on volume ([[concept_breakout_trading]]).
- **Sell rules:** cut every loss at **7–8%** without exception; take many
  gains at 20–25%, but hold the strongest leaders longer
  ([[concept_trade_management]]).
- **M = market direction:** three of four stocks follow the general market.
  Use follow-through days and distribution days to gauge it
  ([[concept_market_regimes]]).


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/market-wizards.md ===== -->

---
id: book_market_wizards
type: book
title: "Market Wizards (Schwager, 1989) — synthesis of lessons"
partition: 05_books-top-100
layer: L7
status: synthesized
---

# Market Wizards — what the wizards share

Interviews include Michael Marcus, Bruce Kovner, Richard Dennis, Paul Tudor
Jones, Ed Seykota, Larry Hite, William O'Neil, Marty Schwartz, and Van Tharp.

| Lesson | Who exemplifies it | Concept |
|---|---|---|
| Methods differ wildly; risk control does not | All | [[concept_edge]] |
| Your method must fit your personality | Seykota, Tharp | [[concept_trading_plan]] |
| Never risk more than a small % per trade | Hite, Dennis | [[concept_position_sizing]] |
| Defense first; size down when trading poorly | PTJ | [[concept_risk_of_ruin_drawdown]] |
| Follow the trend; let profits run | Dennis, Seykota | [[concept_trend_following]] |
| Fundamentals tell you *why*, technicals tell you *when* | Kovner, Marcus | [[concept_fundamental_macro_analysis]] |
| Losses are part of the process; emotional discipline is the edge | Schwartz, Seykota | [[concept_trading_psychology]] |
| Mentorship accelerates learning | Marcus (Seykota), Kovner (Marcus), PTJ (Tullis) | — |

**Follow-ups:** *The New Market Wizards* (1992: Druckenmiller, Raschke,
Eckhardt, Basso), *Stock Market Wizards* (2001: Minervini), *Hedge Fund
Market Wizards* (2012: Thorp, Dalio), *Unknown Market Wizards* (2020).


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/mind-over-markets.md ===== -->

---
id: book_mind_over_markets
type: book
title: "Mind Over Markets (Dalton, Jones & Dalton, 1990) — summary"
partition: 05_books-top-100
layer: L1
status: synthesized
---

# Mind Over Markets — summary

The canonical applied text for **Market Profile and auction market theory**,
building on Steidlmayer's *Markets and Market Logic* (1986).

- **Market purpose:** facilitate trade. Price advertises, time regulates,
  volume measures acceptance ([[concept_auction_market_theory]]).
- **Timeframes:** distinguish the *day timeframe* trader from the *other
  timeframe* (OTF) participant, the large player whose activity moves value.
- **Day types:** normal, normal variation, trend, double-distribution trend,
  neutral, non-trend. Each implies different tactics
  ([[concept_market_regimes]]).
- **Initiative vs responsive activity** at value extremes
  ([[concept_order_flow]]).
- **Structure tools:** value area, POC, initial balance, range extension,
  excess (tails), poor highs/lows ([[concept_volume_profile]]).
- **Longer-term:** value-area migration reveals trend, while overlapping
  value reveals balance.

**Descendants:** *Markets in Profile* (2007); modern volume-profile and
order-flow trading; the Chart Fanatics AMT guests (Fabio Valentini, Andrea
Cimitan, Rajan Dhall, Forrest Knight).


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/reminiscences-of-a-stock-operator.md ===== -->

---
id: book_reminiscences_stock_operator
type: book
title: "Reminiscences of a Stock Operator (Lefèvre, 1923) — summary"
partition: 05_books-top-100
layer: L7
status: synthesized
---

# Reminiscences of a Stock Operator — key lessons

A thinly fictionalised biography of Jesse Livermore ("Larry Livingston").

1. **The market is never wrong; opinions are.** Price is the arbiter
   ([[concept_trend_following]]).
2. **The big money is made by sitting, not by trading.** Livermore made his
   fortunes by being right *and sitting tight* through major moves
   ([[concept_trade_management]]).
3. **Line of least resistance:** trade in the direction the market is already
   moving most easily, once it is confirmed ([[concept_market_structure]]).
4. **Cut losses, never average down** a losing position
   ([[concept_risk_of_ruin_drawdown]]).
5. **Tips and hope are poison.** Livermore lost repeatedly when he traded on
   others' information or out of hope and fear ([[concept_trading_psychology]]).
6. **Bucket shops vs real markets:** his early edge (tape reading in bucket
   shops) failed when execution changed in real exchanges. It is an early
   lesson in microstructure and execution ([[concept_trade_execution]]).
7. **Human nature doesn't change,** so markets repeat
   ([[concept_market_sentiment]]).

**Lineage:** → Wyckoff studied Livermore → Darvas, O'Neil, Minervini cite him
→ trend following.


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/technical-analysis-financial-markets.md ===== -->

---
id: book_ta_financial_markets
type: book
title: "Technical Analysis of the Financial Markets (Murphy, 1999) — summary"
partition: 05_books-top-100
layer: L3
status: synthesized
---

# Technical Analysis of the Financial Markets — summary

The CMT-style reference; it largely overlaps BabyPips Elementary to Middle
School, at greater depth.

- **Philosophy:** market action discounts everything; prices move in trends;
  history repeats ([[concept_dow_theory]]).
- **Trend concepts:** S/R, trendlines, channels, retracements
  ([[concept_support_resistance]], [[concept_trendlines]], [[concept_fibonacci]]).
- **Patterns:** reversal and continuation ([[concept_chart_patterns]]).
- **Volume and open interest** in futures.
- **Moving averages and oscillators** ([[concept_moving_averages]],
  [[concept_oscillators_momentum]]).
- **Point & figure, Japanese candlesticks, Elliott, time cycles**
  ([[concept_candlestick_patterns]], [[concept_elliott_wave]]).
- **Intermarket analysis** ([[concept_intermarket_analysis]]).


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/trade-your-way-to-financial-freedom.md ===== -->

---
id: book_trade_your_way_financial_freedom
type: book
title: "Trade Your Way to Financial Freedom (Tharp, 1998) — summary"
partition: 05_books-top-100
layer: L6
status: synthesized
---

# Trade Your Way to Financial Freedom — summary

1. **The Holy Grail is you.** Design a system that fits your beliefs and
   objectives ([[concept_trading_plan]]).
2. **R-multiples:** express every trade as a multiple of initial risk
   ([[concept_risk_reward_r_multiples]]).
3. **Expectancy** (mean R) × opportunity = performance
   ([[concept_expectancy]]).
4. **Entries are overrated.** Tharp's random-entry experiments with good
   exits and sizing can still be profitable. Exits and **position sizing**
   drive results ([[concept_position_sizing]]).
5. **Position sizing models** (units per fixed $, equity %, percent risk,
   percent volatility) are tools to reach objectives.
6. Later: **SQN** as a system-quality score ([[concept_performance_metrics]]).


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/trading-and-exchanges.md ===== -->

---
id: book_trading_and_exchanges
type: book
title: "Trading and Exchanges (Harris, 2003) — summary"
partition: 05_books-top-100
layer: L1
status: synthesized
---

# Trading and Exchanges — summary

- **Who trades and why:** informed traders, liquidity providers (dealers,
  limit-order traders), utilitarian traders (hedgers, investors), and
  parasitic traders (front-runners, order anticipators)
  ([[concept_market_microstructure]]).
- **Order types and market structures:** quote-driven vs order-driven,
  auctions, brokered markets ([[concept_trade_execution]]).
- **Liquidity:** immediacy, width, depth, resiliency
  ([[concept_liquidity]]).
- **Bid-ask spread components:** order processing, inventory, adverse
  selection.
- **Transaction-cost measurement** and the zero-sum nature of short-term
  trading after costs ([[concept_optimal_execution_market_impact]]).
- **Why it matters for discretionary traders:** it explains *who your
  counterparty is* and why stop clusters, levels, and sessions behave as
  they do.


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/trading-in-the-zone.md ===== -->

---
id: book_trading_in_the_zone
type: book
title: "Trading in the Zone (Douglas, 2000) — summary"
partition: 05_books-top-100
layer: L7
status: synthesized
---

# Trading in the Zone — summary

**Thesis:** inconsistency comes from beliefs about risk, not from a lack of
analysis. The trader must operate from a *probabilistic mindset*.

- **Five fundamental truths** (paraphrased in [[concept_probabilistic_thinking]]).
- **Seven principles of consistency:** objectively identify edges;
  predefine risk; completely accept risk; act without hesitation; pay
  yourself as the market makes money available; continually monitor errors;
  never violate these principles.
- **Fear is a misperception of risk.** If the loss is accepted beforehand,
  there is nothing to fear in the moment ([[concept_trading_psychology]]).
- **The 20-trade sample exercise:** execute a defined edge 20 times exactly
  to experience the distribution. It is the psychological counterpart of
  [[concept_expectancy]].

Most frequently cited trading-psychology book among professional traders
(Tradezella).


<!-- ===== FILE: trading-intelligence/05_books-top-100/summaries/way-of-the-turtle.md ===== -->

---
id: book_way_of_the_turtle
type: book
title: "Way of the Turtle (Faith, 2007) — summary"
partition: 05_books-top-100
layer: L4
status: synthesized
---

# Way of the Turtle — summary

**The experiment (1983–84):** Richard Dennis and William Eckhardt recruited
novices, taught them a rule set in two weeks, and funded them. Many became
highly profitable, which settled their bet that trading can be taught.

## The rules in brief

| Component | Rule |
|---|---|
| Markets | Liquid futures: bonds, FX, metals, energy, softs, indices |
| Volatility unit | **N** = 20-day ATR ([[concept_volatility]]) |
| Position size | 1 unit = 1% of equity per 1 N move ([[concept_position_sizing]]) |
| Entry | System 1: 20-day breakout (skip if the last breakout was a winner); System 2: 55-day breakout ([[concept_breakout_trading]]) |
| Pyramiding | Add a unit every ½ N, up to 4 units |
| Stop | 2 N from entry |
| Exit | System 1: 10-day opposite breakout; System 2: 20-day |
| Limits | Max units per market, correlated group, and direction ([[concept_correlation_portfolio_risk]]) |

**Faith's emphasis:** the rules were simple. Most Turtles who failed did so
psychologically, by not taking every signal and so destroying the
distribution ([[concept_trading_psychology]]).


<!-- ===== FILE: trading-intelligence/05_books-top-100/top-100-trading-books.md ===== -->

<!-- generated by tools/render_registries.py from the YAML registries; do not edit by hand -->

# Top 100 Trading Books

Ranking method: see the header of `books.yaml`. Each row links to concept ids in `07_concepts/`; *Builds on* shows the book-to-book lineage.

| # | Title | Author | Year | Category | Key idea | Builds on | Concepts |
|---|---|---|---|---|---|---|---|
| 1 | **Reminiscences of a Stock Operator** | Edwin Lefèvre | 1923 | classics | Fictionalised Livermore: the market is never wrong, cut losses, sit tight in big moves, follow the line of least resistance. |  | `concept_trend_following`, `concept_trading_psychology`, `concept_trade_management`, `concept_market_sentiment` |
| 2 | **Market Wizards** | Jack D. Schwager | 1989 | interviews | Top traders share no single method but universally share risk control, discipline, and a method that fits their personality. |  | `concept_edge`, `concept_trading_psychology`, `concept_risk_of_ruin_drawdown`, `concept_trend_following` |
| 3 | **Trading in the Zone** | Mark Douglas | 2000 | psychology | Consistency comes from thinking in probabilities and fully accepting risk before each trade (the five fundamental truths). | The Disciplined Trader | `concept_probabilistic_thinking`, `concept_trading_psychology`, `concept_edge` |
| 4 | **Technical Analysis of the Financial Markets** | John J. Murphy | 1999 | technical_analysis | The standard reference for chart construction, trend, patterns, indicators, and intermarket principles. | Technical Analysis of Stock Trends, The Dow Theory | `concept_chart_patterns`, `concept_support_resistance`, `concept_moving_averages`, `concept_oscillators_momentum`, `concept_dow_theory`, `concept_intermarket_analysis` |
| 5 | **The New Market Wizards** | Jack D. Schwager | 1992 | interviews | Second round of interviews: macro, systematic, and psychology lessons (Eckhardt, Druckenmiller, Raschke, Basso). | Market Wizards | `concept_edge`, `concept_position_sizing`, `concept_trading_psychology` |
| 6 | **How to Make Money in Stocks** | William J. O'Neil | 1988 | growth_momentum | CANSLIM: buy leading growth stocks breaking out of proper bases in a confirmed uptrend; cut losses at 7–8%. | How to Trade in Stocks, The Battle for Investment Survival | `concept_growth_momentum_canslim`, `concept_breakout_trading`, `concept_trade_management` |
| 7 | **Trade Like a Stock Market Wizard** | Mark Minervini | 2013 | growth_momentum | SEPA: trend template, earnings catalysts, and VCP entries with tight, predefined risk. | How to Make Money in Stocks, Secrets for Profiting in Bull and Bear Markets | `concept_growth_momentum_canslim`, `concept_position_sizing`, `concept_volatility` |
| 8 | **Technical Analysis of Stock Trends** | Robert D. Edwards & John Magee | 1948 | technical_analysis | The original catalogue of chart patterns and trendline/support-resistance analysis. | The Dow Theory | `concept_chart_patterns`, `concept_trendlines`, `concept_support_resistance`, `concept_dow_theory` |
| 9 | **Trade Your Way to Financial Freedom** | Van K. Tharp | 1998 | risk_money_management | Expectancy in R-multiples and position sizing, not entries, drive results; design a system that fits you. |  | `concept_expectancy`, `concept_position_sizing`, `concept_risk_reward_r_multiples`, `concept_trading_plan` |
| 10 | **Fooled by Randomness** | Nassim Nicholas Taleb | 2001 | randomness_risk | Survivorship bias and luck masquerade as skill; judge decisions by their alternative histories. |  | `concept_probability_fat_tails`, `concept_overfitting_validation`, `concept_probabilistic_thinking` |
| 11 | **The Alchemy of Finance** | George Soros | 1987 | macro | Reflexivity: perceptions change fundamentals, producing boom-bust sequences; includes a real-time trading diary. |  | `concept_reflexivity`, `concept_fundamental_macro_analysis`, `concept_market_sentiment` |
| 12 | **Trend Following** | Michael W. Covel | 2004 | trend_following | Price-based trend following with strict risk control is a durable, crisis-resilient strategy. |  | `concept_trend_following`, `concept_position_sizing` |
| 13 | **Way of the Turtle** | Curtis Faith | 2007 | trend_following | The Turtle rules (Donchian breakouts, N-based sizing) and why most people can't follow them. |  | `concept_trend_following`, `concept_position_sizing`, `concept_volatility`, `concept_breakout_trading` |
| 14 | **Japanese Candlestick Charting Techniques** | Steve Nison | 1991 | technical_analysis | Candlestick patterns as readings of crowd psychology, best combined with Western technicals. |  | `concept_candlestick_patterns`, `concept_price_action` |
| 15 | **Mind Over Markets** | James F. Dalton, Eric T. Jones & Robert B. Dalton | 1990 | auction_market_theory | Market Profile and auction market theory: value, day types, balance vs imbalance, and the auction's logic. | Markets and Market Logic | `concept_auction_market_theory`, `concept_volume_profile`, `concept_market_regimes` |
| 16 | **How to Trade in Stocks** | Jesse Livermore | 1940 | classics | Pivotal points, timing, pyramiding, and the Livermore market key. |  | `concept_trend_following`, `concept_breakout_trading`, `concept_trade_management` |
| 17 | **Trading for a Living** | Dr. Alexander Elder | 1993 | technical_analysis | The three Ms (mind, method, money); Triple Screen multi-timeframe system; the 2% and 6% rules. |  | `concept_multi_timeframe_analysis`, `concept_trading_psychology`, `concept_position_sizing`, `concept_oscillators_momentum` |
| 18 | **The Disciplined Trader** | Mark Douglas | 1990 | psychology | Mental frameworks are the bottleneck; traders must restructure beliefs about risk and being wrong. |  | `concept_trading_psychology` |
| 19 | **Best Loser Wins** | Tom Hougaard | 2022 | psychology | Winning traders are the best losers; train behaviour against instinct (add to winners, cut losers instantly). | Trading in the Zone | `concept_trading_psychology`, `concept_trade_management` |
| 20 | **A Man for All Markets** | Edward O. Thorp | 2017 | interviews | From card counting to hedge funds: measurable edge plus Kelly sizing plus risk discipline. | Beat the Dealer | `concept_edge`, `concept_kelly_criterion_optimal_f`, `concept_options_greeks` |
| 21 | **Principles** | Ray Dalio | 2017 | macro | Radical transparency, believability-weighted decisions, and systematising lessons from mistakes. |  | `concept_trading_journal_review`, `concept_correlation_portfolio_risk`, `concept_probabilistic_thinking` |
| 22 | **Reading Price Charts Bar by Bar** | Al Brooks | 2009 | price_action | Every bar tells who controls the market; trade two-legged pullbacks and failed breakouts in context. |  | `concept_price_action`, `concept_breakout_trading`, `concept_market_regimes` |
| 23 | **Street Smarts** | Linda Bradford Raschke & Laurence A. Connors | 1995 | price_action | Short-term setups including Turtle Soup (fading failed breakouts), the Holy Grail, and 80-20s. |  | `concept_liquidity_sweep_reversal`, `concept_breakout_trading`, `concept_mean_reversion` |
| 24 | **Option Volatility & Pricing** | Sheldon Natenberg | 1988 | options_volatility | Volatility is the key input; trade options as volatility positions managed through the Greeks. |  | `concept_options_greeks`, `concept_volatility` |
| 25 | **Trading and Exchanges** | Larry Harris | 2003 | microstructure_execution | Who trades, why, and how market structure, order types, and dealers shape prices and costs. |  | `concept_market_microstructure`, `concept_trade_execution`, `concept_liquidity` |
| 26 | **Evidence-Based Technical Analysis** | David Aronson | 2006 | quant_algorithmic | Apply the scientific method and data-snooping corrections; most TA rules fail rigorous testing. |  | `concept_overfitting_validation`, `concept_backtesting`, `concept_random_walk_efficient_markets` |
| 27 | **The Man Who Solved the Market** | Gregory Zuckerman | 2019 | interviews | How Renaissance Technologies used scientists, data, and small statistical edges at scale. |  | `concept_machine_learning_finance`, `concept_time_series_statistics`, `concept_edge` |
| 28 | **Stock Market Wizards** | Jack D. Schwager | 2001 | interviews | Equity-focused wizards; common thread of risk control and adaptability. | Market Wizards | `concept_growth_momentum_canslim`, `concept_edge` |
| 29 | **Hedge Fund Market Wizards** | Jack D. Schwager | 2012 | interviews | Hedge-fund managers on process, risk, and adaptation; Schwager's 40 lessons. | Market Wizards | `concept_correlation_portfolio_risk`, `concept_edge`, `concept_risk_of_ruin_drawdown` |
| 30 | **Unknown Market Wizards** | Jack D. Schwager | 2020 | interviews | Individual traders with extraordinary audited records; edge comes in many forms. | Market Wizards | `concept_edge`, `concept_trading_psychology` |
| 31 | **Diary of a Professional Commodity Trader** | Peter L. Brandt | 2011 | technical_analysis | Classical charting run as a business: trade logs, risk rules, and why most signals fail. | Technical Analysis of Stock Trends | `concept_chart_patterns`, `concept_risk_reward_r_multiples`, `concept_trading_journal_review` |
| 32 | **Secrets for Profiting in Bull and Bear Markets** | Stan Weinstein | 1988 | growth_momentum | Stage analysis with the 30-week MA: buy Stage 2 breakouts, avoid Stage 4. |  | `concept_growth_momentum_canslim`, `concept_moving_averages`, `concept_market_regimes` |
| 33 | **How I Made $2,000,000 in the Stock Market** | Nicolas Darvas | 1960 | classics | Box theory: buy breakouts of price boxes in stocks with rising earnings; use stop-loss orders. | The Battle for Investment Survival | `concept_breakout_trading`, `concept_growth_momentum_canslim` |
| 34 | **The Psychology of Trading** | Brett N. Steenbarger | 2003 | psychology | Brief-therapy techniques applied to trading: change patterns through structured self-observation. |  | `concept_trading_psychology`, `concept_trading_journal_review` |
| 35 | **The Mathematics of Money Management** | Ralph Vince | 1992 | risk_money_management | Optimal f and the geometry of position sizing; leverage drives both growth and ruin. |  | `concept_kelly_criterion_optimal_f`, `concept_position_sizing`, `concept_risk_of_ruin_drawdown` |
| 36 | **Long-Term Secrets to Short-Term Trading** | Larry Williams | 1999 | price_action | Short-term swings, volatility breakouts, and day-of-week/time patterns from a champion trader. |  | `concept_trading_sessions_killzones`, `concept_volatility`, `concept_breakout_trading` |
| 37 | **Markets in Profile** | James F. Dalton | 2007 | auction_market_theory | Market Profile meets behavioural finance across timeframes. | Mind Over Markets | `concept_auction_market_theory`, `concept_volume_profile`, `concept_market_sentiment` |
| 38 | **Trades About to Happen** | David H. Weis | 2013 | auction_market_theory | Modern Wyckoff: reading springs, upthrusts, and effort vs result on bar charts and Weis waves. | Studies in Tape Reading | `concept_wyckoff_method`, `concept_liquidity_sweep_reversal` |
| 39 | **Studies in Tape Reading** | Rollo Tape (Richard D. Wyckoff) | 1910 | classics | Reading the tape to infer the intentions of large operators: the root of order-flow analysis. |  | `concept_order_flow`, `concept_wyckoff_method` |
| 40 | **Tape Reading and Market Tactics** | Humphrey B. Neill | 1931 | classics | Volume and price behaviour reveal supply and demand; follow the tape, not opinions. | Studies in Tape Reading | `concept_order_flow`, `concept_market_sentiment` |
| 41 | **The Black Swan** | Nassim Nicholas Taleb | 2007 | randomness_risk | Rare, high-impact events dominate outcomes and are systematically underestimated. | Fooled by Randomness | `concept_probability_fat_tails`, `concept_risk_of_ruin_drawdown` |
| 42 | **The (Mis)Behavior of Markets** | Benoit Mandelbrot & Richard L. Hudson | 2004 | randomness_risk | Prices are fractal and fat-tailed; Gaussian finance underestimates risk. |  | `concept_probability_fat_tails`, `concept_random_walk_efficient_markets`, `concept_volatility` |
| 43 | **Thinking, Fast and Slow** | Daniel Kahneman | 2011 | psychology | System 1/System 2, heuristics and biases, prospect theory and loss aversion. |  | `concept_trading_psychology`, `concept_probabilistic_thinking` |
| 44 | **Thinking in Bets** | Annie Duke | 2018 | psychology | Separate decision quality from outcome; avoid 'resulting'. |  | `concept_probabilistic_thinking`, `concept_trading_journal_review` |
| 45 | **The Mental Game of Trading** | Jared Tendler | 2021 | psychology | Diagnose greed, fear, tilt, confidence, and discipline problems and fix their root flaws. |  | `concept_trading_psychology` |
| 46 | **The Daily Trading Coach** | Brett N. Steenbarger | 2009 | psychology | 101 lessons for becoming your own trading coach. | The Psychology of Trading | `concept_trading_psychology`, `concept_trading_journal_review` |
| 47 | **Encyclopedia of Chart Patterns** | Thomas N. Bulkowski | 2000 | technical_analysis | Statistical performance of dozens of chart patterns: failure rates, average moves, throwbacks. | Technical Analysis of Stock Trends | `concept_chart_patterns`, `concept_backtesting` |
| 48 | **Elliott Wave Principle** | A. J. Frost & Robert R. Prechter Jr. | 1978 | technical_analysis | Markets unfold in 5-3 wave patterns related by Fibonacci ratios. |  | `concept_elliott_wave`, `concept_fibonacci` |
| 49 | **Bollinger on Bollinger Bands** | John Bollinger | 2001 | technical_analysis | Relative definitions of high and low via volatility bands; squeezes and band walks. |  | `concept_bollinger_bands`, `concept_volatility` |
| 50 | **New Concepts in Technical Trading Systems** | J. Welles Wilder Jr. | 1978 | technical_analysis | Introduced RSI, ATR, ADX/DMI, and Parabolic SAR. |  | `concept_oscillators_momentum`, `concept_volatility`, `concept_market_regimes` |
| 51 | **Intermarket Analysis** | John J. Murphy | 2004 | macro | Bonds, stocks, commodities, and currencies move in linked cycles. |  | `concept_intermarket_analysis`, `concept_fundamental_macro_analysis` |
| 52 | **Technical Analysis Explained** | Martin J. Pring | 1980 | technical_analysis | Comprehensive TA with an emphasis on market cycles and momentum. |  | `concept_oscillators_momentum`, `concept_market_regimes`, `concept_chart_patterns` |
| 53 | **The Art and Science of Technical Analysis** | Adam Grimes | 2012 | technical_analysis | Statistically grounded price action: pullbacks, failure tests, and quantified edges. |  | `concept_price_action`, `concept_backtesting`, `concept_market_structure` |
| 54 | **Mastering the Trade** | John F. Carter | 2005 | price_action | Intraday and swing setups including the squeeze; psychology of the retail trader. |  | `concept_bollinger_bands`, `concept_breakout_trading`, `concept_trading_sessions_killzones` |
| 55 | **Think & Trade Like a Champion** | Mark Minervini | 2017 | growth_momentum | Risk management and process for super-performance: progressive exposure, selling rules. | Trade Like a Stock Market Wizard | `concept_position_sizing`, `concept_trade_management`, `concept_growth_momentum_canslim` |
| 56 | **The Complete TurtleTrader** | Michael W. Covel | 2007 | trend_following | History of the Turtle experiment and what happened to the Turtles. | Trend Following | `concept_trend_following` |
| 57 | **Following the Trend** | Andreas F. Clenow | 2012 | trend_following | A complete diversified futures trend-following model with year-by-year analysis. | Way of the Turtle | `concept_trend_following`, `concept_correlation_portfolio_risk` |
| 58 | **Systematic Trading** | Robert Carver | 2015 | quant_algorithmic | A framework for systematic rules, forecast scaling, volatility targeting, and avoiding overfitting. |  | `concept_position_sizing`, `concept_overfitting_validation`, `concept_trend_following`, `concept_volatility` |
| 59 | **Quantitative Trading** | Ernest P. Chan | 2008 | quant_algorithmic | Building and backtesting a retail quant business; Kelly sizing; pitfalls. |  | `concept_backtesting`, `concept_kelly_criterion_optimal_f`, `concept_mean_reversion` |
| 60 | **Algorithmic Trading: Winning Strategies and Their Rationale** | Ernest P. Chan | 2013 | quant_algorithmic | Mean-reversion (cointegration, pairs) and momentum strategies with statistical tests. | Quantitative Trading | `concept_mean_reversion`, `concept_time_series_statistics`, `concept_trend_following` |
| 61 | **Advances in Financial Machine Learning** | Marcos López de Prado | 2018 | quant_algorithmic | Information bars, triple-barrier labels, meta-labeling, purged CV, and backtest-overfitting statistics. |  | `concept_machine_learning_finance`, `concept_overfitting_validation`, `concept_backtesting` |
| 62 | **Inside the Black Box** | Rishi K. Narang | 2009 | quant_algorithmic | Anatomy of a quant strategy: alpha, risk, transaction cost, and portfolio construction models. |  | `concept_optimal_execution_market_impact`, `concept_edge` |
| 63 | **Building Winning Algorithmic Trading Systems** | Kevin J. Davey | 2014 | quant_algorithmic | A champion trader's process for developing, validating, and monitoring systems. |  | `concept_backtesting`, `concept_overfitting_validation` |
| 64 | **Trading Systems and Methods** | Perry J. Kaufman | 1978 | quant_algorithmic | Encyclopedic reference of trading systems, indicators, and testing methods. |  | `concept_trend_following`, `concept_backtesting`, `concept_market_regimes` |
| 65 | **Expected Returns** | Antti Ilmanen | 2011 | quant_algorithmic | A synthesis of risk premia: value, carry, momentum, volatility, and their evidence. |  | `concept_carry_trade`, `concept_trend_following`, `concept_edge` |
| 66 | **Efficiently Inefficient** | Lasse Heje Pedersen | 2015 | quant_algorithmic | Markets are efficiently inefficient: hedge-fund strategies exist because of costs and limits to arbitrage. |  | `concept_random_walk_efficient_markets`, `concept_trend_following`, `concept_carry_trade` |
| 67 | **Options as a Strategic Investment** | Lawrence G. McMillan | 1980 | options_volatility | The comprehensive reference on options strategies and their risks. |  | `concept_options_greeks` |
| 68 | **Dynamic Hedging** | Nassim Nicholas Taleb | 1997 | options_volatility | Practitioner's guide to managing vanilla and exotic option risk; tails and model risk. |  | `concept_options_greeks`, `concept_probability_fat_tails` |
| 69 | **Options, Futures, and Other Derivatives** | John C. Hull | 1989 | options_volatility | Standard textbook on derivatives pricing and hedging. |  | `concept_options_greeks`, `concept_stochastic_processes` |
| 70 | **Day Trading and Swing Trading the Currency Market** | Kathy Lien | 2008 | forex | FX-specific technical and fundamental strategies; session behaviour and macro drivers. |  | `concept_fundamental_macro_analysis`, `concept_trading_sessions_killzones`, `concept_carry_trade`, `concept_news_trading` |
| 71 | **Inside the House of Money** | Steven Drobny | 2006 | macro | Interviews with global macro managers on how they think and size trades. |  | `concept_fundamental_macro_analysis`, `concept_position_sizing` |
| 72 | **More Money Than God** | Sebastian Mallaby | 2010 | interviews | History of hedge funds: Jones, Soros, Robertson, Tudor Jones, Renaissance. |  | `concept_fundamental_macro_analysis`, `concept_reflexivity` |
| 73 | **When Genius Failed** | Roger Lowenstein | 2000 | randomness_risk | LTCM's collapse: leverage, correlation, and liquidity risk overwhelm brilliant models. |  | `concept_risk_of_ruin_drawdown`, `concept_correlation_portfolio_risk`, `concept_probability_fat_tails` |
| 74 | **Big Debt Crises** | Ray Dalio | 2018 | macro | A template for deflationary and inflationary debt crises with case studies. |  | `concept_fundamental_macro_analysis`, `concept_market_regimes` |
| 75 | **The Most Important Thing** | Howard Marks | 2011 | macro | Second-level thinking, risk, cycles, and contrarianism. |  | `concept_market_sentiment`, `concept_market_regimes` |
| 76 | **Mastering the Market Cycle** | Howard Marks | 2018 | macro | Recognise where we are in economic, credit, and psychological cycles. | The Most Important Thing | `concept_market_regimes`, `concept_market_sentiment`, `concept_reflexivity` |
| 77 | **Pit Bull** | Martin Schwartz | 1998 | interviews | A champion trader's memoir: moving averages, preparation, and emotional cost. |  | `concept_moving_averages`, `concept_trading_psychology` |
| 78 | **Trader Vic: Methods of a Wall Street Master** | Victor Sperandeo | 1991 | technical_analysis | Dow Theory made practical; the 1-2-3 trend-change rule; risk-first speculation. | The Dow Theory | `concept_dow_theory`, `concept_market_structure` |
| 79 | **The Battle for Investment Survival** | Gerald M. Loeb | 1935 | classics | Concentrate, cut losses, and treat speculation as a battle requiring constant attention. |  | `concept_trade_management`, `concept_trading_psychology` |
| 80 | **Extraordinary Popular Delusions and the Madness of Crowds** | Charles Mackay | 1841 | classics | Tulip mania, the South Sea Bubble, and crowd manias. |  | `concept_market_sentiment`, `concept_reflexivity` |
| 81 | **The Art of Contrary Thinking** | Humphrey B. Neill | 1954 | classics | When everyone thinks alike, everyone is likely to be wrong. |  | `concept_market_sentiment` |
| 82 | **The Dow Theory** | Robert Rhea | 1932 | classics | Formal statement of Dow's tenets from Dow's and Hamilton's editorials. |  | `concept_dow_theory`, `concept_market_structure`, `concept_trend_following` |
| 83 | **Beat the Dealer** | Edward O. Thorp | 1962 | risk_money_management | Card counting proved a measurable edge exists; bet size proportional to edge. |  | `concept_edge`, `concept_kelly_criterion_optimal_f` |
| 84 | **Fortune's Formula** | William Poundstone | 2005 | risk_money_management | History of the Kelly criterion from Bell Labs to Vegas to Wall Street. |  | `concept_kelly_criterion_optimal_f`, `concept_position_sizing` |
| 85 | **Against the Gods** | Peter L. Bernstein | 1996 | randomness_risk | The history of risk and probability from Pascal to modern finance. |  | `concept_probability_fat_tails`, `concept_probabilistic_thinking` |
| 86 | **A Random Walk Down Wall Street** | Burton G. Malkiel | 1973 | randomness_risk | The case for market efficiency and passive investing. |  | `concept_random_walk_efficient_markets` |
| 87 | **A Non-Random Walk Down Wall Street** | Andrew W. Lo & A. Craig MacKinlay | 1999 | quant_algorithmic | Variance-ratio tests reject the random walk; markets have predictable components. |  | `concept_random_walk_efficient_markets`, `concept_time_series_statistics` |
| 88 | **Adaptive Markets** | Andrew W. Lo | 2017 | randomness_risk | Market efficiency is an evolving, ecological property; edges appear and decay. | A Non-Random Walk Down Wall Street | `concept_random_walk_efficient_markets`, `concept_market_regimes`, `concept_edge` |
| 89 | **The Definitive Guide to Position Sizing** | Van K. Tharp | 2008 | risk_money_management | Position sizing strategies to meet objectives; SQN and R-multiple simulation. | Trade Your Way to Financial Freedom | `concept_position_sizing`, `concept_expectancy`, `concept_risk_of_ruin_drawdown` |
| 90 | **Trading Sardines** | Linda Bradford Raschke | 2019 | interviews | A lifelong trader's memoir of markets, setups, and resilience. |  | `concept_trading_psychology`, `concept_price_action` |
| 91 | **Day Trading with Short Term Price Patterns and Opening Range Breakout** | Toby Crabel | 1990 | price_action | Opening range breakouts and narrow-range (NR4/NR7) volatility contraction patterns. |  | `concept_breakout_trading`, `concept_volatility`, `concept_trading_sessions_killzones` |
| 92 | **Technical Analysis Using Multiple Timeframes** | Brian Shannon | 2008 | technical_analysis | Align timeframes; stages, moving averages, and VWAP for swing and day traders. |  | `concept_multi_timeframe_analysis`, `concept_vwap`, `concept_moving_averages` |
| 93 | **The Zurich Axioms** | Max Gunther | 1985 | classics | Twelve speculator's axioms: always bet meaningfully, take profits early, flee a sinking ship. |  | `concept_trading_psychology`, `concept_trade_management` |
| 94 | **Where Are the Customers' Yachts?** | Fred Schwed Jr. | 1940 | classics | A satire of Wall Street forecasting and incentives. |  | `concept_random_walk_efficient_markets`, `concept_market_sentiment` |
| 95 | **Markets and Market Logic** | J. Peter Steidlmayer & Kevin Koy | 1986 | auction_market_theory | The original Market Profile text: the market as a self-organising auction of price, time, and value. |  | `concept_auction_market_theory`, `concept_volume_profile` |
| 96 | **One Up on Wall Street** | Peter Lynch | 1989 | macro | Invest in what you know; classify growth stories (fast growers, turnarounds, cyclicals). |  | `concept_growth_momentum_canslim`, `concept_fundamental_macro_analysis` |
| 97 | **Antifragile** | Nassim Nicholas Taleb | 2012 | randomness_risk | Seek convex payoffs that gain from volatility; barbell strategies. | The Black Swan | `concept_probability_fat_tails`, `concept_options_greeks` |
| 98 | **The Hour Between Dog and Wolf** | John Coates | 2012 | psychology | Trader physiology: testosterone and cortisol drive risk-taking cycles. |  | `concept_trading_psychology` |
| 99 | **Market Microstructure in Practice** | Charles-Albert Lehalle & Sophie Laruelle (eds.) | 2013 | microstructure_execution | Fragmentation after Reg NMS/MiFID, liquidity dynamics, and execution practice. |  | `concept_market_microstructure`, `concept_optimal_execution_market_impact` |
| 100 | **Flash Boys** | Michael Lewis | 2014 | microstructure_execution | HFT, latency arbitrage, and how market structure can disadvantage slower orders. |  | `concept_market_microstructure`, `concept_optimal_execution_market_impact` |

## By category

| Category | Count | Titles |
|---|---|---|
| technical_analysis | 13 | Technical Analysis of the Financial Markets; Technical Analysis of Stock Trends; Japanese Candlestick Charting Techniques; Trading for a Living; Diary of a Professional Commodity Trader; Encyclopedia of Chart Patterns; Elliott Wave Principle; Bollinger on Bollinger Bands; New Concepts in Technical Trading Systems; Technical Analysis Explained; The Art and Science of Technical Analysis; Trader Vic: Methods of a Wall Street Master; Technical Analysis Using Multiple Timeframes |
| classics | 11 | Reminiscences of a Stock Operator; How to Trade in Stocks; How I Made $2,000,000 in the Stock Market; Studies in Tape Reading; Tape Reading and Market Tactics; The Battle for Investment Survival; Extraordinary Popular Delusions and the Madness of Crowds; The Art of Contrary Thinking; The Dow Theory; The Zurich Axioms; Where Are the Customers' Yachts? |
| quant_algorithmic | 11 | Evidence-Based Technical Analysis; Systematic Trading; Quantitative Trading; Algorithmic Trading: Winning Strategies and Their Rationale; Advances in Financial Machine Learning; Inside the Black Box; Building Winning Algorithmic Trading Systems; Trading Systems and Methods; Expected Returns; Efficiently Inefficient; A Non-Random Walk Down Wall Street |
| interviews | 10 | Market Wizards; The New Market Wizards; A Man for All Markets; The Man Who Solved the Market; Stock Market Wizards; Hedge Fund Market Wizards; Unknown Market Wizards; More Money Than God; Pit Bull; Trading Sardines |
| psychology | 9 | Trading in the Zone; The Disciplined Trader; Best Loser Wins; The Psychology of Trading; Thinking, Fast and Slow; Thinking in Bets; The Mental Game of Trading; The Daily Trading Coach; The Hour Between Dog and Wolf |
| randomness_risk | 8 | Fooled by Randomness; The Black Swan; The (Mis)Behavior of Markets; When Genius Failed; Against the Gods; A Random Walk Down Wall Street; Adaptive Markets; Antifragile |
| macro | 8 | The Alchemy of Finance; Principles; Intermarket Analysis; Inside the House of Money; Big Debt Crises; The Most Important Thing; Mastering the Market Cycle; One Up on Wall Street |
| risk_money_management | 5 | Trade Your Way to Financial Freedom; The Mathematics of Money Management; Beat the Dealer; Fortune's Formula; The Definitive Guide to Position Sizing |
| price_action | 5 | Reading Price Charts Bar by Bar; Street Smarts; Long-Term Secrets to Short-Term Trading; Mastering the Trade; Day Trading with Short Term Price Patterns and Opening Range Breakout |
| growth_momentum | 4 | How to Make Money in Stocks; Trade Like a Stock Market Wizard; Secrets for Profiting in Bull and Bear Markets; Think & Trade Like a Champion |
| trend_following | 4 | Trend Following; Way of the Turtle; The Complete TurtleTrader; Following the Trend |
| auction_market_theory | 4 | Mind Over Markets; Markets in Profile; Trades About to Happen; Markets and Market Logic |
| options_volatility | 4 | Option Volatility & Pricing; Options as a Strategic Investment; Dynamic Hedging; Options, Futures, and Other Derivatives |
| microstructure_execution | 3 | Trading and Exchanges; Market Microstructure in Practice; Flash Boys |
| forex | 1 | Day Trading and Swing Trading the Currency Market |

## Most-covered concepts across the 100 books

| Concept | # books |
|---|---|
| Trading Psychology & Discipline (`concept_trading_psychology`) | 17 |
| Trend Following (`concept_trend_following`) | 13 |
| Edge (positive expectancy, repeatable) (`concept_edge`) | 12 |
| Position Sizing (`concept_position_sizing`) | 12 |
| Market Regimes (trend vs range, high vs low volatility) (`concept_market_regimes`) | 10 |
| Market Sentiment & Positioning (COT, contrarian signals) (`concept_market_sentiment`) | 9 |
| Breakout Trading (and fakeouts) (`concept_breakout_trading`) | 9 |
| Volatility (realized, implied, ATR, regimes) (`concept_volatility`) | 9 |
| Trade Management (stops, targets, breakeven, scaling, trailing) (`concept_trade_management`) | 7 |
| Growth-Stock Momentum (CANSLIM, SEPA, VCP) (`concept_growth_momentum_canslim`) | 7 |
| Probability, Distributions & Fat Tails (`concept_probability_fat_tails`) | 7 |
| Fundamental & Macro Analysis (rates, central banks, growth, inflation) (`concept_fundamental_macro_analysis`) | 7 |
| Backtesting (manual & systematic) (`concept_backtesting`) | 7 |
| Random Walk & Efficient Market Hypothesis (`concept_random_walk_efficient_markets`) | 7 |
| Risk of Ruin & Drawdown Math (`concept_risk_of_ruin_drawdown`) | 6 |
| Probabilistic Thinking (thinking in bets) (`concept_probabilistic_thinking`) | 6 |
| Options & the Greeks (`concept_options_greeks`) | 6 |
| Classical Chart Patterns (`concept_chart_patterns`) | 5 |
| Overfitting & Edge Validation (multiple testing, deflated Sharpe) (`concept_overfitting_validation`) | 5 |
| Kelly Criterion & Optimal f (`concept_kelly_criterion_optimal_f`) | 5 |
