---
id: concept_prop_firm_risk_rules
type: concept
title: Prop-Firm Evaluations & Risk Rules
partition: 07_concepts
layer: L6
aliases: [prop firm, funded account, evaluation, challenge, trailing drawdown, daily loss limit, consistency rule, payouts]
related: [concept_risk_of_ruin_drawdown, concept_position_sizing, concept_scalping, concept_trading_psychology]
sources:
  - {title: "BabyPips — Risk Management: How to Increase Your Odds of Passing Prop Firm Challenges", url: "https://www.babypips.com/learn/forex/prop-firm-risk-management", tier: T2}
status: synthesized
---

# Prop-Firm Evaluations & Risk Rules

Most Chart Fanatics guests are futures prop-firm traders, and payout totals
are a common credential (e.g., JJ Simon's claims of $1.2M–$1.8M in payouts;
the numbers vary by source, so they are T4).

## Typical rules

| Rule | Effect on strategy |
|---|---|
| **Max (trailing) drawdown** | Path-dependence: early losses can end the account. Favours small risk early. |
| **Daily loss limit** | Caps tail days; forces a stop-trading rule |
| **Profit target** | Encourages over-aggression near deadlines |
| **Consistency rule** | No single day can exceed X% of profits |
| **News restrictions** | No trading around high-impact releases ([[concept_news_trading]]) |

## Sizing math for evaluations

Treat the drawdown limit as the **bankroll**. With a $2,500 trailing limit,
risking $250/trade (10% of the buffer) gives a material chance of failure
after a normal losing streak ([[concept_risk_of_ruin_drawdown]]). BabyPips'
prop guidance: apply `(Account × Risk%) ÷ Stop` consistently, budget risk per
trade, per idea, and per day, and stop after a set number of daily losses.

## Caveat

Evaluation success ≠ live edge. Several sources note prop-optimised
strategies behave differently on live accounts (fills, size, psychology).
Umar Ashraf's framework warns: *"The goal is NOT to make money"* early on;
it is to collect data and build process.
