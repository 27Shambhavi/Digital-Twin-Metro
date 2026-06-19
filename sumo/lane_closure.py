import os
import subprocess

SUMO_HOME = r"C:\Program Files (x86)\Eclipse\Sumo"

NETCONVERT = os.path.join(
    SUMO_HOME,
    "bin",
    "netconvert.exe"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NETWORK = os.path.join(
    BASE_DIR,
    "osm",
    "indore.net.xml"
)

OUTPUT = os.path.join(
    BASE_DIR,
    "osm",
    "indore_construction.net.xml"
)

print("="*60)
print("Creating Metro Construction Scenario")
print("="*60)

command = [
    NETCONVERT,
    "--sumo-net-file",
    NETWORK,
    "-o",
    OUTPUT
]

subprocess.run(command)

print("\nConstruction Network Created!")
print(OUTPUT)