#!/usr/bin/env python3

"""
Title: Get locale from request
Description: Create a get_locale function with the babel.localeselector
decorator. Use request.accept_languages
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


@babel.localeselector
def get_locale():
    """ method get_locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """ method that returns the rendered template """
    return render_template('2-index.html')


if __name__ = "__main__":
    app.run(host="0.0.0.0", port="5000")
