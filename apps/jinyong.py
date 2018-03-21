#!/usr/bin/env python
# coding=utf-8

from common.model import Jinyong as jy
from flask import Flask, render_template, jsonify
from common.dumblog import dlog
app = Flask(__name__)
logger = dlog(__file__)


@app.route('/ludingji/')
def ludingji():
    data = jy.select()
    return render_template('ludingji.html', data=data)


@app.route('/ludingji/<param>/')
def ludingji_detail(param):
    # qu = jy.select().where(jy.title==param).get()
    if int(param) > 52:
        result = 'page num is wrong !'
        return jsonify(result)
    qu = jy.select().where(jy.id == param).get()
    res = qu.content.split('br')
    result = [x for x in res]
    logger.info('res is {}'.format(len(res)))
    return render_template('ludingji_detail.html', content=result, head=qu.name, title=qu.title)


@app.route('/test/')
def unittest():
    js_lang = u'test'
    # js_lang = u'function message(){alter("printf")}'
    return render_template('test.html', js_lang=js_lang)
