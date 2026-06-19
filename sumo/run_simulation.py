import os
import subprocess

SUMO_GUI = r"C:\Program Files (x86)\Eclipse\Sumo\bin\sumo-gui.exe"

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

configs = {

    "1": os.path.join(BASE, "sumo", "simulation.sumocfg"),

    "2": os.path.join(BASE, "sumo", "construction.sumocfg"),

    "3": os.path.join(BASE, "sumo", "peak_hour.sumocfg")

}

print("\nChoose Scenario\n")

print("1. Normal")

print("2. Construction")

print("3. Peak Hour")

choice = input("\nChoice : ")

subprocess.run([SUMO_GUI, configs[choice]])