---
id: concept_machine_learning_finance
type: concept
title: Machine Learning in Finance (labels, leakage, meta-labeling)
partition: 07_concepts
layer: L0
aliases: [financial machine learning, triple barrier, meta-labeling, purged cross-validation]
related: [concept_backtesting, concept_overfitting_validation, concept_time_series_statistics, concept_performance_metrics]
influenced_by: [person_marcos_lopez_de_prado]
status: synthesized
---

# Machine Learning in Finance

Financial data has a low signal-to-noise ratio, is non-stationary, and is
autocorrelated. Off-the-shelf ML overfits it badly. The core corrections
come from López de Prado, *Advances in Financial Machine Learning* (2018):

1. **Better bars.** Sample by information (dollar, volume, or tick-imbalance
   bars) instead of time. The returns come out closer to i.i.d.
2. **Triple-barrier labeling.** Label each event by which barrier is hit
   first: profit-take, stop-loss, or time limit. The label then matches how a
   trade actually resolves ([[concept_trade_management]]).
3. **Meta-labeling.** A primary model (it can be a discretionary setup!)
   decides *side*. A secondary ML model decides *whether to take the trade and
   how big*. This is the most practical bridge between a discretionary
   playbook and ML ([[concept_position_sizing]]).
4. **Purged and embargoed K-fold CV.** Remove training samples whose labels
   overlap the test window, to prevent leakage.
5. **Feature importance** (MDI, MDA, SFI) instead of chasing in-sample accuracy.
6. **Deflated Sharpe ratio** and the probability of backtest overfitting
   correct for the number of trials ([[concept_overfitting_validation]]).

## Practitioner warning

Most ML funds fail for process reasons: siloed researchers, backtest
overfitting, and non-stationary features. They rarely fail for model-choice
reasons. Start with a sound economic hypothesis ([[concept_edge]]) and use ML
to *filter and size*, not to discover the whole strategy.
