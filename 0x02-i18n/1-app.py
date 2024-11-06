#!/usr/bin/env python3

"""
Title: Basic babel setup
Description: configure available languages in our app,
create a Config class that has a LANGUAGES class attribute equal
to ["en", "fr"].
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class declaration """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """ method that returns the rendered template """
    return render_template('1-index.html')
