# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import ast
import yaml
from functools import wraps
from lxml import etree
from common.model import Jinyong
from flask import render_template

with open('settings.yaml', 'r') as file:
    config = yaml.load(file)


def parse(url):
    headers = {
        'Cookie': config['cookie'],
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    print('crawling : %s' % (url))
    try:
        response = requests.get(url, headers=headers)
        print('status_code is %s' % response.status_code)
        time.sleep(config['time_sleep'])
        # return response.content
        result = etree.HTML(response.content)
        return result
    except Exception as err:
        print(err)
        return None


def save(fun):
    def wrap(*args):
        item = fun(*args)
        # item = ast.literal_eval(item)
        # News.create(
        Jinyong.create(
            id=item['id'],
            title=item['title'],
            name=item['name'],
            url=item['url'],
            content=item['content'],
        )
        print('saved success {}'.format(item['title'].encode('utf-8', 'ignore')))
    return wrap


def _try(func):
    @wraps(func)
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception as err:
            print(err)
            return render_template('404.html')

    return wrapper
