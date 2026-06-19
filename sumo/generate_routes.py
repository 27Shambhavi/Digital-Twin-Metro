import os
import subprocess
import sys

SUMO_HOME = r"C:\Program Files (x86)\Eclipse\Sumo"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NETWORK = os.path.join(BASE_DIR, "osm", "indore.net.xml")

RANDOM_TRIPS = os.path.join(
    SUMO_HOME,
    "tools",
    "randomTrips.py"
)

print("\nChoose Scenario\n")
print("1. Normal")
print("2. Peak Hour")

choice = input("\nEnter Choice : ")

if choice == "1":

    OUTPUT = os.path.join(
        BASE_DIR,
        "data",
        "raw",
        "routes.rou.xml"
    )

    period = "3"

elif choice == "2":

    OUTPUT = os.path.join(
        BASE_DIR,
        "data",
        "raw",
        "peak_routes.rou.xml"
    )

    period = "1"

else:

    print("Invalid Choice")

    exit()

command = [

    sys.executable,

    RANDOM_TRIPS,

    "-n",
    NETWORK,

    "-r",
    OUTPUT,

    "-e",
    "3600",

    "--period",
    period,

    "--seed",
    "42"

]

subprocess.run(command)

print("\nDone.")