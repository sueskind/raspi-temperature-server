import datetime as dt

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def get_data():
    import random
    return {
        "times": [dt.datetime(2020, 3, 3, 12, i, random.randint(0, 59)).isoformat() for i in range(3, 10)],
        "sensors": [[random.random() * 5 + 30 for _ in range(3, 10)] for _ in range(3)]
    }


if __name__ == '__main__':
    app.run(debug=True)
