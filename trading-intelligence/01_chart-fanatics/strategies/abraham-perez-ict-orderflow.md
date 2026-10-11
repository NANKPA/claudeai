---
id: strategy_abraham_perez_ict_orderflow
type: strategy
title: "Abraham Perez — Nasdaq ICT & Order Flow Scalping Strategy (NQ futures, scalping)"
partition: 01_chart-fanatics
layer: L4
aliases: [Nasdaq ICT order flow scalping, NQ ICT + Bookmap scalping, Abraham Perez NQ strategy, IFVG order-flow scalp]
taught_by: [person_abraham_perez]
featured_in: [channel_chart_fanatics]
uses: [concept_smart_money_concepts, concept_liquidity, concept_liquidity_sweep_reversal, concept_fair_value_gap, concept_market_structure, concept_dow_theory, concept_order_flow, concept_volume_profile, concept_vwap, concept_multi_timeframe_analysis, concept_trading_sessions_killzones, concept_risk_reward_r_multiples, concept_scalping]
derived_from: [concept_smart_money_concepts, concept_order_flow]
related: [strategy_candace_lau_nq_sweep_reversal, strategy_marco_trades_liquidity_grab, strategy_yush_order_flow]
sources:
  - {title: "Chart Fanatics — Nasdaq ICT & Order Flow Scalping Strategy (NQ)", url: "https://www.chartfanatics.com/strategies/nasdaq-ict-and-order-flow-scalping-strategy", tier: T2}
status: verified-t2
---

# Abraham Perez — Nasdaq ICT & Order Flow Scalping Strategy (NQ futures, scalping)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/nasdaq-ict-and-order-flow-scalping-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook presents Abraham as a discretionary Nasdaq futures scalper who combines ICT liquidity concepts, Dow Theory structure, volume analysis and Bookmap order flow. The page text uses only his first name; the surname Perez comes from this knowledge base's catalogue entry, not the playbook. The page gives no other biography.

## Built for

- **Instruments:** Nasdaq futures (NQ).
- **Style:** scalping. Discretionary, and it needs the ability to read structure, liquidity, volume and Bookmap.
- **Timeframes:**
  - Daily and 4-hour for context.
  - 1-hour and 15-minute to confirm structure.
  - 1-minute and seconds charts to refine the entry.
- **Sessions:**
  - Asia and New York are the main sessions. Asia on Nasdaq can be cleaner when everything lines up.
  - New York can be more manipulated, balanced or choppy, so it needs more patience.
  - London is usually less attractive for this approach.

## Core idea

The entry pattern is not the edge. The edge comes from knowing where liquidity is likely to be targeted, how price reacts once it is taken, and whether buyers or sellers are actually in control. The process has three steps: find the bias on higher timeframes, wait for liquidity to be taken, then enter only when structure, volume and Bookmap order flow all confirm. In the playbook's words, "liquidity can attract price, but aggression moves price."

## Rules

1. **Higher-timeframe context (Daily, 4H).** Establish the likely direction and whether price is trending or rotating. Find external liquidity (above major highs, below major lows) and the next reaction area. Ask where price is most likely to raid liquidity first. An uptrend can still raid downside liquidity before continuing, and a downtrend can raid upside liquidity. After external liquidity is taken, look for a pullback into internal liquidity or the next reaction zone.
2. **Secondary structure (1H, 15M).** Lower-timeframe structure must support the higher-timeframe idea. Look for:
   - displacement in the intended direction;
   - a strong close, not just a wick;
   - volume that shows real intent.
3. **Liquidity first.** Wait for price to take a pool rather than front-running it. Pools include prior highs and lows, equal highs and lows, obvious liquidity pools, and prior support and resistance. A sweep alone is *not* a signal: price can take liquidity and keep going.
4. **Confirmation checklist.** Before any entry, all five must be true:
   - liquidity was taken;
   - structure shifted;
   - volume supports the move;
   - order flow supports the direction;
   - Bookmap shows aggression on the correct side.

   POC or VWAP should also act as support or resistance in favour of the trade. If Bookmap looks balanced, wait.
