import datetime as dt
import random


class DataHandler:

    def __init__(self):
        self.sensors = 3
        self.data = {"times": [], "sensors": [list() for _ in range(self.sensors)]}

    def _add_data(self):
        self.data["times"].append(dt.datetime.now().isoformat())
        for sensor in self.data["sensors"]:
            sensor.append(random.random() * 2 + 25)

    def get_data(self):
        self._add_data()
        return self.data
