import datetime as dt
import sqlite3

from constants import DB_PATH


class DataHandler:

    def __init__(self):
        self.sensor_count = 3  # TODO mock

        self.con = sqlite3.connect(DB_PATH)
        self.cur = self.con.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS measurements (time INTEGER, "
                         + ", ".join(f"sensor{i} REAL" for i in range(self.sensor_count))
                         + ");")
        self.con.commit()

    def add_row(self, time, measurements):
        t = int(time.timestamp())
        self.cur.execute("INSERT INTO measurements VALUES (" + ",".join("?" * (self.sensor_count + 1)) + ");",
                         (t,) + measurements)
        self.con.commit()

    def get_range(self, start, end):
        query = self.cur.execute("SELECT * FROM measurements WHERE time >= ? AND time <= ?",
                                 (int(start.timestamp()), int(end.timestamp())))
        time, *sensors = zip(*query)
        return {
            "time": [dt.datetime.fromtimestamp(t).isoformat() for t in time],
            "sensors": sensors
        }

    def get_latest(self):
        query = self.cur.execute("SELECT * FROM measurements WHERE ")


if __name__ == '__main__':
    dh = DataHandler()
    res = dh.get_range(dt.datetime(2021, 1, 1), dt.datetime(2022, 1, 1))
