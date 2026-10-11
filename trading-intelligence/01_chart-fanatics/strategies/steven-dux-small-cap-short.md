---
id: strategy_steven_dux_small_cap_short
type: strategy
title: "Steven Dux — Small-Cap Short Statistics Playbook (US small-cap stocks, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Small-Cap Short Statistics Playbook, Steven Dux small-cap short, Dux gap-up short, Dux bounce short, Dux first red day]
taught_by: [person_steven_dux]
featured_in: [channel_chart_fanatics]
uses: [concept_mean_reversion, concept_support_resistance, concept_volume_profile, concept_liquidity, concept_market_sentiment, concept_market_microstructure, concept_price_action, concept_trading_sessions_killzones, concept_position_sizing, concept_risk_reward_r_multiples, concept_trade_management, concept_performance_metrics, concept_probabilistic_thinking, concept_edge]
derived_from: [concept_mean_reversion, concept_market_sentiment]
related: [strategy_kyle_williams_first_red_day, strategy_alex_temiz_first_red_day, strategy_kris_verma_shorting, strategy_marios_stamatoudis_parabolic_short]
sources:
  - {title: "Chart Fanatics — Steven Dux - Small-Cap Short Statistics Playbook", url: "https://www.chartfanatics.com/strategies/small-cap-short-statistics", tier: T2}
status: verified-t2
---

# Steven Dux — Small-Cap Short Statistics Playbook (US small-cap stocks, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/small-cap-short-statistics. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook presents Steven Dux as a statistics-first short
seller of low-float US small-cap runners. He waits for the data to qualify a
setup before the chart pattern matters.

## Built for

- **Instruments:** the page header lists stocks and futures, but every rule
  and example concerns **US small-cap equities**: low market cap, low
  float, big percentage moves and heavy retail participation. It works best
  with borrow access.
- **Style:** short-biased day trading. Bounce shorts and first red days are
  next-day or multi-day setups; whether positions are held overnight is not
  specified in the playbook.
- **Timeframes:** the daily chart for history and multi-day runs, and 1-hour
  or 30-minute charts for volume-at-price context. Intraday execution charts
  are not named.
- **Time window:** gap-up shorts focus on **9:30 to 11:30 ET**, when much of
  the day's volume trades. The cleaner trigger comes at about **10:00 to
  11:00**.
- **Tools and level:** a scanner, float and market-cap data, pre-market and
  intraday volume, and a way to estimate full-day volume. The page says it
  is **not a beginner system**: you need to handle halts, locates,
  slippage and squeezes.

## Core idea

Short a small-cap runner only when the numbers show likely selling pressure
outweighing likely buying power. There are three variants of that
imbalance. The **gap-up short** fades a stock up more than 100% once early
volume is spent and it starts losing momentum. The **bounce short** sells
into a prior high-volume consolidation where trapped holders wait to get
out near break-even. The **first red day** shorts a parabolic multi-day
runner after the first red day confirms exhaustion. Filters, crowding
reads, timing and size all come from Dux's statistics. Their purpose is to
avoid being right but too early.

## Rules

**A. Qualify the universe (all variants)**

1. **Market cap:** initial market cap under **$100M** for gap-up shorts.
   Bounce shorts and many first red day candidates can go up to about
   **$200M**.
2. **Float:** under **50M shares**. Dux's bands: 1 to 2M is very low float,
   2 to 5M is mid float, 5 to 10M is larger but still in the universe.
3. **Price:** above **$3**. Lower-priced names distort the statistics.
4. **Sector exclusions:** remove **biotech** and **energy** unless there is
   an extreme outlier reason. Avoid **thin Chinese tickers**, especially
   with intraday volume under about **30M shares** and a thin level 2,
   because of halt risk.

**B. Read volume and crowding**

5. **Estimate full-day volume** from pre-market volume, using a rough
   **1:5 to 1:10** ratio.
6. **Crowding limits for a same-day short:**
   - **More than 50M shares pre-market** means caution. The stock can stay
     crowded and squeeze through the setup. The better trade may be the
     next day, if it gaps down and volume dries up.
   - **Float rotation above about 15x**, especially in very low floats,
     means cutting size and waiting for a clear momentum shift.

**C. Gap-up short (intraday)**

7. **Setup:** the stock is up more than **100%**, with initial market cap
   under $100M and float under 50M. Expect an opening push. Dux's averages
   are **30 to 35%** on 1 to 2M floats and **20 to 25%** on 5 to 10M
   floats.
8. **Timing:** do not short the open. Let it push and **consolidate for
   about an hour**. Look for the first meaningful weakness between about
   **10:00 and 11:00**, once roughly **30 to 35% of expected daily volume**
   has traded.
9. **Entry:** start building size during the consolidation and go to full
   size on the breakdown.
   - *Ultra-low float (under about 2M) with heavy rotation:* wait for a
     clear momentum shift, such as a big drop from the high followed by a
     bounce to short.
   - *Higher float (about 7 to 8M):* shorting against the **pre-market
     high** is more acceptable.
10. **Stop:** above the **consolidation high**.
11. **Target:** based on the average fade (see Evidence) and the intraday
    structure. The first objective is continuation of the breakdown from
    the consolidation. Manage by whether volume keeps drying up and trapped
    buyers start leaving.

**D. Bounce short (next-day or multi-day)**

12. **Find trapped supply:** look back about **one year** on the daily
    chart. Find a day where the stock spiked on heavy volume, consolidated
    around a clear price, then dumped. Measure the trapped block, for
    example 25M shares around $5, about **$125M** trapped.
13. **Compare demand with supply:** estimate the current day's volume from
    pre-market (adjusted for a weak open). The trapped-to-current ratio
    should favour the trapped supply, for example **2:1** (current volume of
    about 10 to 15M against 25M trapped). Size up when the ratio is much
    stronger.
    Skip if current volume can match or overwhelm the trapped block.
