import os
from os.path import join, dirname, abspath

PROJECT_ROOT = dirname(dirname(abspath(__file__)))
DB_DIR = join(PROJECT_ROOT, "data")
DB_PATH = join(PROJECT_ROOT, "data", "db.sqlite")

os.makedirs(DB_DIR, exist_ok=True)

SENSOR_COUNT = 3
