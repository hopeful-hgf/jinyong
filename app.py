#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, jsonify, render_template
from common.model import Jinyong as jy
app = Flask(__name__)

@app.route('/')
def hello_world():
    data = jy.select()
    names = []
    for d in data:
        if d.name not in names:
            names.append(d.name)
    # return jsonify(names)
    return render_template('index.html', names=names)


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
    qu = jy.select().where(jy.id==param).get()
    res = qu.content.split('br')
    result = [x for x in res]
    print('res is {}'.format(len(res)))
    return render_template('ludingji_detail.html', content=result, head=qu.name, title=qu.title)


@app.route('/test/')
def test():
    js_lang = u'test'
    # js_lang = u'function message(){alter("printf")}'
    return render_template('test.html', js_lang=js_lang)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
