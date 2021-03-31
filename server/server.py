from flask import Flask, render_template

from data import DataHandler

app = Flask(__name__, template_folder="../templates")
dh = DataHandler()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def get_data():
    return dh.get_data()


if __name__ == '__main__':
    app.run(debug=True)
