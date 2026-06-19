import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# ===================================================
# Page Configuration
# ===================================================

st.set_page_config(
    page_title="AI Metro Digital Twin",
    layout="wide"
)

st.title("🚇 AI-Based Intelligent Traffic Mitigation Framework")

st.subheader("Metro Construction Impact Dashboard")

# ===================================================
# Paths
# ===================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

RESULT = os.path.join(
    BASE_DIR,
    "results",
    "scenario_comparison.csv"
)

df = pd.read_csv(RESULT)

# ===================================================
# Show Table
# ===================================================

st.header("Scenario Comparison")

st.dataframe(df)

# ===================================================
# Bar Chart
# ===================================================

fig, ax = plt.subplots(figsize=(10,5))

x = range(len(df))

width = 0.35

ax.bar(
    [i-width/2 for i in x],
    df["Normal"],
    width,
    label="Normal"
)

ax.bar(
    [i+width/2 for i in x],
    df["Construction"],
    width,
    label="Construction"
)

ax.set_xticks(x)

ax.set_xticklabels(df["Metric"], rotation=20)

ax.legend()

st.pyplot(fig)

# ===================================================
# Percentage Change
# ===================================================

st.header("Percentage Change")

st.dataframe(df[["Metric","% Change"]])

# ===================================================
# Worst Metric
# ===================================================

worst = df.loc[df["% Change"].idxmax()]

st.error(
    f"""
Worst Impact:

{worst['Metric']}

Change = {worst['% Change']:.2f} %
"""
)