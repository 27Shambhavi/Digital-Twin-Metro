import os
import xml.etree.ElementTree as ET
import pandas as pd

# ===================================================
# Paths
# ===================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

NORMAL = os.path.join(
    BASE_DIR,
    "data",
    "simulation_output",
    "tripinfo.xml"
)

CONSTRUCTION = os.path.join(
    BASE_DIR,
    "data",
    "simulation_output",
    "construction_tripinfo.xml"
)

RESULT = os.path.join(
    BASE_DIR,
    "results",
    "scenario_comparison.csv"
)


# ===================================================
# Function
# ===================================================

def read_tripinfo(path):

    tree = ET.parse(path)

    root = tree.getroot()

    duration = []
    waiting = []
    timeloss = []
    route = []

    for trip in root.findall("tripinfo"):

        duration.append(float(trip.attrib["duration"]))

        waiting.append(float(trip.attrib["waitingTime"]))

        timeloss.append(float(trip.attrib["timeLoss"]))

        route.append(float(trip.attrib["routeLength"]))

    avg_speed = sum(route) / sum(duration)

    return {

        "Vehicles": len(duration),

        "Avg Duration (s)": sum(duration) / len(duration),

        "Avg Waiting (s)": sum(waiting) / len(waiting),

        "Avg TimeLoss (s)": sum(timeloss) / len(timeloss),

        "Avg Speed (m/s)": avg_speed

    }


normal = read_tripinfo(NORMAL)

construction = read_tripinfo(CONSTRUCTION)

comparison = pd.DataFrame({

    "Metric": normal.keys(),

    "Normal": normal.values(),

    "Construction": construction.values()

})

comparison["% Change"] = (

    (comparison["Construction"] - comparison["Normal"])

    / comparison["Normal"]

) * 100

comparison.to_csv(RESULT, index=False)

print("\n")

print(comparison)

print("\nSaved at")

print(RESULT)