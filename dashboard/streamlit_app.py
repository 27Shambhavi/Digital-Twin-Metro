"""Streamlit dashboard for AI Metro Digital Twin research outputs."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parents[1]
RESULTS_DIR = BASE_DIR / "results"

SCENARIO_FILE = RESULTS_DIR / "scenario_comparison.csv"
MODEL_FILE = RESULTS_DIR / "model_comparison.csv"
PERFORMANCE_FILE = RESULTS_DIR / "performance_report.csv"
MITIGATION_FILE = RESULTS_DIR / "mitigation_results.csv"


st.set_page_config(
    page_title="AI Metro Digital Twin",
    page_icon="Metro",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    :root {
        --surface: #ffffff;
        --muted: #667085;
        --border: #e4e7ec;
        --ink: #101828;
        --blue: #2563eb;
        --green: #047857;
        --red: #b42318;
        --amber: #b54708;
        --slate: #344054;
    }

    .block-container {
        padding-top: 2.35rem;
        padding-bottom: 2.5rem;
        max-width: 1420px;
    }

    h1, h2, h3 {
        color: var(--ink);
        letter-spacing: 0;
    }

    .hero {
        border-bottom: 1px solid var(--border);
        padding: 0.25rem 0 1.25rem 0;
        margin-bottom: 1.15rem;
        overflow: visible;
    }

    .hero-title {
        font-size: 2.15rem;
        font-weight: 760;
        line-height: 1.28;
        margin: 0 0 0.45rem 0;
        padding-top: 0.18rem;
        overflow-wrap: anywhere;
    }

    .hero-copy {
        color: var(--muted);
        font-size: 1rem;
        max-width: 980px;
    }

    .ribbon-grid {
        display: grid;
        grid-template-columns: repeat(5, minmax(150px, 1fr));
        gap: 0.72rem;
        margin: 0.35rem 0 1.2rem 0;
    }

    .status-pill {
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 0.78rem 0.9rem;
        background: #ffffff;
        min-height: 82px;
    }

    .status-pill.active {
        border-color: #bbf7d0;
        background: #f0fdf4;
    }

    .status-pill.warn {
        border-color: #fed7aa;
        background: #fff7ed;
    }

    .status-pill.idle {
        border-color: #e4e7ec;
        background: #f8fafc;
    }

    .pill-label {
        color: var(--muted);
        font-size: 0.72rem;
        font-weight: 760;
        text-transform: uppercase;
        margin-bottom: 0.32rem;
    }

    .pill-value {
        color: var(--ink);
        font-size: 1.08rem;
        font-weight: 780;
        line-height: 1.18;
    }

    .pill-note {
        color: var(--muted);
        font-size: 0.78rem;
        margin-top: 0.28rem;
    }

    .stat-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 1rem 1.05rem;
        min-height: 122px;
    }

    .stat-label {
        color: var(--muted);
        font-size: 0.78rem;
        font-weight: 650;
        text-transform: uppercase;
        margin-bottom: 0.45rem;
    }

    .stat-value {
        color: var(--ink);
        font-size: 1.7rem;
        font-weight: 780;
        line-height: 1.08;
        word-break: break-word;
    }

    .stat-note {
        color: var(--muted);
        font-size: 0.86rem;
        margin-top: 0.45rem;
    }

    .status-good {
        color: var(--green);
        font-weight: 700;
    }

    .status-risk {
        color: var(--red);
        font-weight: 700;
    }

    .section-title {
        font-size: 1.05rem;
        font-weight: 760;
        margin: 0.35rem 0 0.65rem 0;
    }

    .insight-box {
        border-left: 4px solid var(--blue);
        background: #f8fafc;
        padding: 0.85rem 1rem;
        margin: 0.35rem 0 1rem 0;
        color: var(--ink);
    }

    .paper-result {
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        align-items: center;
        gap: 0.9rem;
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 1rem;
        background: #ffffff;
        margin-bottom: 1rem;
    }

    .result-node {
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
        border: 1px solid var(--border);
        background: #f8fafc;
    }

    .result-node.before {
        background: #fff7ed;
        border-color: #fed7aa;
    }

    .result-node.after {
        background: #f0fdf4;
        border-color: #bbf7d0;
    }

    .result-label {
        color: var(--muted);
        font-size: 0.78rem;
        font-weight: 760;
        text-transform: uppercase;
        margin-bottom: 0.35rem;
    }

    .result-value {
        color: var(--ink);
        font-size: 2.15rem;
        font-weight: 820;
        line-height: 1.05;
    }

    .result-arrow {
        color: var(--blue);
        font-size: 2.1rem;
        font-weight: 800;
    }

    .small-muted {
        color: var(--muted);
        font-size: 0.9rem;
    }

    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e4e7ec;
        border-radius: 8px;
        padding: 0.8rem 0.9rem;
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid #e4e7ec;
        border-radius: 8px;
    }

    @media (max-width: 900px) {
        .ribbon-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
        .paper-result {
            grid-template-columns: 1fr;
        }
        .result-arrow {
            transform: rotate(90deg);
            text-align: center;
        }
        .hero-title {
            font-size: 1.72rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


@st.cache_data
def load_csv(path):
    """Load a CSV if it exists and return an empty frame otherwise."""
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()


def format_number(value, suffix="", digits=2):
    """Format dashboard values consistently."""
    if pd.isna(value):
        return "N/A"
    return f"{value:,.{digits}f}{suffix}"


def impact_tone(value):
    """Return a readable impact label for scenario percentage deltas."""
    if value > 0:
        return "Increase"
    if value < 0:
        return "Decrease"
    return "No change"


def render_status_pill(label, value, note, tone="idle"):
    """Render a top-ribbon status indicator."""
    st.markdown(
        f"""
        <div class="status-pill {tone}">
            <div class="pill-label">{label}</div>
            <div class="pill-value">{value}</div>
            <div class="pill-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_stat_card(label, value, note, status=None):
    """Render a compact KPI card."""
    status_class = ""
    if status == "good":
        status_class = "status-good"
    elif status == "risk":
        status_class = "status-risk"

    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-label">{label}</div>
            <div class="stat-value {status_class}">{value}</div>
            <div class="stat-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_mitigation_result(before_value, after_value, improvement):
    """Render the headline before/after congestion result."""
    st.markdown(
        f"""
        <div class="paper-result">
            <div class="result-node before">
                <div class="result-label">Before mitigation</div>
                <div class="result-value">{before_value * 100:.1f}%</div>
                <div class="pill-note">Predicted congestion</div>
            </div>
            <div class="result-arrow">-></div>
            <div class="result-node after">
                <div class="result-label">After mitigation</div>
                <div class="result-value">{after_value * 100:.1f}%</div>
                <div class="pill-note">Expected congestion</div>
            </div>
        </div>
        <div class="insight-box">
            <strong>Paper-ready result:</strong> mitigation reduces average congestion by {improvement:.2f}% in the generated scenario output.
        </div>
        """,
        unsafe_allow_html=True
    )


