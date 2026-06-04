# 📈 National Grid Load Forecasting via STL Decomposition & SARIMAX

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Statsmodels](https://img.shields.io/badge/statsmodels-0.14+-green.svg)](https://www.statsmodels.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)

## 📌 Overview
This repository delivers an end-to-end econometric time series pipeline to model and forecast Turkey’s national electricity generation and consumption metrics (TEİAŞ). By decoupling complex multi-seasonal grid behaviors, the framework evaluates structural trends, applies comprehensive stationarity diagnostics, and deploys tuned SARIMAX models to ensure grid load optimization and energy security analytics.

---

### 🎯 Goal & Modern Value
* **Goal:** Model structural electricity consumption patterns, isolate temporal seasonality, and execute statistical out-of-sample projections with calibrated confidence boundaries.
* **Expert Consensus (2026):** High-frequency utility and grid data exhibit heavily volatile seasonal signatures. The modern analytical standard leverages robust **STL (Seasonal and Trend Decomposition using Loess)** to separate deterministic trend components from stochastic residuals, combining it with regularized **SARIMAX** wrappers to account for calendar effects and exogenous shocks before deploying machine learning layers.

---

## 🏗️ Pipeline Architecture
* **Operational Cleaning:** Handles outlier detection and variance stabilization across cross-sectional generation metrics.
* **Robust STL Decomposition:** Extracts underlying structural trends and isolates distinct monthly/annual periodicities using localized regression modeling.
* **Statistical Rigor:** Runs simultaneous Augmented Dickey-Fuller (ADF) and KPSS diagnostics to guarantee mathematical transformation stationarity.
* **Residual Verification:** Validates model robustness using Ljung-Box and Jarque-Bera matrices to confirm residuals follow a strict non-correlated white noise distribution.

---

## 📁 Project Structure
The repository strictly adheres to clean, production-ready modular machine learning layouts:

```text
Time-Series-Project/
├── notebooks/             # Main interactive econometric research environment (teias_report.ipynb)
├── reports/               
│   ├── html/              # Production-grade high-fidelity analytical report html
│   └── figures/           # Generated diagnostic assets (ACF, PACF, STL, Forecast Profiles)
├── presentation/          # Master executive slide deck (TEIAS_Final_Sunum.pptx)
├── .gitignore             # Strict exclusion matrix for local JREs and datasets
└── README.md              # Global architectural documentation
