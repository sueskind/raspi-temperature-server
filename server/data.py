import datetime as dt
import random


class DataHandler:

    def get_data(self):
        return {
            "times": [dt.datetime(2020, 3, 3, 12, i, random.randint(0, 59)).isoformat() for i in range(3, 10)],
            "sensors": [[random.random() * 5 + 30 for _ in range(3, 10)] for _ in range(3)]
        }
