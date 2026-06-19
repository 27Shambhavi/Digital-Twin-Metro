import os
import joblib
import numpy as np
import pandas as pd

from xgboost import XGBRegressor

from sklearn.model_selection import train_test_split

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

MODEL = os.path.join(
    BASE_DIR,
    "trained_models",
    "research_xgboost.pkl"
)

os.makedirs(os.path.dirname(MODEL), exist_ok=True)

# ======================================================
# LOAD DATA
# ======================================================

df = pd.read_csv(DATA)

print("=" * 60)
print("Research Dataset Loaded")
print("=" * 60)

print(df.head())

# ======================================================
# FEATURES
# ======================================================

FEATURES = [

    "Construction",

    "PeakHour",

    "RouteLength",

    "TravelTime",

    "WaitingTime",

    "AverageSpeed"

]

TARGET = "CongestionLevel"

X = df[FEATURES]

y = df[TARGET]

# ======================================================
# SPLIT
# ======================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42

)

# ======================================================
# MODEL
# ======================================================

model = XGBRegressor(

    n_estimators=500,

    learning_rate=0.03,

    max_depth=6,

    subsample=0.8,

    colsample_bytree=0.8,

    random_state=42

)

print("\nTraining XGBoost...\n")

model.fit(

    X_train,

    y_train

)

# ======================================================
# PREDICTION
# ======================================================

prediction = model.predict(X_test)

# ======================================================
# METRICS
# ======================================================

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

print("=" * 60)

print("XGBOOST RESULTS")

print("=" * 60)

print(f"MAE  : {mae:.4f}")

print(f"RMSE : {rmse:.4f}")

print(f"R²   : {r2:.4f}")

# ======================================================
# SAVE MODEL
# ======================================================

joblib.dump(

    model,

    MODEL

)

# ======================================================
# SAVE RESULTS
# ======================================================

import pandas as pd

RESULT_DIR = os.path.join(
    BASE_DIR,
    "results"
)

os.makedirs(RESULT_DIR, exist_ok=True)

result = pd.DataFrame({

    "Model": ["XGBoost"],

    "MAE": [mae],

    "RMSE": [rmse],

    "R2": [r2]

})

result.to_csv(

    os.path.join(

        RESULT_DIR,

        "xgboost_results.csv"

    ),

    index=False

)

print("\nSaved Results CSV")