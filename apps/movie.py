#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template
from flask import send_from_directory
app = Flask(__name__)



@app.route('/v/')
def list_movies():
    import os
    files = os.listdir('video')
    return render_template('listdir.html', data=files)


@app.route('/v/<filename>')
def get_file(filename):
    path = 'video'
    return send_from_directory(path, filename)
