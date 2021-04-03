import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from constants import DB_PATH

app = Flask(__name__, template_folder="../templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DB_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Measurement(db.Model):
    time = db.Column(db.DATETIME, primary_key=True)
    sensor1 = db.Column(db.REAL)
    sensor2 = db.Column(db.REAL)
    sensor3 = db.Column(db.REAL)


if not os.path.exists(DB_PATH):
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/range")
def get_range():
    results = Measurement.query.order_by(Measurement.time).all()
    out = {
        "times": [],
        "sensors": [[], [], []]
    }
    for r in results:
        out["times"].append(r.time.isoformat())
        out["sensors"][0].append(r.sensor1)
        out["sensors"][1].append(r.sensor2)
        out["sensors"][2].append(r.sensor3)
    return out


@app.route("/update")
def get_update():
    result = Measurement.query.order_by(Measurement.time.desc()).first()

    return {
        "time": result.time.isoformat(),
        "sensors": [result.sensor1, result.sensor2, result.sensor3]
    }


if __name__ == '__main__':
    app.run(debug=True)
