import os
import xml.etree.ElementTree as ET
import pandas as pd

# ==========================================================
# PROJECT PATH
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

# ==========================================================
# INPUT FILES
# ==========================================================

NORMAL_FILE = os.path.join(
    BASE_DIR,
    "data",
    "simulation_output",
    "tripinfo.xml"
)

CONSTRUCTION_FILE = os.path.join(
    BASE_DIR,
    "data",
    "simulation_output",
    "construction_tripinfo.xml"
)

PEAK_FILE = os.path.join(
    BASE_DIR,
    "data",
    "simulation_output",
    "peak_tripinfo.xml"
)

# ==========================================================
# OUTPUT FILE
# ==========================================================

OUTPUT = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "research_dataset.csv"
)

# ==========================================================
# FUNCTION
# ==========================================================

def parse_tripinfo(file_path, construction, peak_hour):

    tree = ET.parse(file_path)

    root = tree.getroot()

    rows = []

    for trip in root.findall("tripinfo"):

        duration = float(trip.attrib.get("duration", 0))

        waiting = float(trip.attrib.get("waitingTime", 0))

        timeloss = float(trip.attrib.get("timeLoss", 0))

        route = float(trip.attrib.get("routeLength", 0))

        speed = 0

        if duration != 0:

            speed = route / duration

        congestion = waiting / duration if duration != 0 else 0

        rows.append({

            "Construction": construction,

            "PeakHour": peak_hour,

            "RouteLength": route,

            "TravelTime": duration,

            "WaitingTime": waiting,

            "TimeLoss": timeloss,

            "AverageSpeed": speed,

            "CongestionLevel": congestion

        })

    return rows


# ==========================================================
# LOAD ALL SCENARIOS
# ==========================================================

dataset = []

if os.path.exists(NORMAL_FILE):

    dataset.extend(
        parse_tripinfo(
            NORMAL_FILE,
            construction=0,
            peak_hour=0
        )
    )

if os.path.exists(CONSTRUCTION_FILE):

    dataset.extend(
        parse_tripinfo(
            CONSTRUCTION_FILE,
            construction=1,
            peak_hour=0
        )
    )

if os.path.exists(PEAK_FILE):

    dataset.extend(
        parse_tripinfo(
            PEAK_FILE,
            construction=0,
            peak_hour=1
        )
    )

# ==========================================================
# SAVE DATASET
# ==========================================================

df = pd.DataFrame(dataset)

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

df.to_csv(
    OUTPUT,
    index=False
)

print("=" * 60)
print("Research Dataset Generated Successfully")
print("=" * 60)

print(df.head())

print()

print("Shape :", df.shape)

print()

print("Saved At")

print(OUTPUT)