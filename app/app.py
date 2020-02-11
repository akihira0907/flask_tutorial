from flask import Flask, render_template, request, session, redirect, url_for
from models.models import PoemContent, User
from models.database import db_session
from datetime import datetime
import app.key as key
from hashlib import sha256
# from requests import session

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    # oretsuba_names = ["hiyoko", "asuka", "naru", "miyako"]
    all_poem = PoemContent.query.all()
    return render_template("index.html", name=name, all_poem=all_poem)


@app.route("/index", methods=["post"])
def post():
    name = request.form["name"]
    # oretsuba_names = ["hiyoko", "asuka", "naru", "miyako"]
    all_poem = PoemContent.query.all()
    return render_template("index.html", name=name, all_poem=all_poem)


@app.route("/add", methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = PoemContent(title, body, datetime.now())
    db_session.add(content)
    db_session.commit()
    return index()


@app.route("/update", methods=["post"])
def update():
    content = PoemContent.query.filter_by(id=request.form["update"]).first()
    content.title = request.form["title"]
    content.body = request.form["body"]
    db_session.commit()
    return index()


@app.route("/delete", methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = PoemContent.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return index()


@app.route("/login", methods=["post"])
def login():
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        password = request.form["password"]
        hashed_pass = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        if user.hashed_pass == hashed_pass:
            session["user_name"] = user_name
            return redirect(url_for("index"))
        else:
            return redirect(url_for("top", status="wrong_password"))
    else:
        return redirect(url_for("top", status="user_notfound"))


@app.route("/register", methods=["post"])
def register():
    user_name = request.form["user_name"]
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        return redirect(url_for("newcomer", status="exist_user"))
    else:
        password = request.form["password"]
        hashed_pass = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        user = User(user_name, hashed_pass)
        db_session.add(user)
        db_session.commit()
        session["user_name"] = user_name
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
