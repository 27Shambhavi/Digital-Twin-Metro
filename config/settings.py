"""
Configuration settings for Digital Twin project
"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SIMULATION_OUTPUT_DIR = DATA_DIR / "simulation_output"
MODELS_DIR = PROJECT_ROOT / "trained_models"
RESULTS_DIR = PROJECT_ROOT / "results"

# SUMO configuration
SUMO_CONFIG = PROJECT_ROOT / "sumo" / "simulation.sumocfg"
OSM_MAP = PROJECT_ROOT / "osm" / "indore.net.xml"
ROUTES_FILE = PROJECT_ROOT / "osm" / "routes.rou.xml"

# Model configuration
XGBOOST_MODEL_PATH = MODELS_DIR / "xgboost_model.pkl"
LSTM_MODEL_PATH = MODELS_DIR / "lstm_model.h5"
GRU_MODEL_PATH = MODELS_DIR / "gru_model.h5"

# Simulation scenarios
SCENARIOS = ["normal", "construction", "rain", "peak_hour"]