def plot_scenario_bars(df):
    """Create the normal vs construction comparison bar chart."""
    fig, ax = plt.subplots(figsize=(10.8, 5.2))
    x_axis = range(len(df))
    width = 0.36

    ax.bar(
        [item - width / 2 for item in x_axis],
        df["Normal"],
        width,
        label="Normal",
        color="#2563eb"
    )
    ax.bar(
        [item + width / 2 for item in x_axis],
        df["Construction"],
        width,
        label="Construction",
        color="#f97316"
    )

    ax.set_xticks(list(x_axis))
    ax.set_xticklabels(df["Metric"], rotation=18, ha="right")
    ax.set_ylabel("Observed value")
    ax.set_title("Normal vs Metro Construction Scenario")
    ax.grid(axis="y", alpha=0.22)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False)
    fig.tight_layout()
    return fig


def plot_percent_change(df):
    """Create horizontal percentage-impact chart."""
    sorted_df = df.sort_values("% Change")
    colors = ["#047857" if value < 0 else "#b42318" for value in sorted_df["% Change"]]

    fig, ax = plt.subplots(figsize=(9.4, 4.8))
    ax.barh(sorted_df["Metric"], sorted_df["% Change"], color=colors)
    ax.axvline(0, color="#475467", linewidth=1)
    ax.set_xlabel("Change from normal scenario (%)")
    ax.set_title("Construction Impact by Metric")
    ax.grid(axis="x", alpha=0.2)
    ax.spines[["top", "right", "left"]].set_visible(False)
    fig.tight_layout()
    return fig


