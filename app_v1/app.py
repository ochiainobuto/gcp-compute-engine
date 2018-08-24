#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from flask import escape, Markup
from wtforms import Form, TextAreaField, StringField, validators, ValidationError
import arrow

app = Flask(__name__)



@app.route('/')
def index():
    return 'Hello World'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)
