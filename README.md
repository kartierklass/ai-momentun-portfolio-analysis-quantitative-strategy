# MomentumFlow: An AI-Powered Quantitative Strategy Engine 🚀

**MomentumFlow is a complete, end-to-end Python framework for developing, testing, and understanding AI-driven stock trading strategies. This project moves beyond simple model building to create a robust backtesting engine that evaluates performance, identifies common pitfalls like overfitting, and uses Explainable AI (XAI) to interpret a model's decision-making process.**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/xgboost-4E7496?style=for-the-badge&logo=xgboost&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

---

## Project Overview

The goal of this project was to explore the viability of an AI-enhanced momentum investing strategy. The system automates the entire quantitative research workflow:

* **Data Pipeline**: Fetches historical stock price data using the `yfinance` API.
* **Feature Engineering**: Creates a rich feature set, including multi-period momentum signals (1, 3, 6, and 12-month) and rolling volatility as a risk metric.
* **Comparative Modeling**: Trains and evaluates multiple machine learning models, starting with a baseline `RandomForest` and upgrading to a more powerful `XGBoost` model to improve generalization.
* **Backtesting Engine**: Implements a robust backtesting framework to simulate the strategy's performance on unseen data, comparing it against a simple equal-weighted benchmark.
* **Explainable AI (XAI)**: Integrates model interpretability using feature importance analysis to understand the key drivers behind the AI's predictions.

---

## The Core Finding: A Realistic Outcome

A key outcome of this project was the practical demonstration of **overfitting** in a financial context. The initial RandomForest model achieved a near-perfect training score (R² of 0.98) but failed significantly on test data (R² of -0.37).

Upgrading to an XGBoost model produced a more realistic and healthier result, reducing overfitting (Training R² of 0.47) and improving test performance. However, the final backtest confirmed that even this improved model did not outperform the benchmark. This is a realistic outcome in quantitative finance and highlights that the primary value of this project is the **framework itself**—a powerful tool for rapidly prototyping and validating new ideas.

### Final Performance Backtest
**

---

## Model Interpretability: Understanding the "Why"

Using XGBoost's built-in feature importance, we analyzed the "brain" of our best-performing model. The analysis revealed that long-term momentum and recent volatility were the most influential factors in its decision-making process. This step moves beyond a "black box" approach to provide crucial insights into the model's behavior.

### Feature Importance Analysis
**

---

## Tech Stack

| Technology      | Purpose                                    |
| --------------- | ------------------------------------------ |
| **Python** | Core programming language                  |
| **Pandas** | Data manipulation and analysis             |
| **scikit-learn**| Baseline model (RandomForest) and ML tools |
| **XGBoost** | Advanced gradient boosting model           |
| **Matplotlib** | Data visualization and plotting            |
| **Jupyter** | Interactive development and analysis       |
| **yfinance** | Financial data acquisition                 |

---

## Installation & Usage

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/MomentumFlow.git](https://github.com/YourUsername/MomentumFlow.git)
    cd MomentumFlow
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch the Jupyter Notebook:**
    ```bash
    jupyter notebook analysis.ipynb
    ```

---

## Future Enhancements

This framework provides a strong foundation for future research, including:
* **Integrating Alternative Data**: Incorporating NLP-driven news sentiment analysis as an additional feature.
* **Advanced Time-Series Models**: Experimenting with deep learning models like LSTMs that are specifically designed for sequential data.
* **Hyperparameter Tuning**: Implementing systematic tuning (e.g., GridSearch) to optimize model performance.
* **Portfolio Optimization**: Moving beyond a "winner-take-all" strategy to build an optimized portfolio based on Markowitz theory.