def plot_model_leaderboard(df):
    """Create model R2 leaderboard chart."""
    leaderboard = df.sort_values("R2", ascending=True)
    colors = [
        "#2563eb" if model == df.iloc[0]["Model"] else "#98a2b3"
        for model in leaderboard["Model"]
    ]

    fig, ax = plt.subplots(figsize=(8.5, 4.6))
    ax.barh(leaderboard["Model"], leaderboard["R2"], color=colors)
    ax.set_xlabel("R2 score")
    ax.set_title("Prediction Model Leaderboard")
    ax.set_xlim(0, max(1.0, leaderboard["R2"].max() + 0.05))
    ax.grid(axis="x", alpha=0.22)
    ax.spines[["top", "right", "left"]].set_visible(False)
    fig.tight_layout()
    return fig


def plot_mitigation_before_after(before_value, after_value):
    """Create a paper-friendly before/after mitigation chart."""
    fig, ax = plt.subplots(figsize=(8.4, 4.8))
    values = [before_value * 100, after_value * 100]
    labels = ["Before Mitigation", "After Mitigation"]
    colors = ["#f97316", "#047857"]

    bars = ax.bar(labels, values, color=colors, width=0.5)
    ax.set_ylim(0, max(values) * 1.28)
    ax.set_ylabel("Average congestion (%)")
    ax.set_title("Congestion Reduction After AI Mitigation")
    ax.grid(axis="y", alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(values) * 0.035,
            f"{value:.1f}%",
            ha="center",
            va="bottom",
            fontsize=12,
            fontweight="bold"
        )

    ax.annotate(
        "reduced",
        xy=(1, values[1]),
        xytext=(0, values[0]),
        arrowprops={"arrowstyle": "->", "color": "#2563eb", "lw": 2.2},
        color="#2563eb",
        fontsize=11,
        fontweight="bold",
        ha="center"
    )
    fig.tight_layout()
    return fig


scenario_df = load_csv(SCENARIO_FILE)
model_df = load_csv(MODEL_FILE)
performance_df = load_csv(PERFORMANCE_FILE)
mitigation_df = load_csv(MITIGATION_FILE)

with st.sidebar:
    st.markdown("### AI Metro Digital Twin")
    st.caption("Research dashboard")
    st.divider()
    st.markdown("**Data status**")
    st.write("Scenario comparison", "Available" if not scenario_df.empty else "Missing")
    st.write("Model comparison", "Available" if not model_df.empty else "Missing")
    st.write("Mitigation report", "Available" if not performance_df.empty else "Missing")
    st.divider()
    st.markdown("**System components**")
    st.write("SUMO digital twin")
    st.write("OpenStreetMap network")
    st.write("XGBoost, Random Forest, LSTM, GRU")
    st.write("AI mitigation engine")

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">AI Metro Digital Twin Dashboard</div>
        <div class="hero-copy">
            Advanced scenario monitoring, congestion prediction, and mitigation evidence for metro construction traffic impact research.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

if scenario_df.empty:
    st.error("Scenario comparison data is missing. Run src/evaluation/compare_scenarios.py first.")
    st.stop()

