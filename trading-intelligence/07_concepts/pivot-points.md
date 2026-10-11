---
id: concept_pivot_points
type: concept
title: Pivot Points
partition: 07_concepts
layer: L3
aliases: [floor pivots, standard pivots, camarilla, woodie, R1 S1, daily pivot]
related: [concept_support_resistance, concept_trading_sessions_killzones, concept_mean_reversion, concept_breakout_trading]
status: synthesized
---

# Pivot Points

BabyPips Middle School Grade 8: computing pivot points and using them for
**range trading** and **breakouts**.

## Standard (floor) pivots from the prior period's H, L, C

```
P  = (H + L + C) / 3
R1 = 2P − L        S1 = 2P − H
R2 = P + (H − L)   S2 = P − (H − L)
R3 = H + 2(P − L)  S3 = L − 2(H − P)
```

Variants: Woodie, Camarilla, Fibonacci pivots.

## Use

- **Range days:** fade R1/S1 back toward P.
- **Trend days:** a break-and-hold beyond R1/S1 targets R2/S2.
- They work largely because floor traders and algorithms watch the same
  prior-day H/L/C references, which are themselves liquidity levels
  ([[concept_liquidity]]).
