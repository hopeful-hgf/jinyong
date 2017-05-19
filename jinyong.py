# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, time, json, re, os, ast, yaml
from common.redisq import RedisQueue
from common.dumblog import dlog
# from common.pipeline import pipe
from common.common import parse,save
# from common.model import Jinyong
from lxml import etree
from fnvhash import fnv1a_32

logger = dlog(__file__, console='debug')


class Crawler(object):
    def __init__(self):
        self.count = 0
        with open('settings.yaml','r') as file:
            config = yaml.load(file)

    @save
    def crawl(self, url):
        html = parse(url)
        item = {}
        item['url'] = url
        item['name'] = html.xpath(r'//*[@id="breadnav"]/a[2]//text()')[-1]
        item['title'] = html.xpath(r'//*[@id="title"]//text()')[-1]
        pre_content = html.xpath(r'//*[@id="vcon"]//text()')
        item['content'] = ''
        for con in pre_content:
            item['content'] += con.strip()
        # print 'title is {}'.format(item['title'].encode('utf-8','ignore'))
        return item



def run():
    go = Crawler()
    for i in range(822, 874):
        url = 'http://www.jinyongwang.com/lu/%s.html' % i
        go.crawl(url)
        # break
    logger.info('mission finished')


if __name__ == "__main__":
    run()