worst_row = scenario_df.loc[scenario_df["% Change"].abs().idxmax()]
waiting_row = scenario_df[scenario_df["Metric"] == "Avg Waiting (s)"].iloc[0]
speed_row = scenario_df[scenario_df["Metric"] == "Avg Speed (m/s)"].iloc[0]
best_model = model_df.sort_values("R2", ascending=False).iloc[0] if not model_df.empty else None
report = performance_df.iloc[0] if not performance_df.empty else None

ribbon_cols = st.columns(5)
with ribbon_cols[0]:
    render_status_pill("Current scenario", "Construction", "Metro work-zone impact view", "warn")
with ribbon_cols[1]:
    render_status_pill("Simulation", "Running", "Latest SUMO outputs loaded", "active")
with ribbon_cols[2]:
    render_status_pill("Construction", "Enabled", "Lane disruption scenario", "warn")
with ribbon_cols[3]:
    render_status_pill("Peak hour", "Enabled", "High-demand route set available", "active")
with ribbon_cols[4]:
    render_status_pill("Rain", "Planned", "Future scenario extension", "idle")

if report is not None:
    render_mitigation_result(
        report["Average Predicted Congestion"],
        report["Average Expected Congestion"],
        report["Average Improvement (%)"]
    )

stat_cols = st.columns(4)
with stat_cols[0]:
    render_stat_card(
        "Digital twin scenarios",
        "3",
        "Normal, construction, and peak-hour simulation runs"
    )
with stat_cols[1]:
    render_stat_card(
        "Waiting impact",
        format_number(waiting_row["% Change"], "%"),
        f"{impact_tone(waiting_row['% Change'])} under construction",
        "risk" if waiting_row["% Change"] > 0 else "good"
    )
with stat_cols[2]:
    render_stat_card(
        "Speed impact",
        format_number(speed_row["% Change"], "%"),
        f"{impact_tone(speed_row['% Change'])} in average speed",
        "risk" if speed_row["% Change"] < 0 else "good"
    )
with stat_cols[3]:
    if best_model is not None:
        render_stat_card(
            "Best prediction model",
            best_model["Model"],
            f"R2 = {best_model['R2']:.4f}",
            "good"
        )
    else:
        render_stat_card("Best prediction model", "N/A", "Run model comparison first")

st.markdown(
    f"""
    <div class="insight-box">
        <strong>Highest scenario shift:</strong> {worst_row['Metric']} changed by {worst_row['% Change']:.2f}% between normal and construction simulation.
    </div>
    """,
    unsafe_allow_html=True
)

overview_tab, models_tab, mitigation_tab, data_tab = st.tabs(
    ["Scenario Overview", "Model Performance", "Mitigation Engine", "Data Tables"]
)

with overview_tab:
    left_col, right_col = st.columns([1.22, 1])
    with left_col:
        st.markdown('<div class="section-title">Scenario Comparison</div>', unsafe_allow_html=True)
        st.pyplot(plot_scenario_bars(scenario_df), use_container_width=True)
    with right_col:
        st.markdown('<div class="section-title">Construction Impact</div>', unsafe_allow_html=True)
        st.pyplot(plot_percent_change(scenario_df), use_container_width=True)

    metric_cols = st.columns(len(scenario_df))
    for index, row in scenario_df.iterrows():
        with metric_cols[index]:
            st.metric(
                label=row["Metric"],
                value=format_number(row["Construction"]),
                delta=format_number(row["% Change"], "%")
            )

