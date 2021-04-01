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

    def add_row(self, time, *measurements):
        self.cur.execute("INSERT INTO measurements VALUES (" + ",".join("?" * (self.sensor_count + 1)) + ");",
                         (time,) + measurements)
        self.con.commit()

    def get_range(self, start, end):
        query = self.cur.execute("SELECT * FROM measures WHERE time >= ? AND time <= ?",
                                 (int(start.timestamp()), int(end.timestamp())))

    def get_latest(self):
        query = self.cur.execute("SELECT * FROM measurements WHERE ")


if __name__ == '__main__':
    dh = DataHandler()
    dh.add_row(200021, 4.521, 25.12, 333.21)
