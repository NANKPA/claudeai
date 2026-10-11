---
id: strategy_carmine_rosato_lvn
type: strategy
title: "Carmine Rosato — Low Volume Node (LVN) Pullback Strategy (futures/indices, scalping/day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Carmine LVN Trading Strategy, LVN pullback, low volume node strategy, Carmine LVN]
taught_by: [person_carmine_rosato]
featured_in: [channel_chart_fanatics]
uses: [concept_volume_profile, concept_order_flow, concept_support_resistance, concept_liquidity, concept_scalping, concept_position_sizing, concept_risk_reward_r_multiples]
derived_from: [concept_volume_profile, concept_auction_market_theory]
related: [strategy_carmine_rosato_orderflow_masterclass, strategy_forrest_knight_volume_profile, strategy_fabio_valentini_amt_order_flow]
sources:
  - {title: "Chart Fanatics — Carmine LVN Trading Strategy", url: "https://www.chartfanatics.com/strategies/low-volume-node", tier: T2}
status: verified-t2
---

# Carmine Rosato — Low Volume Node (LVN) Pullback Strategy (futures/indices, scalping/day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/low-volume-node. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Carmine Rosato teaches order flow, Level 2 walls, and reversal
and breakout-retest setups in free masterclasses on Chart Academy. This LVN
setup is described as using the same order-flow method.

## Built for

- **Instruments:** futures and indices.
- **Style:** scalping and day trading.
- **Timeframe / session:** no chart timeframe is named. The worked example
  starts at the open and plays out later in the same session.
- **Tools:** volume-by-price profile, liquidity heatmap, footprint chart and
  delta.

## Core idea

A strong push away from a key level runs fast and leaves little traded
volume behind. That thin pocket is a **low volume node (LVN)**, and the
playbook reads it as a sign that large participants were active. Price
often comes back to the LVN, where those participants reload or defend
their positions. The trader waits for that return, gets order-flow proof
that the level is being defended again, and enters with a tight stop for a
high reward-to-risk trade.

## Rules

1. **Mark a level of interest.** Find a clear supply, demand, support or
   resistance level. Price should have consolidated there and then moved
   impulsively away, which shows strong buyers or sellers.
2. **Let price leave.** The first move away is not an entry. Wait for the
   rally or drop that confirms large participants stepped in.
3. **Find the LVN.** On a volume-by-price profile, locate the area that
   price crossed quickly on little or no volume. Treat it as a **zone**,
   not a single price.
4. **Wait for the revisit.** Let price pull back into the LVN.
5. **Confirm the defence.** Use the heatmap, footprint, delta or order flow
   to see large buyers or sellers defending the zone. In the example, this
   meant passive bids held while sell orders hit them, aggressive selling
   was absorbed, and every new low was bought straight back.
6. **Enter.** Go long when price bounces from demand or support, short when
   it rejects supply or resistance.
7. **Stop.** Just beyond the LVN, or beyond the recent low (for longs) or
   high (for shorts).
8. **Size.** Set position size from the stop distance so the dollar risk is
   the same on every trade.
9. **Target.** A logical level: high or low of the day, another supply or
   demand zone, another LVN, or a support or resistance level. Scale out or
   take the whole profit depending on context and volatility.

**Worked example (long).** The market sold off at the open into a marked
demand zone and bounced hard. The rally left two LVNs, one at 5563 and a
deeper one in the 5550s. Later, price pulled back into the 5563 LVN and
showed absorption. The long went in at 5561 with a tight stop just below
the zone, and price reached the target, the high of the day.

## Risk management

- **Risk per trade:** fix the dollar risk before every entry. The amount
  itself is not specified in the playbook.
- **Sizing:** from the stop distance, so dollar risk stays constant.
- **Invalidation:** a move through the LVN zone or the recent swing, where
  the stop sits.
- **Daily or weekly limits:** not specified in the playbook.
- **Mindset:** accept that some trades will lose, and stay disciplined.

## What the playbook leaves unspecified

- Which chart timeframe and which profile lookback to use when finding LVNs.
- How to choose among several LVNs. The page admits this takes experience;
  its example had two candidates and used the shallower one.
- What exactly counts as confirmation: how much absorption, which delta
  reading, how many failed breaks.
- How tight the stop is in ticks or points. The example says only that it
  sat "just below the zone".
- The minimum reward-to-risk, and the rules for scaling out.
- Whether to trade only at certain times or sessions, and any daily loss
  limit.

## Evidence & claims

- The page claims **no win rate, R:R figure, P&L or payout**. Among the pros
  it lists a qualitative "High reward-to-risk potential" (self-reported,
  T4).
- The example gives an entry (5561) and a target (high of day) but no stop
  price, so its R multiple cannot be worked out. No expectancy check is
  possible.

## Concepts & lineage

- Finding thin-volume zones on a volume-by-price profile →
  [[concept_volume_profile]]
- An LVN as a pocket the auction moved through quickly on thin volume →
  [[concept_auction_market_theory]]
- Confirming the defence with heatmap, footprint and delta absorption →
  [[concept_order_flow]], [[concept_liquidity]]
- Supply, demand, support and resistance as the origin of the move →
  [[concept_support_resistance]]
- Tight-stop intraday execution → [[concept_scalping]]
- Constant dollar risk set by stop distance →
  [[concept_position_sizing]], [[concept_risk_reward_r_multiples]]
