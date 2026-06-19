"""Create a performance report from mitigation engine output."""

import os

import pandas as pd

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

DATA = os.path.join(
    BASE_DIR,
    "results",
    "mitigation_results.csv"
)

REPORT = os.path.join(
    BASE_DIR,
    "results",
    "performance_report.csv"
)

df = pd.read_csv(DATA)

predicted_mean = df["PredictedCongestion"].mean()
expected_mean = df["ExpectedCongestion"].mean()

report = {
    "Average Predicted Congestion": predicted_mean,
    "Average Expected Congestion": expected_mean,
    "Average Improvement (%)": (
        (predicted_mean - expected_mean) / predicted_mean
    ) * 100,
    "Diversion Cases": (
        df["SuggestedStrategy"] == "Traffic Diversion"
    ).sum(),
    "Signal Optimization Cases": (
        df["SuggestedStrategy"] == "Diversion + Signal Optimization"
    ).sum(),
    "Emergency Cases": (
        df["SuggestedStrategy"] == "Emergency Traffic Management"
    ).sum()
}

result = pd.DataFrame(report, index=[0])

result.to_csv(
    REPORT,
    index=False
)

print(result)
print()
print("Performance Report Generated")
