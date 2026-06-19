import os
import numpy as np
import pandas as pd
import joblib

from sklearn.preprocessing import MinMaxScaler

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

DATA = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "research_dataset.csv"
)

OUTPUT = os.path.join(
    BASE_DIR,
    "data",
    "processed"
)

SCALER = os.path.join(
    BASE_DIR,
    "trained_models",
    "scaler.pkl"
)

os.makedirs(os.path.dirname(SCALER), exist_ok=True)

# ==========================================================
# LOAD DATA
# ==========================================================

df = pd.read_csv(DATA)

# ==========================================================
# FEATURES
# ==========================================================

features = [

    "Construction",

    "PeakHour",

    "RouteLength",

    "TravelTime",

    "WaitingTime",

    "AverageSpeed"

]

target = "CongestionLevel"

X = df[features].values

y = df[target].values

# ==========================================================
# NORMALIZATION
# ==========================================================

scaler = MinMaxScaler()

X = scaler.fit_transform(X)

joblib.dump(scaler, SCALER)

# ==========================================================
# CREATE SEQUENCES
# ==========================================================

TIME_STEPS = 5

X_seq = []

y_seq = []

for i in range(len(X) - TIME_STEPS):

    X_seq.append(

        X[i:i + TIME_STEPS]

    )

    y_seq.append(

        y[i + TIME_STEPS]

    )

X_seq = np.array(X_seq)

y_seq = np.array(y_seq)

# ==========================================================
# SAVE
# ==========================================================

np.save(

    os.path.join(
        OUTPUT,
        "X_sequence.npy"
    ),

    X_seq

)

np.save(

    os.path.join(
        OUTPUT,
        "y_sequence.npy"
    ),

    y_seq

)

print("=" * 60)

print("Sequence Dataset Generated")

print("=" * 60)

print()

print("X Shape :", X_seq.shape)

print("y Shape :", y_seq.shape)

print()

print("Scaler Saved")

print(SCALER)