from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    oretsuba_names = ["hiyoko", "asuka", "naru", "miyako"]
    return render_template("index.html", name=name, oretsuba_names=oretsuba_names)


@app.route("/index", methods=["post"])
def post():
    name = request.form["name"]
    oretsuba_names = ["hiyoko", "asuka", "naru", "miyako"]
    return render_template("index.html", name=name, oretsuba_names=oretsuba_names)


if __name__ == "__main__":
    app.run(debug=True)
