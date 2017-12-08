# !/usr/bin/env python
# -*- coding: utf-8 -*-

# import yaml
import time
from common.dumblog import dlog
from common.pipeline import multi
from common.common import parse, save
# from common.model import Jinyong

logger = dlog(__file__, console='debug')


class Crawler(object):
    def __init__(self):
        self.count = 0

    @save
    def crawl(self, url, id):
        html = parse(url)
        item = {}
        item['url'] = url
        item['id'] = id
        item['name'] = html.xpath(r'//*[@id="breadnav"]/a[2]//text()')[-1]
        item['title'] = html.xpath(r'//*[@id="title"]//text()')[-1]
        pre_content = html.xpath(r'//*[@id="vcon"]//p//text()')
        item['content'] = ''
        for con in pre_content:
            item['content'] += con.strip() + 'br'
        # print 'title is {}'.format(item['title'].encode('utf-8','ignore'))
        return item


def run():
    go = Crawler()
    for i in range(822, 874):
        id = i - 821
        url = 'http://www.jinyongwang.com/lu/%s.html' % i
        multi(go.crawl, _args = [url, id])
        time.sleep(2)
        # go.crawl(url, id)
        # break
    logger.info('mission finished !')


if __name__ == "__main__":
    run()
