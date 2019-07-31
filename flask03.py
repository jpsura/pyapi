#!/usr/bin/env python3
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
app = Flask(__name__)

@app.route("/success/<name>")
def success(name):
    return "Welcome {}".format(name)

@app.route("/login",methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("success", name=user))
    else:
        user = request.arg.get("nm")
        return redirect(url_for("success", name=user))
if __name__ == "__main__":
    app.run(port=5009)
