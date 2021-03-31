from flask import Flask, render_template

from data import DataHandler

app = Flask(__name__, template_folder="../templates")
dh = DataHandler()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/previous")
def get_previous():
    return dh.get_data()


@app.route("/update")
def get_update():
    return dh.get_update()


if __name__ == '__main__':
    app.run(debug=True)
