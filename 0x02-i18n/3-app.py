#!/usr/bin/env python3
"""
title: Parametrize template
Description: Use the _ or gettext function to parametrize your templates.
Use the message IDs home_title and home_header
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ config class declaration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object("1-app.Config")
babel = Babel(app)


@app.route("/")
def hello_world():
    """ method that returns hello world template """
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """ method that gets the best matching language for user """
    return request.accept_languages.best_match(Config.LANGUAGES)