5. **Entry model (1M or seconds chart). Pick one:**
   - **IFVG.** *Short:* liquidity is taken above, price sells off aggressively and closes below the IFVG, and order flow confirms. *Long:* sell-side liquidity is taken, price reclaims with volume and closes above the IFVG, and order flow confirms. An IFVG without order-flow support is skipped, because these fail often.
   - **Change in State of Delivery.** Price reacts at a key area and appears to continue the old direction. It then manipulates with volume, breaks the other way, and retests the broken area: failed support becomes resistance for shorts, broken resistance becomes support for longs. Enter once volume and order flow confirm the control shift.
   - **Break and retest continuation.** Price breaks a prior high or low with displacement, and a fair value gap carries the move. The retest of the broken area must close back in the continuation direction, with order flow supporting.
6. **Stop.** *Shorts:* above the swept high or the structure that invalidates the bearish idea. *Longs:* below the swept low or the invalidating structure. If POC or VWAP is reclaimed against the trade, the thesis is weakening.
7. **Targets.**
   - In choppy or uncertain conditions, such as a manipulated New York session, use a conservative target of about 1:2.
   - In clean conditions with strong order flow, hold toward the next liquidity pool or reaction area: opposing liquidity, prior highs and lows, or fair value zones.
8. **Management.** Give the trade room while POC and VWAP keep supporting it and the session is clean. Cut or reduce if aggressive volume flips against the position or the controlling side loses control.
9. **No-trade conditions.** Don't trade if any of these apply:
   - higher-timeframe context and lower-timeframe structure disagree;
   - the market is balanced with no side in control;
   - no meaningful liquidity has been taken;
   - the pattern appears without order-flow confirmation;
   - the entry would be late;
   - risk can't be clearly defined;
   - POC or VWAP works against the idea;
   - volume doesn't support the direction.

## Risk management

- **Risk per trade:** Not specified in the playbook beyond keeping risk "tight enough for a scalp".
- **Sizing:** match position size to the stop distance. No fixed % or contract count is given.
- **Invalidation:** the structure that proves the idea wrong (the swept high or low). POC or VWAP reclaiming against the trade is a warning sign.
- **Chasing:** don't enter late. If the move has run too far, the risk-to-reward no longer works.
- **Daily / weekly limits:** Not specified in the playbook.

## What the playbook leaves unspecified

- Exact Asia and New York session times, and any news filter.
- Objective thresholds for "displacement", volume that "shows intent", and Bookmap aggression (dot or print size), plus a definition of a "balanced" heatmap.
- Which POC (session, developing or composite) and which VWAP anchor.
- IFVG geometry: which timeframe's gap, and how a close "below/above the IFVG area" is measured.
- How to choose between the three entry models in real time.
- When to move to break-even, partial-profit rules, a daily loss limit, and a maximum trade count.

## Evidence & claims

- The page makes no win-rate, P&L or payout claims.
- The "~1:2" figure is a target rule for choppy conditions, not a reported result. For reference, a strict 1:2 needs a win rate above 33.3% to break even before costs.
- The two worked examples are a bearish pullback short, discussed for both Asia and New York (closer to 1:2 in New York), and an Asia continuation short. Both are described qualitatively, with no prices or numeric outcomes (T4).

## Concepts & lineage

- External vs internal liquidity, equal highs and lows, liquidity pools: [[concept_liquidity]]
- A sweep is not an automatic reversal; wait for confirmation after the raid: [[concept_liquidity_sweep_reversal]]
- IFVG and FVG-driven continuation: [[concept_fair_value_gap]]
- ICT framework, including Change in State of Delivery: [[concept_smart_money_concepts]]
- Displacement, structure shifts, break and retest: [[concept_market_structure]], [[concept_dow_theory]]
- Bookmap heatmap (passive liquidity) vs tape and dots (aggressive orders), absorption: [[concept_order_flow]]
- POC as a support or resistance filter: [[concept_volume_profile]]; VWAP as a filter: [[concept_vwap]]
- Daily/4H → 1H/15M → 1M/seconds top-down process: [[concept_multi_timeframe_analysis]]
- Asia vs New York vs London session quality: [[concept_trading_sessions_killzones]]
- Conservative 1:2 targets vs holding toward the next liquidity pool: [[concept_risk_reward_r_multiples]]
- Short-holding-period execution: [[concept_scalping]]
