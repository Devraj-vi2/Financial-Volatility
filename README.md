\# Financial Volatility Forecasting \& Risk Decision System



An uncertainty-aware financial time-series forecasting system that predicts market volatility and converts probabilistic forecasts into dynamic risk-exposure decisions.



\## Problem



Financial markets exhibit changing volatility regimes. A model that predicts expected volatility without quantifying uncertainty can provide an incomplete picture for risk management.



This project combines machine learning, deep learning, and Bayesian uncertainty estimation to forecast volatility and translate predictions into actionable risk regimes.



\## System Architecture



Market Data

&#x20;       ↓

Data Cleaning \& Feature Engineering

&#x20;       ↓

Rolling Volatility / Returns / Volume

&#x20;       ↓

PCA Dimensionality Reduction

&#x20;       ↓

┌───────────────┬────────────────┐

│    XGBoost    │      LSTM      │

└───────────────┴────────────────┘

&#x20;                ↓

&#x20;          Bayesian LSTM

&#x20;                ↓

&#x20;         MC Dropout (T=100)

&#x20;                ↓

&#x20;    Volatility + Uncertainty

&#x20;                ↓

&#x20;      Risk Regime Classification

&#x20;                ↓

&#x20;      Dynamic Risk Exposure

&#x20;                ↓

&#x20;         Historical Backtest



\## Dataset



Market data was collected for six financial instruments:



\- SPY — S\&P 500 ETF

\- QQQ — Nasdaq-100 ETF

\- GLD — Gold ETF

\- TLT — Long-Term Treasury ETF

\- USO — Oil ETF

\- VIX — Market Volatility Index



The dataset contains approximately 4,024 trading observations.



\## Feature Engineering



The pipeline incorporates:



\- Daily returns

\- Rolling volatility

\- Price-based features

\- Trading volume

\- Cross-asset information

\- PCA-derived market factors



PCA was used to reduce correlated market variables while retaining approximately 95% of the variance.



\## Models



\### XGBoost



A gradient-boosted tree model trained on engineered market features for volatility forecasting.



\### LSTM



A recurrent neural network trained on sequential market observations to capture temporal dependencies.



\### Bayesian LSTM



Monte Carlo Dropout was applied during inference to obtain multiple stochastic predictions.



100 forward passes were used to estimate:



\- Predictive mean

\- Predictive standard deviation

\- Approximate prediction intervals



This allows the system to distinguish between predictions with different levels of uncertainty.



\## Risk Decision Engine



Predicted volatility is converted into four risk regimes:



| Regime | Exposure |

|---|---:|

| LOW | 100% |

| NORMAL | 75% |

| HIGH | 40% |

| EXTREME | 15% |



The exposure level is then used by the backtesting framework to evaluate a volatility-aware strategy.



\## Backtest Results



The risk-aware strategy was compared against a Buy \& Hold SPY benchmark.



| Metric | Risk-Aware Strategy | Buy \& Hold |

|---|---:|---:|

| Annual Return | 8.24% | 21.51% |

| Annual Volatility | \*\*6.84%\*\* | 16.03% |

| Sharpe Ratio | 1.21 | 1.34 |

| Maximum Drawdown | \*\*-7.58%\*\* | -18.76% |



The strategy reduced annualized volatility by approximately \*\*57%\*\* and maximum drawdown by approximately \*\*60%\*\*, while accepting lower absolute returns.



The system is therefore designed primarily as a \*\*risk-management and exposure-control framework\*\*, rather than a return-maximization strategy.



\## Tech Stack



\- Python

\- Pandas

\- NumPy

\- Scikit-learn

\- XGBoost

\- PyTorch

\- Matplotlib

\- Seaborn

\- yFinance

\- Jupyter



\## Repository Structure



```text

financial-volatility/

│

├── data/

├── models/

├── notebooks/

│   ├── 01\_eda.ipynb

│   ├── 02\_xgboost.ipynb

│   └── 03\_lstm.ipynb

│

├── results/

│   ├── model\_comparison.csv

│   ├── risk\_decisions.csv

│   └── backtest\_comparison.csv

│

├── reports/

├── src/

│

├── README.md

├── requirements.txt

└── .gitignore

