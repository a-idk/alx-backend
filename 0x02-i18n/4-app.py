#!/usr/bin/env python3
"""
Title: Force locale with URL parameter
Description: implement a way to force a particular locale by passing
the locale=fr parameter to your app’s URLs
"""

import babel
from flask import Flask, render_template, request
from flask_babel import Babel
import re


class Config():
    """ config class """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config())
Babel.default_locale = "en"
Babel.default_timezone = "UTC"
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ method that gets locale """
    lang = request.args.get('locale')
    if lang is not None:
        if lang in app.config['LANGUAGES']:
            return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def gettext():
    """ method that gets text from rendered template """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
