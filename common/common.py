# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, time, ast, yaml
from lxml import etree
from dumblog import dlog
from model import Jinyong
from pipeline import pipe

logger = dlog(__file__, console='debug')
with open('settings.yaml','r') as file:
    config = yaml.load(file)


def parse(url):
    headers={
        'Cookie' : config['cookie'],
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    logger.info('crawling : %s' % (url))
    try:
        response = requests.get(url, headers=headers)
        logger.info('status_code is %s' % response.status_code)
        time.sleep(config['time_sleep'])
        # return response.content
        result = etree.HTML(response.content)
        return result
    except Exception,err:
        logger.info(err)
        return None



def save(fun):
    def wrap(*args):
        item = fun(*args)
        # item = ast.literal_eval(item)
        # News.create(
        Jinyong.create(
            title=item['title'],
            name=item['name'],
            url=item['url'],
            content=item['content'],
        )
        logger.info('saved success {}'.format(item['title'].encode('utf-8','ignore')))
    return wrap