14. **Entry:** as close as possible to the old consolidation or resistance,
    for the tightest risk.
    - *Gap straight into the zone on light pre-market volume:* it can fail
      fast after the open.
    - *Climb into the zone during regular hours:* expect more patience and
      possibly a bounce before it rolls over.
15. **Stop:** built around the prior resistance or consolidation. Size so
    that a small push through the level is still survivable.
16. **Target:** depends on how price came back. A direct gap into the zone
    tends to fade faster and deeper than a climb from the lows.

**E. First red day (multi-day runner)**

17. **Qualify the run:** at least **three consecutive green days**, with
    rising (or dollar-adjusted rising) volume and about **300% range** from
    the initial breakout. A two-day run needs about **1,000%**. A **red or
    flat day in the middle resets the count.**
18. **Exhaustion check:** estimate whether the day is likely to reach the
    dollar-volume exhaustion zone, using initial market cap, expected day
    range and estimated volume. If it is not likely, leave it alone.
19. **Wait for the first red day**, then trade the **following session**
    when it opens weak or stays red. The second day of weakness is the main
    trade, not the first guess at the top.
20. **Entry:** about **one-quarter size** near the open, adding if price
    bounces into resistance.
21. **Stop:** around the consolidation or spike area of the red-day failure
    zone.
22. **Reward filter:** skip if the first red day has already erased more
    than **about 50% of the whole run**. The remaining reward is too small.
23. **Manage:** ride the unwind as demand fades. With large size, cover
    along the way so the position gives liquidity back instead of trapping
    itself.

## Risk management

- **Stop first, size second:** place the stop at the real invalidation
  point (consolidation high, prior resistance, or spike area), then size
  down until the risk is acceptable. Do not pick a stop to suit a size.
- **Size caps (bounce shorts):** stay under about **10% of the float** and
  about **1% of the volume**. Oversizing can break the supply-demand
  balance the trade depends on.
- **Size down** for very low floats, crowded names, prices just above $3,
  or setups that only barely qualify. **Size up** when the volume ratio is
  strong and trapped supply is obvious.
- **Scaling:** build into gap-up shorts during the consolidation. Start
  first red days at about one-quarter size.
- **Catastrophe rules:** no thin stocks where a halt could block the exit.
  Do not treat ultra-low-float crowding as a normal fade. Do not size a
  first red day as if the top were guaranteed. Do not short into the
  heaviest volume of a squeeze without a momentum shift. The account has to
  survive being early.
- **Risk per trade in $ or % of account, and daily or weekly loss
  limits:** not specified in the playbook.

## What the playbook leaves unspecified

- The actual win rates. The page says each setup has a known approximate
  win rate and frequency per year but gives no numbers.
- The execution chart and the exact definition of a "meaningful"
  breakdown or "momentum shift" (candle close, VWAP loss, prior low).
- How to calculate the first red day's "dollar-volume exhaustion zone" from
  market cap, range and volume. The method is described, but no formula is
  given.
- How deep a consolidation must be, and how to tell it has formed, beyond
  "about an hour".
- Bounce-short size caps beyond the 10% float and 1% volume limits, and
  whether those caps also apply to gap-up shorts and first red days.
- Concrete profit-taking rules: how much to cover at each stage, and
  whether to use time stops.
- Borrow cost, locate availability and short-sale restriction (SSR) effects
  on the entries.
- What counts as an "extreme outlier" that allows a biotech or energy
  trade.
- How the futures listed in the header fit in. No futures rules are given.

## Evidence & claims

All figures are Dux's own statistics as reported on the page,
self-reported (T4):

- **Gap-up short:** average risk about **7%**, average fade about **24 to
  26%** (about 26% from the intraday high, closer to 24 to 25% from a
  confirmed entry), described as roughly **1:3.5 to 1:4** reward-to-risk
  on clean setups. As arithmetic, 24 to 26% over 7% is about 3.4 to 3.7R,
  so the 1:4 end is slightly above the stated averages.
- **Opening push:** averages of 30 to 35% (1 to 2M floats) and 20 to 25%
  (5 to 10M floats).
- **Bounce short:** one approach type faded about **75%** of the move from
  the top, and another about **50%**.
- **Biotech:** Dux's tracking showed a "meaningful drop" in win rate. No
  figure is given.
- **No win rate** is stated, so a full expectancy check is not possible. As
  a reference only: at 1:3.5 the breakeven win rate is 1/4.5 ≈ 22%, and at
  1:4 it is 1/5 = 20%. With E = p×RR − (1−p), the setup needs a win rate
  above those levels, net of slippage and borrow costs, to be positive.

## Concepts & lineage

- Fading emotional, overextended runners back toward value →
  [[concept_mean_reversion]], [[concept_market_sentiment]]
- Trapped volume at a prior consolidation acting as overhead supply →
  [[concept_support_resistance]], [[concept_volume_profile]]
- Pre-market volume, float rotation and crowding as demand measures; halts,
  thin level 2 and locates → [[concept_liquidity]],
  [[concept_market_microstructure]]
- The 9:30 to 11:30 window and the 10:00 to 11:00 trigger →
  [[concept_trading_sessions_killzones]]
- Consolidation, breakdown and bounce-into-resistance triggers →
  [[concept_price_action]]
- Stop at invalidation, then size to float, volume and setup quality →
  [[concept_position_sizing]], [[concept_risk_reward_r_multiples]]
- Scaling in, quarter-size starts and covering into the unwind →
  [[concept_trade_management]]
- Setup frequency, average fade and filters from tracked statistics →
  [[concept_performance_metrics]], [[concept_probabilistic_thinking]],
  [[concept_edge]]
