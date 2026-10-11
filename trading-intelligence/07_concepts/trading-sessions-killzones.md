---
id: concept_trading_sessions_killzones
type: concept
title: Trading Sessions & Kill Zones (time-of-day edge)
partition: 07_concepts
layer: L2
aliases: [market hours, kill zone, killzone, Asian session, London session, New York session, kill zones, London open, NY open, opening range, initial balance, macro times]
related: [concept_liquidity, concept_amd_power_of_three, concept_smart_money_concepts, concept_volatility, concept_news_trading, concept_scalping]
influenced_by: [person_michael_huddleston, person_larry_williams]
status: synthesized
---

# Trading Sessions & Kill Zones

**Volatility and liquidity are not uniform through the day.** Time is a
filter as important as price. BabyPips teaches market hours early because FX
trades 24/5 across overlapping sessions.

## The FX/futures clock (New York time, approximate)

| Window | Character |
|---|---|
| **Asian session** (~19:00–03:00) | Lower range; builds the Asian high/low (often the "accumulation" range) |
| **London open / London kill zone** (~02:00–05:00) | First major expansion; frequently sweeps the Asian range |
| **NY pre-market & US data** (08:30) | News shocks ([[concept_news_trading]]) |
| **NY open / NY AM kill zone** (~09:30–11:00 for indices; 07:00–10:00 FX) | Highest volume overlap with London; main reversals and trends |
| **London close** (~10:00–12:00) | Profit-taking reversals in FX |
| **NY PM / power hour** (15:00–16:00) | Index rebalancing flows |

## How playbooks use time

- **TG Capital (Chart Fanatics):** trades *only* the London kill zone,
  **3:00–6:30 AM NY time**, on the 30-minute chart (T2).
- **Trader Kane, "The Lab Model":** uses the **10:00 AM ET four-hour candle**
  as a timing anchor on NQ (T3 reconstruction).
- **JJ Simon:** treats the NY open/pre-open price as the session's *fair
  price* (`strategy_jj_simon_fair_pricing`).
- **AMT:** the **initial balance** (first hour) frames day type
  ([[concept_auction_market_theory]]).

## Lineage

Larry Williams (day-of-week and time-of-day studies) → Toby Crabel (opening
range breakout, 1990) → ICT kill zones and "macro" windows → session-based
prop-firm scalping. See also [[concept_amd_power_of_three]].
