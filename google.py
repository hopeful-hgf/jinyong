#!/usr/bin/env python
# coding=utf-8

from common import crawler, dlog
logger = dlog(__file__)

def search(url):
    try:
        rep = crawler(url)
        return rep.content
    except Exception as err:
        logger.error(err)

if __name__ == '__main__':
    url = ''
    search(url)
