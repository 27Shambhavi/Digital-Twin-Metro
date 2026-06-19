import os
import xml.etree.ElementTree as ET
import pandas as pd

# =====================================================
# Project Paths
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TRIPINFO_FILE = os.path.join(
    BASE_DIR,
    "data",
    "simulation_output",
    "tripinfo.xml"
)

OUTPUT_CSV = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "traffic_dataset.csv"
)

# =====================================================
# Parse XML
# =====================================================

tree = ET.parse(TRIPINFO_FILE)
root = tree.getroot()

records = []

for trip in root.findall("tripinfo"):

    records.append({

        "vehicle_id": trip.attrib.get("id"),

        "depart": float(trip.attrib.get("depart", 0)),

        "arrival": float(trip.attrib.get("arrival", 0)),

        "duration": float(trip.attrib.get("duration", 0)),

        "routeLength": float(trip.attrib.get("routeLength", 0)),

        "waitingTime": float(trip.attrib.get("waitingTime", 0)),

        "waitingCount": int(trip.attrib.get("waitingCount", 0)),

        "timeLoss": float(trip.attrib.get("timeLoss", 0)),

        "speed":

        float(trip.attrib.get("routeLength", 0))

        /

        max(float(trip.attrib.get("duration", 1)),1)

    })

# =====================================================
# DataFrame
# =====================================================

df = pd.DataFrame(records)

df.to_csv(OUTPUT_CSV,index=False)

print("="*60)
print("Dataset Generated Successfully")
print("="*60)

print(df.head())

print("\nShape :",df.shape)