# Fraud Detection Model: Logistic Regression vs XGBoost

A machine learning project that builds and compares two classification models — Logistic Regression and XGBoost — for detecting fraudulent transactions, with a focus on evaluating performance beyond simple accuracy.

## Overview

Fraud detection datasets are highly imbalanced, where the vast majority of transactions are legitimate. This project goes beyond accuracy scores and evaluates models based on false positive rates, since flagging too many genuine transactions as fraud has real business costs.

## Models Compared

| Model | Accuracy | False Fraud Flags (False Positives) |
|---|---|---|
| Logistic Regression | 94% | 1,03,092 |
| XGBoost | 99% | 217 |

XGBoost significantly reduced false positives while improving overall accuracy, and was further optimized through hyperparameter tuning.

## Project Structure

```
.
├── analysis_model.ipynb              # Main notebook: data analysis, training & evaluation
├── analysis_model - Copy.ipynb       # XGBoost model notebook
├── frauddetection.py                 # Script version of the fraud detection pipeline
├── fraud_detection_model.pkl         # Saved Logistic Regression model
├── fraud_detection_model_XGBOOST.pkl # Saved XGBoost model
├── requirements.txt                  # Project dependencies
└── .gitignore
```

## Key Steps

1. Data preprocessing and exploratory analysis
2. Training a Logistic Regression baseline model
3. Training an XGBoost model
4. Hyperparameter tuning on XGBoost to improve performance and reduce false positives
5. Comparing both models on accuracy and false positive rates

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Open `analysis_model.ipynb` to walk through the data analysis and model training process, or run `frauddetection.py` for the script-based pipeline. Pre-trained models are available as `.pkl` files for direct inference.

## Results & Insights

While both models achieved high accuracy, the false positive comparison revealed a major practical difference: Logistic Regression flagged far more legitimate transactions as fraudulent than XGBoost, making XGBoost the more reliable model for real-world deployment.
