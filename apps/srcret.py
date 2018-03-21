#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/secret')
def srcret():
    return render_template('srcret.html')
