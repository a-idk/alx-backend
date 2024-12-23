#!/usr/bin/env python3
"""
Title: Basic Flask app
Description: setting up a basic flask app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """ method that returns rendered template """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
