import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ======================================================
# PATHS
# ======================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "research_dataset.csv"
)

XGB_MODEL = os.path.join(
    BASE_DIR,
    "trained_models",
    "research_xgboost.pkl"
)

RF_MODEL = os.path.join(
    BASE_DIR,
    "trained_models",
    "random_forest.pkl"
)

RESULT_CSV = os.path.join(
    BASE_DIR,
    "results",
    "model_comparison.csv"
)

RESULT_PNG = os.path.join(
    BASE_DIR,
    "results",
    "model_comparison.png"
)

# ======================================================
# LOAD DATA
# ======================================================

df = pd.read_csv(DATA)

features = [

    "Construction",

    "PeakHour",

    "RouteLength",

    "TravelTime",

    "WaitingTime",

    "AverageSpeed"

]

target = "CongestionLevel"

X = df[features]

y = df[target]

# ======================================================
# LOAD MODELS
# ======================================================

models = {

    "XGBoost": joblib.load(XGB_MODEL),

    "Random Forest": joblib.load(RF_MODEL)

}

results = []

# ======================================================
# EVALUATION
# ======================================================

for name, model in models.items():

    prediction = model.predict(X)

    mae = mean_absolute_error(y, prediction)

    rmse = np.sqrt(mean_squared_error(y, prediction))

    r2 = r2_score(y, prediction)

    results.append({

        "Model": name,

        "MAE": mae,

        "RMSE": rmse,

        "R2": r2

    })

result_df = pd.DataFrame(results)

print(result_df)

result_df.to_csv(

    RESULT_CSV,

    index=False

)

# ======================================================
# GRAPH
# ======================================================

plt.figure(figsize=(7,5))

plt.bar(

    result_df["Model"],

    result_df["R2"]

)

plt.title("Model Comparison")

plt.ylabel("R2 Score")

plt.tight_layout()

plt.savefig(RESULT_PNG)

plt.show()

print("\nSaved Results")

print(RESULT_CSV)

print(RESULT_PNG)