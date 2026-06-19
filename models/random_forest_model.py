import os
import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ===================================================
# PATHS
# ===================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "research_dataset.csv"
)

MODEL = os.path.join(
    BASE_DIR,
    "trained_models",
    "random_forest.pkl"
)

os.makedirs(os.path.dirname(MODEL), exist_ok=True)

# ===================================================
# LOAD DATA
# ===================================================

df = pd.read_csv(DATA)

print("=" * 60)
print("Research Dataset")
print("=" * 60)

print(df.head())

# ===================================================
# FEATURES
# ===================================================

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

# ===================================================
# TRAIN TEST SPLIT
# ===================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42

)

# ===================================================
# MODEL
# ===================================================

model = RandomForestRegressor(

    n_estimators=300,

    max_depth=12,

    random_state=42,

    n_jobs=-1

)

print("\nTraining Random Forest...\n")

model.fit(

    X_train,

    y_train

)

# ===================================================
# PREDICTION
# ===================================================

prediction = model.predict(X_test)

# ===================================================
# METRICS
# ===================================================

mae = mean_absolute_error(

    y_test,

    prediction

)

rmse = np.sqrt(

    mean_squared_error(

        y_test,

        prediction

    )

)

r2 = r2_score(

    y_test,

    prediction

)

print("="*60)

print("RANDOM FOREST RESULTS")

print("="*60)

print(f"MAE  : {mae:.4f}")

print(f"RMSE : {rmse:.4f}")

print(f"R²   : {r2:.4f}")

# ===================================================
# SAVE
# ===================================================

joblib.dump(

    model,

    MODEL

)

# ======================================================
# SAVE RESULTS
# ======================================================

RESULT_DIR = os.path.join(
    BASE_DIR,
    "results"
)

os.makedirs(RESULT_DIR, exist_ok=True)

result = pd.DataFrame({

    "Model": ["Random Forest"],

    "MAE": [mae],

    "RMSE": [rmse],

    "R2": [r2]

})

result.to_csv(

    os.path.join(

        RESULT_DIR,

        "random_forest_results.csv"

    ),

    index=False

)

print("\nSaved Results CSV")