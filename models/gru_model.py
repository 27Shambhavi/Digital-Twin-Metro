import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    GRU,
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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA = os.path.join(
    BASE_DIR,
    "data",
    "processed"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "trained_models"
)

RESULT_DIR = os.path.join(
    BASE_DIR,
    "results"
)

os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

# ======================================================
# LOAD DATA
# ======================================================

X = np.load(os.path.join(DATA, "X_sequence.npy"))
y = np.load(os.path.join(DATA, "y_sequence.npy"))

print("=" * 60)
print("Sequence Dataset Loaded")
print("=" * 60)

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

# ======================================================
# MODEL
# ======================================================

model = Sequential()

model.add(
    GRU(
        64,
        return_sequences=True,
        input_shape=(X.shape[1], X.shape[2])
    )
)

model.add(Dropout(0.2))

model.add(
    GRU(
        32
    )
)

model.add(Dropout(0.2))

model.add(
    Dense(
        16,
        activation="relu"
    )
)

model.add(Dense(1))

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

model.summary()

# ======================================================
# CALLBACKS
# ======================================================

checkpoint = ModelCheckpoint(
    os.path.join(MODEL_DIR, "gru.keras"),
    save_best_only=True,
    monitor="val_loss"
)

early = EarlyStopping(
    patience=10,
    restore_best_weights=True
)

# ======================================================
# TRAIN
# ======================================================

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=50,
    batch_size=32,
    callbacks=[checkpoint, early],
    verbose=1
)

# ======================================================
# PREDICT
# ======================================================

prediction = model.predict(X_test).flatten()

# ======================================================
# METRICS
# ======================================================

mae = mean_absolute_error(y_test, prediction)

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
print("GRU RESULTS")
print("="*60)

print(f"MAE  : {mae:.6f}")
print(f"RMSE : {rmse:.6f}")
print(f"R²   : {r2:.6f}")

# ======================================================
# SAVE RESULTS
# ======================================================

pd.DataFrame({

    "Model":["GRU"],

    "MAE":[mae],

    "RMSE":[rmse],

    "R2":[r2]

}).to_csv(

    os.path.join(
        RESULT_DIR,
        "gru_results.csv"
    ),

    index=False

)

# ======================================================
# LOSS GRAPH
# ======================================================

plt.figure(figsize=(8,5))

plt.plot(history.history["loss"],label="Train")

plt.plot(history.history["val_loss"],label="Validation")

plt.legend()

plt.title("GRU Loss")

plt.savefig(

    os.path.join(
        RESULT_DIR,
        "gru_loss.png"
    )

)

plt.show()

# ======================================================
# PREDICTION GRAPH
# ======================================================

plt.figure(figsize=(8,5))

plt.plot(y_test[:100],label="Actual")

plt.plot(prediction[:100],label="Predicted")

plt.legend()

plt.title("GRU Prediction")

plt.savefig(

    os.path.join(
        RESULT_DIR,
        "gru_prediction.png"
    )

)

plt.show()

print("\nGRU Completed Successfully.")