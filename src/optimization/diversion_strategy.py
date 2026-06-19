"""Generate congestion mitigation recommendations from predicted traffic state."""

import os

import joblib
import pandas as pd

# ============================================================
# PATHS
# ============================================================

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

OUTPUT = os.path.join(
    BASE_DIR,
    "results",
    "mitigation_results.csv"
)

FEATURES = [
    "Construction",
    "PeakHour",
    "RouteLength",
    "TravelTime",
    "WaitingTime",
    "AverageSpeed"
]

# ============================================================
# LOAD
# ============================================================

model = joblib.load(MODEL)
df = pd.read_csv(DATA)

# ============================================================
# PREDICT CONGESTION
# ============================================================

X = df[FEATURES]
df["PredictedCongestion"] = model.predict(X)

# ============================================================
# MITIGATION ENGINE
# ============================================================

strategy = []
improved = []

for congestion in df["PredictedCongestion"]:
    if congestion < 0.30:
        strategy.append("No Action")
        improved.append(congestion)
    elif congestion < 0.60:
        strategy.append("Traffic Diversion")
        improved.append(congestion * 0.80)
    elif congestion < 0.80:
        strategy.append("Diversion + Signal Optimization")
        improved.append(congestion * 0.60)
    else:
        strategy.append("Emergency Traffic Management")
        improved.append(congestion * 0.40)

df["SuggestedStrategy"] = strategy
df["ExpectedCongestion"] = improved

# ============================================================
# SAVE
# ============================================================

df.to_csv(
    OUTPUT,
    index=False
)

print("=" * 60)
print("AI Mitigation Engine Completed")
print("=" * 60)
print(df.head())
print()
print("Saved at")
print(OUTPUT)
