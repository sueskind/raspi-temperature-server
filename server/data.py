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
        query = self.cur.execute("SELECT * FROM measurements WHERE time >= ? AND time <= ?;",
                                 (int(start.timestamp()), int(end.timestamp())))
        try:
            time, *sensors = zip(*query)
        except ValueError:
            time, sensors = [], [[]]
        return {
            "time": [dt.datetime.fromtimestamp(t).isoformat() for t in time],
            "sensors": sensors
        }

    def get_latest(self):
        query = self.cur.execute("SELECT * FROM measurements ORDER BY time DESC LIMIT 1;")
        try:
            time, *sensors = list(query)[0]
        except ValueError:
            time, sensors = None, []
        return {
            "time": time,
            "sensors": sensors
        }


if __name__ == '__main__':
    dh = DataHandler()
    res = dh.get_range(dt.datetime(2021, 1, 1), dt.datetime(2021, 1, 1))
    res = dh.get_latest()
