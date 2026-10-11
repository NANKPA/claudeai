---
id: strategy_usman_ashraf_options
type: strategy
title: "Usman Ashraf — Options Trading Masterclass: Options Fundamentals for Beginners (stock options, options education)"
partition: 01_chart-fanatics
layer: L7
aliases: [Options Trading Masterclass, Usman Ashraf options basics, options fundamentals masterclass, Usman Ashraf options]
taught_by: [person_usman_ashraf]
featured_in: [channel_chart_fanatics]
uses: [concept_options_greeks, concept_volatility, concept_leverage_margin, concept_liquidity, concept_position_sizing]
derived_from: [concept_options_greeks]
related: [strategy_brando_options_swing, strategy_gala_trades_price_action]
sources:
  - {title: "Chart Fanatics — Options Trading Masterclass by Usman Ashraf", url: "https://www.chartfanatics.com/strategies/options-trading-masterclass", tier: T2}
status: verified-t2
---

# Usman Ashraf — Options Trading Masterclass: Options Fundamentals for Beginners (stock options, options education)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/options-trading-masterclass. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Usman Ashraf teaches options to beginners. The page says it is
the foundation of his free six-lesson Options Masterclass on Chart Academy.
This page is an education primer on how options work, not a trade setup.

## Built for

- **Instruments:** options on stocks. The examples use AMD.
- **Style:** not a single style. The page links expiry choice to style:
  day traders may prefer weekly or zero-day (0DTE) contracts, and swing
  traders expirations weeks or months away. Longer-dated options (monthlies
  or LEAPS) are described as slower but less exposed to decay.
- **Timeframes / sessions:** not specified.
- **Audience:** beginners. The page recommends buying options rather than
  selling them while learning, because a buyer's risk is defined.

## Core idea

An option is a contract giving the right, but not the obligation, to buy
(call) or sell (put) 100 shares at a strike price before expiration, for a
premium that is the buyer's maximum loss. Most retail traders trade the
premium rather than exercising. The premium is made of intrinsic and
extrinsic (time) value. It is shaped by moneyness, time decay, implied
volatility and the Greeks, and liquidity decides whether you can get in and
out cleanly. Leverage is the attraction, so sizing and expiry must match
the trader's style.

## Rules

This is the decision checklist the page implies, in order. It is not an
entry model.

1. **Know the contract.** One contract covers **100 shares**. The three
   parts are expiration date, strike price and premium. For a buyer, the
   premium is the most you can lose.
2. **Pick a side you can handle.** Buyers pay the premium and have capped
   risk. Sellers (writers) collect it but carry much larger risk. The page
   says buying is usually safer and simpler for beginners.
3. **Pick the direction.** Buy calls if you expect the stock to rise and
   puts if you expect it to fall. The page gives no method for deciding
   direction.
4. **Plan to trade the premium, not exercise.** The page's example: AMD at
   $95, a $97 call bought for $0.50 ($50 per contract) might be worth $1.50
   if AMD reaches $98, so selling it returns $150 without touching the
   shares.
5. **Choose moneyness.** ITM options already have intrinsic value. ATM
   strikes sit near the current price. OTM strikes are cheaper but need a
   bigger move to pay.
6. **Respect time.** Extrinsic value falls as expiration approaches, and at
   expiry only intrinsic value is left. You are trading direction within a
   limited time.
7. **Check implied volatility.** Higher IV makes premiums more expensive,
   and lower IV makes them cheaper. Before earnings IV usually rises, then
   often collapses after the release (volatility crush), pulling option
   prices down with it.
8. **Read the Greeks.**
   - *Delta:* price change per $1 move in the stock. 0.50 means about $0.50.
     Calls have positive delta and puts negative.
   - *Gamma:* how fast delta changes. It is high for short-dated and 0DTE
     options.
   - *Theta:* daily time decay. The page's example is −0.10, about $0.10 lost
     per day.
   - *Vega:* change per 1% move in IV. The example is 0.20, about $0.20 per
     1%.
9. **Check liquidity.** Volume is today's contracts traded and resets at
   the open. Open interest is all contracts still open. In the page's
   example, wanting 70 contracts at a strike with only 100 OI may fill
   slowly, while 10,000 OI is no problem.
10. **Match expiry and size to style.** Short-dated contracts can move
    explosively but decay fast, and a sideways move can erase much of the
    premium. Longer-dated ones move slower but cushion decay.
11. **Choose a risk method.** Either treat the whole premium as the risk
    ("sizing to zero"), or use a stop based on premium value or price
    levels. The page says both can work.

## Risk management

- **Max loss for a buyer:** the premium paid.
- **Risk per trade:** Not specified in the playbook (no % or $ figure).
- **Sizing:** match position size and expiry to style. Two approaches are
  given: size to zero, or a premium-based or price-level stop. No numbers.
- **Daily / weekly limits:** Not specified in the playbook.
- **Seller risk:** described as far greater than buyer risk. No limits or
  margin rules are given.
- **Warning:** leverage makes losses compound as fast as gains without
  discipline.

## What the playbook leaves unspecified

- Any trade setup: how to choose direction, when to enter, where to take
  profit or when to exit.
- Which delta, strike distance or days to expiry to choose for day trades
  versus swings.
- IV thresholds, such as when an option is too expensive to buy.
- A stop level for premium-based stops, such as a percentage of premium.
- Unit conventions. Editor's note from general options knowledge, not from
  the page: the Greek examples are per share, so a contract of 100 shares
  moves about 100 times those amounts, and theta changes as expiry nears
  rather than staying fixed.
- Assignment risk, market hours, 0DTE mechanics and strategy selection.
  The page says these are covered in the full Chart Academy course, not
  here.

## Evidence & claims

- The page makes **no win-rate, R:R, P&L or payout claims**.
- The AMD premium example ($50 to $150, tripling) and the house and car
  deposit analogies are **hypothetical illustrations**, not trade results.
- Two statements are the author's guidance, not tested claims (T4): that
  buying options is usually safer and simpler for beginners, and that
  options can become "one of the most effective tools in your trading
  arsenal".

## Concepts & lineage

- Delta, gamma, theta and vega, and how they move the premium →
  [[concept_options_greeks]]
- Implied volatility, volatility crush around earnings →
  [[concept_volatility]]
- Controlling 100 shares for a fraction of their cost →
  [[concept_leverage_margin]]
- Volume and open interest as fill-quality measures →
  [[concept_liquidity]]
- Matching expiry and size to style, sizing to zero or premium stops →
  [[concept_position_sizing]]
- Lineage: standard options pricing sensitivities →
  [[concept_options_greeks]]
