import os
from os.path import join, dirname, abspath

# dirs
PROJECT_ROOT = dirname(dirname(abspath(__file__)))
DB_DIR = join(PROJECT_ROOT, "data")
DB_PATH = join(PROJECT_ROOT, "data", "db.sqlite")

os.makedirs(DB_DIR, exist_ok=True)

# sensors
SENSOR_FILENAMES = ["28-3c01d6073e19", "28-3c01d607ac47", "28-3c01d607f173"]
SENSOR_PATH_FMT = "/sys/bus/w1/devices/{}/w1_slave"
