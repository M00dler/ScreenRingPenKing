# Problem Statement: Football Player Market Value Prediction

## Context:
Football is one of the most popular sports globally, with professional players commanding egregiously high market values. Market valuations are influenced by numerous factors, including physical attributes, game performance, and experience.

## Challenges:
The transfer market's complexity, with non-linear relationships between factors like player statistics and market value, makes accurate predictions difficult. Additionally, there is a need to interpret predictions for practical use by stakeholders.

## Project Objective:
To predict football players' current market values and understand the key factors driving these valuations using machine learning models.

---

## Features:
- **Dataset**: Kaggle's TransferMarkt Football Player Stats, including tens of thousands of players' personal, professional, and match statistics.
- **Key Features**:
  - Player attributes: age, position, competition rank.
  - Game statistics: goals, assists, minutes played, cards.
  - Regional and competition-related data.
- **Preprocessing**:
  - Merging multiple CSV files into a refined dataset.
  - Dropping irrelevant columns and rows with missing critical data.
  - Feature engineering: one-hot encoding positions, calculating ages, and log-transforming target values for better distribution.

---

## Targets:
- **Prediction Target**: Market value of football players.
- **Evaluation Metrics**:
  - **Mean Absolute Error (MAE)**: Measures average prediction error.
  - **R² (Coefficient of Determination)**: Measures model reliability.

---

## Methodology:
1. **Exploratory Data Analysis**:
   - Observed trends in market valuations by time, position, and age.
   - Identified patterns such as higher valuations for younger players and attackers.
2. **Data Processing**:
   - Consolidated data, encoded features, and simplified columns for efficient analysis.
   - Addressed multicollinearity using Elastic Net regularization.
3. **Model Training**:
   - Implemented and compared four models:
     - **Linear Regression**: Baseline with interpretable linear relationships.
     - **Elastic Net**: Combines L1/L2 regularization to handle multicollinearity.
     - **Random Forest**: Captures non-linear relationships with ensemble learning.
     - **XGBoost**: Highly accurate gradient boosting with advanced optimizations.
   - Used **GridSearchCV** to fine-tune hyperparameters.
4. **Model Selection**:
   - Best model: **XGBoost** (MAE: €1.14M, R²: 0.714).
   - Improved performance through parameter tuning (MAE reduced to 0.641).

---

## Insights:
- **Key Features**:
  - Positive correlation: Recent goals and assists.
  - Negative correlation: Competition rank, age, and position (e.g., goalkeeper).
- **Valuation Trends**:
  - Younger players (20–27) and attackers have higher valuations.
  - Recent performance weighs more heavily than historical data.
- **Error Analysis**:
  - Residual errors follow a normal distribution, confirming model robustness.

---

## Conclusion:
We successfully developed a robust model to predict football player market values with low error margins. This project demonstrates the potential of machine learning in solving complex valuation problems, offering actionable insights for stakeholders in the football transfer market.

## Main notebook:
`football_final.ipynb`

## Contributors:
- [Audric Yap](https://github.com/AudricY)
  - feature engineering, model training, model evaluation
- [Gabriel Lim](https://github.com/M00dler)
  -  feature engineering, model training, model evaluation
- [Joshua Chin](https://github.com/yuurraa)
  - EDA, data preprocessing, feature engineering, model training, model evaluation

## References:
- https://www.kaggle.com/datasets/davidcariboo/player-scores/data 
- https://xgboost.readthedocs.io/en/stable/
- https://scikit-learn.org/stable
- https://seaborn.pydata.org/
- https://matplotlib.org/stable
- https://pandas.pydata.org/pandas-docs/stable
- https://numpy.org/doc/stable/
- https://www.kaggle.com
- https://www.transfermarkt.com