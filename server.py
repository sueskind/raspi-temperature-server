from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def get_data():
    import random
    return {"temperatures": [random.random() * 3 + 30 for _ in range(20)]}


if __name__ == '__main__':
    app.run(debug=True)
