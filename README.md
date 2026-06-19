# AI Metro Digital Twin

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-EC6B23)](https://xgboost.readthedocs.io/)
[![SUMO](https://img.shields.io/badge/SUMO-Traffic%20Simulation-2E7D32)](https://www.eclipse.org/sumo/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

AI Metro Digital Twin is a research-focused urban mobility platform that combines SUMO traffic simulation, OpenStreetMap road networks, machine learning prediction models, and an interactive dashboard to analyze metro construction impacts and recommend traffic mitigation strategies.

## Description

A SUMO and AI-powered digital twin for simulating metro construction traffic disruption, predicting congestion, and evaluating mitigation strategies.

This project builds a digital twin of an urban traffic corridor using OpenStreetMap data and SUMO simulation outputs, then transforms scenario-level mobility data into machine learning datasets for congestion prediction. It compares XGBoost, Random Forest, LSTM, and GRU models, generates performance reports, and supports decision-making through an AI mitigation engine and Streamlit dashboard.

## Project Overview

AI Metro Digital Twin models normal, metro construction, and peak-hour traffic conditions to quantify how infrastructure work affects urban mobility. The system generates traffic simulation outputs, engineers research-ready features, trains prediction models, compares performance, and recommends congestion mitigation strategies.

The repository is organized for reproducible research, GitHub presentation, and future extension into a larger smart-city decision support system.

## Problem Statement

Metro construction can disrupt existing traffic networks through lane closures, rerouting pressure, increased waiting time, lower average speed, and higher travel-time uncertainty. Traditional traffic analysis often studies these impacts after deployment or with limited static assumptions.

This project addresses the need for a digital twin that can simulate construction scenarios, generate measurable mobility indicators, predict congestion, and support proactive mitigation planning.

## Project Objectives

- Build a SUMO-based traffic digital twin from OpenStreetMap data.
- Simulate normal, metro construction, and peak-hour mobility scenarios.
- Generate structured datasets from simulation output XML files.
- Engineer congestion-related features such as travel time, waiting time, route length, and average speed.
- Train and compare XGBoost, Random Forest, LSTM, and GRU models.
- Generate evaluation reports and model comparison visualizations.
- Recommend mitigation strategies using predicted congestion levels.
- Provide a Streamlit dashboard for scenario comparison.

## Complete System Architecture

```text
OpenStreetMap Road Network
        |
        v
SUMO Network and Route Generation
        |
        v
Traffic Simulation Scenarios
Normal | Metro Construction | Peak Hour
        |
        v
Simulation Output XML
tripinfo | summary | emission
        |
        v
Dataset Generation and Feature Engineering
        |
        v
Prediction Models
XGBoost | Random Forest | LSTM | GRU
        |
        v
Evaluation and Comparison
MAE | RMSE | R2 | Scenario Metrics
        |
        v
AI Mitigation Engine and Dashboard
```

## Technology Stack

- **Language:** Python
- **Simulation:** Eclipse SUMO
- **Map Data:** OpenStreetMap
- **Data Processing:** NumPy, Pandas
- **Machine Learning:** Scikit-learn, XGBoost
- **Deep Learning:** TensorFlow/Keras
- **Visualization:** Matplotlib, Streamlit
- **Model Persistence:** Joblib
- **Research Output:** IEEE-style paper draft folder

## Project Workflow

1. Generate or import SUMO-compatible network data from OpenStreetMap.
2. Generate routes for normal and peak-hour traffic.
3. Run SUMO scenarios for normal, construction, and peak-hour conditions.
4. Parse SUMO XML outputs into structured CSV datasets.
5. Engineer model-ready features and sequence data.
6. Train XGBoost, Random Forest, LSTM, and GRU models.
7. Compare models using MAE, RMSE, and R2 score.
8. Run the mitigation engine to estimate improved congestion.
9. Launch the dashboard to inspect scenario-level results.

## Folder Structure

```text
AI_Metro_Digital_Twin/
|-- config/
|-- dashboard/
|-- data/
|   |-- raw/
|   |-- processed/
|   `-- simulation_output/
|-- docs/
|   `-- images/
|-- models/
|-- notebooks/
|-- osm/
|-- paper/
|-- results/
|-- src/
|   |-- preprocessing/
|   |-- feature_engineering/
|   |-- prediction/
|   |-- optimization/
|   |-- evaluation/
|   `-- utils/
|-- sumo/
|-- trained_models/
|-- README.md
|-- requirements.txt
|-- LICENSE
|-- CONTRIBUTING.md
`-- CHANGELOG.md
```

## Implemented Features

- SUMO digital twin for traffic simulation.
- OpenStreetMap-based road network integration.
- Metro construction scenario modeling.
- Peak-hour traffic scenario modeling.
- Simulation output collection for trip, summary, and emission data.
- Dataset generation from SUMO XML output.
- Feature engineering for congestion prediction.
- XGBoost regression model.
- Random Forest regression model.
- LSTM sequence model.
- GRU sequence model.
- Model comparison reports and plots.
- AI mitigation engine for congestion reduction recommendations.
- Streamlit dashboard for scenario comparison.

## Project Statistics

| Category | Count / Status |
| --- | --- |
| ML models implemented | 4 |
| Prediction models | XGBoost, Random Forest, LSTM, GRU |
| Simulation engine | Eclipse SUMO |
| Digital twin scenarios | Normal, Metro Construction, Peak Hour |
| Dashboard | Streamlit |
| Mitigation engine | Implemented |

## Results

### Model Performance

| Model | MAE | RMSE | R2 |
| --- | ---: | ---: | ---: |
| Random Forest | 0.0191 | 0.0299 | 0.9939 |
| XGBoost | 0.0197 | 0.0303 | 0.9937 |
| LSTM | 0.2186 | 0.2746 | 0.4671 |
| GRU | 0.2151 | 0.2772 | 0.4569 |

### Scenario Impact

| Metric | Observed Construction Impact |
| --- | ---: |
| Vehicle count | +0.33% |
| Average duration | +1.56% |
| Average waiting time | +2.59% |
| Average time loss | +2.94% |
| Average speed | -2.50% |

### Mitigation Summary

The mitigation engine estimates an average predicted congestion of `0.5113`, average expected congestion of `0.2613`, and an estimated improvement of approximately `48.90%` after applying strategy recommendations.

## Screenshots

Screenshots and visual documentation should be stored in `docs/images/`.

| Asset | Location |
| --- | --- |
| Dashboard screenshot placeholder | `docs/images/dashboard-placeholder.md` |
| Results visualization placeholder | `docs/images/results-placeholder.md` |
| Generated plots | `results/` |

## Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/27Shambhavi/AI-Metro-Digital-Twin.git
cd AI-Metro-Digital-Twin
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install SUMO

Install Eclipse SUMO from the official website and update SUMO paths in the scripts if your installation path differs from the default Windows path used in this project.

## How to Run

### Run SUMO simulation

```bash
python sumo/run_simulation.py
```

### Generate datasets

```bash
python src/preprocessing/dataset_generator.py
python src/feature_engineering/feature_extractor.py
python src/preprocessing/sequence_generator.py
```

### Train prediction models

```bash
python models/xgboost_model.py
python models/random_forest_model.py
python models/lstm_model.py
python models/gru_model.py
```

### Compare models

```bash
python models/compare_all_models
```

### Run mitigation engine

```bash
python src/optimization/diversion_strategy.py
python src/evaluation/perfomance_report.py
```

### Launch dashboard

```bash
streamlit run dashboard/streamlit_app.py
```

## Future Scope

- Add real-time traffic feeds for live digital twin synchronization.
- Extend the scenario engine with weather, incidents, public events, and adaptive signal timing.
- Add explainability reports for model decisions.
- Integrate geospatial dashboard layers.
- Improve route choice modeling and dynamic traffic assignment.
- Package model training as configurable experiments.
- Add automated tests and continuous integration.

## GitHub Topics

`digital-twin` `sumo` `traffic-simulation` `machine-learning` `deep-learning` `smart-city` `urban-mobility` `xgboost` `tensorflow` `streamlit` `python` `ieee`

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements

- Eclipse SUMO for microscopic traffic simulation.
- OpenStreetMap contributors for map data.
- TensorFlow, XGBoost, Scikit-learn, Pandas, NumPy, Matplotlib, and Streamlit communities.
