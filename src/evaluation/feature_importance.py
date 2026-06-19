"""Plot feature importance for the trained XGBoost congestion model."""

import os

import joblib
import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

MODEL = os.path.join(
    BASE_DIR,
    "trained_models",
    "research_xgboost.pkl"
)

DATA = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "research_dataset.csv"
)

FEATURES = [
    "Construction",
    "PeakHour",
    "RouteLength",
    "TravelTime",
    "WaitingTime",
    "AverageSpeed"
]

model = joblib.load(MODEL)
df = pd.read_csv(DATA)
X = df[FEATURES]

importance = model.feature_importances_

plt.figure(figsize=(8, 5))
plt.bar(X.columns, importance)
plt.ylabel("Importance")
plt.title("Feature Importance")
plt.tight_layout()
plt.show()
