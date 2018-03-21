#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, jsonify, render_template
from apps import ludingji, ludingji_detail, unittest, srcret
from common.model import Jinyong as jy
from common.dumblog import dlog
logger = dlog(__file__)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route(('/<param>/'))
def pipeline(param):
    _dict = {
        'ludingji': ludingji,
        'test': unittest,
        'srcret': srcret,
    }
    try:
        result = _dict.get(param)()
        logger.info('----------> %s' % result)
        return result
    except Exception as err:
        logger.info(err)
        return render_template('404.html')


@app.route(('/<param>/<page>'))
def pipeline_page(param, page):
    _dict = {
        'ludingji': ludingji_detail,
    }
    try:
        return _dict.get(param)(page)
    except Exception as err:
        logger.info(err)
        return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
