import datetime as dt
import random


class DataHandler:

    def __init__(self):
        self.sensors = 3
        start_values = 5
        self.data = {
            "times": [(dt.datetime.now() + dt.timedelta(seconds=(i - start_values) * 5)).isoformat()
                      for i in range(start_values)],
            "sensors": [[random.random() * 2 + 25 for _ in range(start_values)] for _ in range(self.sensors)]}

    def get_data(self):
        return self.data

    def get_update(self):
        return {"time": dt.datetime.now().isoformat(),
                "sensors": [random.random() * 2 + 25 for _ in range(self.sensors)]}
