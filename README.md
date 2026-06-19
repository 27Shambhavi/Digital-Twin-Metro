# 🚦 ML-Driven Digital Twin for Traffic Prediction and Mitigation in Metro Construction Zones

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-EC6B23)](https://xgboost.readthedocs.io/)
[![SUMO](https://img.shields.io/badge/SUMO-Traffic%20Simulation-2E7D32)](https://www.eclipse.org/sumo/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


A Digital Twin framework that combines **SUMO traffic simulation**, **Machine Learning**, and **Deep Learning** to analyze, predict, and mitigate traffic congestion caused by metro construction activities.

The project creates a virtual representation of an urban road network, simulates multiple traffic scenarios, generates research datasets, trains predictive models, and recommends mitigation strategies through an interactive dashboard.

---

# 📌 Problem Statement

Metro rail construction frequently causes lane closures, reduced road capacity, traffic congestion, longer travel times, increased fuel consumption, and higher emissions.

Conventional traffic management is mostly reactive, where mitigation measures are applied only after congestion has already occurred.

This project proposes a **Digital Twin-based Decision Support Framework** capable of simulating construction scenarios, predicting congestion using Machine Learning models, and recommending traffic mitigation strategies before severe congestion develops.

---

# 🎯 Objectives

* Develop a Digital Twin of an urban road network using SUMO.
* Simulate multiple traffic scenarios including normal, construction, and peak-hour traffic.
* Generate a structured traffic dataset from simulation outputs.
* Engineer relevant traffic features for congestion prediction.
* Compare Machine Learning and Deep Learning models for traffic prediction.
* Recommend mitigation strategies based on predicted congestion.
* Provide an interactive dashboard for traffic analysis and decision support.

---

# 🏗️ System Workflow

```text
OpenStreetMap
        │
        ▼
SUMO Digital Twin
        │
        ▼
Traffic Scenario Simulation
        │
        ▼
Traffic Dataset Generation
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning & Deep Learning
(XGBoost • Random Forest • LSTM • GRU)
        │
        ▼
Congestion Prediction
        │
        ▼
Mitigation Recommendation
        │
        ▼
Interactive Dashboard
```

---

# ⚙️ Technology Stack

## Simulation

* SUMO
* OpenStreetMap
* NetEdit

## Programming

* Python 3.10+

## Machine Learning

* XGBoost
* Random Forest

## Deep Learning

* TensorFlow
* Keras
* LSTM
* GRU

## Data Processing

* NumPy
* Pandas
* Scikit-learn

## Visualization

* Matplotlib
* Streamlit

---

# 📂 Project Structure

```text
AI_Metro_Digital_Twin/

├── config/
├── dashboard/
├── data/
│   ├── raw/
│   ├── processed/
│   └── simulation_output/
├── docs/
├── models/
├── notebooks/
├── osm/
├── paper/
├── results/
├── src/
│   ├── preprocessing/
│   ├── feature_engineering/
│   ├── prediction/
│   ├── optimization/
│   ├── evaluation/
│   └── utils/
├── sumo/
├── trained_models/
├── README.md
├── requirements.txt
└── LICENSE
```

---


# 🚦 Implemented Features

* Digital Twin creation using SUMO
* OpenStreetMap road network integration
* Metro construction traffic simulation
* Peak-hour traffic simulation
* Dataset generation from simulation outputs
* Feature engineering pipeline
* XGBoost implementation
* Random Forest implementation
* LSTM implementation
* GRU implementation
* Model comparison
* Traffic mitigation engine
* Interactive Streamlit dashboard

---
#📍**Case Study**

The proposed framework was evaluated using a real-world case study of Vijay Nagar Square, Indore, Madhya Pradesh, India, one of the city's busiest traffic intersections and a major commercial corridor.

The road network was extracted from OpenStreetMap (OSM) and converted into a SUMO-compatible network to create a Digital Twin of the study area. Multiple traffic scenarios were simulated, including:

- Normal Traffic Scenario
- Metro Construction Scenario (lane closure to emulate construction activity)
- Peak Hour Traffic Scenario

Simulation outputs such as vehicle travel time, waiting time, average speed, route length, and congestion metrics were collected and processed into a structured dataset for Machine Learning and Deep Learning model training.

This real-world case study demonstrates the applicability of the proposed framework for evaluating the impact of metro construction on urban traffic and supporting data-driven traffic management decisions.

## 🗺️ Study Area

**Location:** Vijay Nagar Square, Indore, Madhya Pradesh, India

**Road Network Source:** OpenStreetMap (OSM)

**Simulation Platform:** SUMO (Simulation of Urban MObility)

**Study Objective:** Analyze the impact of metro construction on traffic flow and evaluate congestion prediction and mitigation strategies.



# 📊 Model Performance

| Model         |    MAE |   RMSE |     R² |
| ------------- | -----: | -----: | -----: |
| XGBoost       | 0.0095 | 0.0163 | 0.9981 |
| Random Forest | 0.0099 | 0.0172 | 0.9979 |
| LSTM          | 0.2186 | 0.2746 | 0.4671 |
| GRU           | 0.2151 | 0.2772 | 0.4569 |

**Observation**

Tree-based ensemble models (XGBoost and Random Forest) achieved the highest predictive performance on the generated simulation dataset, while recurrent neural networks (LSTM and GRU) showed comparatively lower performance due to the limited temporal dependency in the current dataset.

---

# 📈 Dashboard

The dashboard provides:

* Scenario comparison
* Traffic impact analysis
* Model performance comparison
* Mitigation recommendations
* Dataset exploration
* Prediction analytics

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/AI-Metro-Digital-Twin.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Generate traffic routes

```bash
python sumo/generate_routes.py
```

Run traffic simulation

```bash
python sumo/run_simulation.py
```

Generate dataset

```bash
python src/preprocessing/feature_extractor.py
```

Train models

```bash
python models/xgboost_model.py

python models/random_forest_model.py

python models/lstm_model.py

python models/gru_model.py
```

Launch dashboard

```bash
streamlit run dashboard/streamlit_app.py
```
https://digital-twin-metro-ksms66hbclgb27r5xy59lp.streamlit.app/
---

# 📖 Research Contribution

This work integrates:

* Digital Twin technology
* Traffic simulation
* Machine Learning
* Deep Learning
* Decision Support

into a unified framework for predicting and mitigating congestion caused by metro construction activities.

---

# 🔮 Future Work

* Real-time traffic sensor integration
* Weather-aware traffic prediction
* Automatic scenario generation
* Reinforcement Learning for adaptive signal control
* Explainable Machine Learning (SHAP)
* Cloud deployment
* IoT integration
* Closed-loop Digital Twin optimization

---

# 📜 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Shambhavi Jha**

Machine Learning | Data Science | Intelligent Transportation Systems | Digital Twins

