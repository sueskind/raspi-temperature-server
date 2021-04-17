import re
import sqlite3
import time

from constants import DB_PATH, SENSOR_FILENAMES, SENSOR_PATH_FMT


def measurements_loop():
    last_measurements = []

    def get_temperature(i):
        filename = SENSOR_PATH_FMT.format(SENSOR_FILENAMES[i])
        with open(filename, "r") as f:
            text = f.read()
        try:
            temp_str = re.findall(r"t=(\d*)", text)[0]
            return int(temp_str) / 1000
        except IndexError:
            return last_measurements[i]

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    try:
        while True:
            c.execute("""DELETE FROM measurement WHERE time < DATETIME('now', '-3 day')""")

            measurements = [get_temperature(i) for i in range(len(SENSOR_FILENAMES))]
            c.execute("""INSERT INTO measurement VALUES(DATETIME('now'),?,?,?)""", measurements)

            conn.commit()

            last_measurements = measurements
            time.sleep(1)

    finally:
        conn.close()