with models_tab:
    if model_df.empty:
        st.warning("Model comparison data is missing. Run models/compare_all_models first.")
    else:
        model_df = model_df.sort_values("R2", ascending=False).reset_index(drop=True)
        chart_col, table_col = st.columns([1.05, 1])
        with chart_col:
            st.markdown('<div class="section-title">Prediction Leaderboard</div>', unsafe_allow_html=True)
            st.pyplot(plot_model_leaderboard(model_df), use_container_width=True)
        with table_col:
            st.markdown('<div class="section-title">Evaluation Metrics</div>', unsafe_allow_html=True)
            st.dataframe(
                model_df.style.format({
                    "MAE": "{:.4f}",
                    "RMSE": "{:.4f}",
                    "R2": "{:.4f}"
                }),
                use_container_width=True,
                hide_index=True
            )

        st.markdown('<div class="section-title">Saved Result Visualizations</div>', unsafe_allow_html=True)
        image_cols = st.columns(3)
        for col, image_name, caption in zip(
            image_cols,
            ["model_comparison.png", "mae_comparison.png", "rmse_comparison.png"],
            ["R2 comparison", "MAE comparison", "RMSE comparison"]
        ):
            image_path = RESULTS_DIR / image_name
            with col:
                if image_path.exists():
                    st.image(str(image_path), caption=caption, use_container_width=True)

with mitigation_tab:
    if performance_df.empty:
        st.warning("Mitigation report is missing. Run src/optimization/diversion_strategy.py and src/evaluation/perfomance_report.py first.")
    else:
        report = performance_df.iloc[0]
        before_value = report["Average Predicted Congestion"]
        after_value = report["Average Expected Congestion"]
        improvement = report["Average Improvement (%)"]

        cols = st.columns(4)
        cols[0].metric(
            "Before mitigation",
            format_number(before_value * 100, "%"),
            "Predicted congestion"
        )
        cols[1].metric(
            "After mitigation",
            format_number(after_value * 100, "%"),
            "Expected congestion"
        )
        cols[2].metric(
            "Estimated improvement",
            format_number(improvement, "%")
        )
        cols[3].metric(
            "Emergency cases",
            f"{int(report['Emergency Cases']):,}"
        )

        chart_col, table_col = st.columns([1.15, 1])
        with chart_col:
            st.markdown('<div class="section-title">Congestion Before vs After Mitigation</div>', unsafe_allow_html=True)
            st.pyplot(plot_mitigation_before_after(before_value, after_value), use_container_width=True)
        with table_col:
            st.markdown('<div class="section-title">Mitigation Summary</div>', unsafe_allow_html=True)
            st.dataframe(
                performance_df.style.format({
                    "Average Predicted Congestion": "{:.4f}",
                    "Average Expected Congestion": "{:.4f}",
                    "Average Improvement (%)": "{:.2f}%"
                }),
                use_container_width=True,
                hide_index=True
            )

        if not mitigation_df.empty:
            strategy_counts = mitigation_df["SuggestedStrategy"].value_counts().reset_index()
            strategy_counts.columns = ["Strategy", "Cases"]

            fig, ax = plt.subplots(figsize=(9.2, 4.6))
            ax.bar(strategy_counts["Strategy"], strategy_counts["Cases"], color="#2563eb")
            ax.set_ylabel("Number of cases")
            ax.set_title("Recommended Mitigation Strategies")
            ax.tick_params(axis="x", rotation=18)
            ax.grid(axis="y", alpha=0.22)
            ax.spines[["top", "right"]].set_visible(False)
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)

            st.dataframe(
                strategy_counts,
                use_container_width=True,
                hide_index=True
            )

with data_tab:
    st.markdown('<div class="section-title">Scenario Dataset</div>', unsafe_allow_html=True)
    st.dataframe(
        scenario_df.style.format({
            "Normal": "{:.4f}",
            "Construction": "{:.4f}",
            "% Change": "{:.2f}%"
        }),
        use_container_width=True,
        hide_index=True
    )

    if not mitigation_df.empty:
        st.markdown('<div class="section-title">Mitigation Sample</div>', unsafe_allow_html=True)
        st.dataframe(
            mitigation_df.head(100),
            use_container_width=True,
            hide_index=True
        )

st.caption("AI Metro Digital Twin | SUMO simulation, machine learning prediction, and mitigation analytics")
