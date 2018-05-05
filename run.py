#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, render_template, jsonify, send_from_directory
from google import search
from common import _try, jy
from common.dumblog import dlog
logger = dlog(__file__)
app = Flask(__name__)


@app.route('/')
def hello_world():
    _str = '<html>  <meta http-equiv="refresh" content="0;url=https://www.littletool.top/index/">  </html> '
    return _str


@app.route('/index/')
def index():
    return render_template('index.html')


@_try
@app.route('/ludingji/')
@app.route('/ludingji/<page>')
def ludingji(page=1):
    # qu = jy.select().where(jy.title==page).get()
    if int(page) > 52:
        result = 'page num is wrong !'
        return jsonify(result)
    qu = jy.select().where(jy.id == page).get()
    titles = [t.title for t in jy.select()]
    result = [x for x in qu.content.split('br')]
    return render_template('ludingji.html', content=result, head=qu.name, titles=titles, title=qu.title)


@app.route('/google/<path:word>')
def google(word='python'):
    url = 'https://www.google.com.hk/search?hl=en&q=%s' % word
    return search(url)

@_try
@app.route('/v/')
def list_movies():
    import os
    files = os.listdir('video')
    return render_template('listdir.html', data=files)


@_try
@app.route('/v/<filename>')
def get_file(filename):
    path = 'video'
    return send_from_directory(path, filename)


@_try
@app.route('/secret/')
def _srcret():
    return render_template('secret.html')


@_try
@app.route('/test/')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=8000)
    # app.run()
