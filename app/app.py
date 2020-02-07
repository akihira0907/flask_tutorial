from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    weapons = ["sword", "gun", "shield", "bow"]
    return render_template("index.html", name=name, weapons=weapons)


@app.route("/index", methods=["post"])
def post():
    name = request.form["name"]
    weapons = ["sword", "gun", "shield", "bow"]
    return render_template("index.html", name=name, weapons=weapons)


if __name__ == "__main__":
    app.run(debug=True)
