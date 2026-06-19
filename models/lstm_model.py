import os
import joblib
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    LSTM,
    Dense,
    Dropout
)

from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint
)

# ======================================================
# PATHS
# ======================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA = os.path.join(
    BASE_DIR,
    "data",
    "processed"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "trained_models"
)

os.makedirs(MODEL_DIR, exist_ok=True)

# ======================================================
# LOAD DATA
# ======================================================

X = np.load(
    os.path.join(
        DATA,
        "X_sequence.npy"
    )
)

y = np.load(
    os.path.join(
        DATA,
        "y_sequence.npy"
    )
)

print("="*60)
print("Sequence Dataset Loaded")
print("="*60)

print("X Shape :", X.shape)
print("y Shape :", y.shape)

# ======================================================
# TRAIN TEST SPLIT
# ======================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42

)

print()

print("Training Samples :", len(X_train))

print("Testing Samples :", len(X_test))

# ======================================================
# MODEL
# ======================================================

model = Sequential()

model.add(

    LSTM(

        64,

        input_shape=(

            X.shape[1],

            X.shape[2]

        ),

        return_sequences=True

    )

)

model.add(

    Dropout(0.2)

)

model.add(

    LSTM(

        32

    )

)

model.add(

    Dropout(0.2)

)

model.add(

    Dense(

        16,

        activation="relu"

    )

)

model.add(

    Dense(

        1

    )

)

model.compile(

    optimizer="adam",

    loss="mse",

    metrics=["mae"]

)

print()

model.summary()
# ======================================================
# CALLBACKS
# ======================================================

checkpoint_path = os.path.join(
    MODEL_DIR,
    "lstm.keras"
)

early_stop = EarlyStopping(

    monitor="val_loss",

    patience=10,

    restore_best_weights=True

)

checkpoint = ModelCheckpoint(

    checkpoint_path,

    monitor="val_loss",

    save_best_only=True,

    verbose=1

)

# ======================================================
# TRAIN MODEL
# ======================================================

print("\nTraining LSTM...\n")

history = model.fit(

    X_train,

    y_train,

    validation_split=0.2,

    epochs=50,

    batch_size=32,

    callbacks=[early_stop, checkpoint],

    verbose=1

)

# ======================================================
# PREDICTION
# ======================================================

prediction = model.predict(X_test)

prediction = prediction.flatten()

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

print("\n")

print("="*60)

print("LSTM RESULTS")

print("="*60)

print(f"MAE  : {mae:.6f}")

print(f"RMSE : {rmse:.6f}")

print(f"R²   : {r2:.6f}")

# ======================================================
# SAVE TRAINING CURVE
# ======================================================

plt.figure(figsize=(8,5))

plt.plot(

    history.history["loss"],

    label="Training Loss"

)

plt.plot(

    history.history["val_loss"],

    label="Validation Loss"

)

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.title("LSTM Training Curve")

plt.legend()

plt.tight_layout()

plt.savefig(

    os.path.join(

        BASE_DIR,

        "results",

        "lstm_loss.png"

    )

)

plt.show()

# ======================================================
# PREDICTION GRAPH
# ======================================================

plt.figure(figsize=(8,5))

plt.plot(

    y_test[:100],

    label="Actual"

)

plt.plot(

    prediction[:100],

    label="Predicted"

)

plt.xlabel("Samples")

plt.ylabel("Congestion Level")

plt.title("LSTM Prediction")

plt.legend()

plt.tight_layout()

plt.savefig(

    os.path.join(

        BASE_DIR,

        "results",

        "lstm_prediction.png"

    )

)

plt.show()

# ======================================================
# SAVE METRICS
# ======================================================

results = {

    "Model":["LSTM"],

    "MAE":[mae],

    "RMSE":[rmse],

    "R2":[r2]

}

import pandas as pd

pd.DataFrame(results).to_csv(

    os.path.join(

        BASE_DIR,

        "results",

        "lstm_results.csv"

    ),

    index=False

)

print("\n")

print("="*60)

print("LSTM Training Completed Successfully")

print("="*60)

print("\nSaved Files")

print("------------------------------")

print("trained_models/lstm.keras")

print("results/lstm_loss.png")

print("results/lstm_prediction.png")

print("results/lstm_results.csv")