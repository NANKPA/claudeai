---
id: concept_fair_value_gap
type: concept
title: Fair Value Gap (FVG), Inversion FVG, Imbalance
partition: 07_concepts
layer: L3
aliases: [FVG, fair value gap, imbalance, inefficiency, IFVG, inversion fair value gap, BPR, balanced price range, consequent encroachment]
related: [concept_smart_money_concepts, concept_market_structure, concept_order_blocks_breakers, concept_volume_profile, concept_trade_execution]
derived_from: [concept_chart_patterns]
influenced_by: [person_michael_huddleston]
status: synthesized
---

# Fair Value Gap (FVG)

**Definition (3-candle).** In a bullish FVG, candle 1's high is below
candle 3's low. The middle candle moved so fast that a price range traded
only one-sided. Bearish is the mirror image.

```
bullish FVG = [high(c1), low(c3)]  when low(c3) > high(c1)
```

## Interpretation

- Represents **one-sided, inefficient delivery** (displacement). It is the
  candlestick analogue of a **low-volume node** ([[concept_volume_profile]])
  and of classic **gaps** in Edwards & Magee.
- Price often **revisits** the gap to rebalance before continuing. Entries at
  the gap or its midpoint (**consequent encroachment, 50%**) offer a tight
  stop.
- **Inversion FVG (IFVG).** An FVG that price closes *through* flips polarity.
  A failed bullish gap becomes resistance. Candace Lau and Trader Kane use
  IFVGs as reversal confirmation.
- **Balanced Price Range (BPR).** Overlapping bullish and bearish FVGs.

## Rules of thumb

1. Only FVGs **created by displacement that broke structure** matter.
   Random gaps in chop do not.
2. Context first: in a discount zone in an uptrend, a bullish FVG is a
   candidate entry ([[concept_premium_discount_ote]]).
3. **TG Capital's "Trident":** FVG + a doji wick into its midpoint + a
   confirmation candle, inside the London kill zone with stacked EMAs
   (`strategy_tg_capital_trident`).

## Evidence note

FVG "fills" are common partly by construction: price frequently retraces
into any recent range. Measure the fill rate *and* the post-fill
continuation rate in your market before relying on it.
