# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import yaml
from lxml import etree

with open('settings.yaml', 'r') as file:
    config = yaml.load(file)


def crawler(url):
    headers = {
        'Cookie':
        config['cookie'],
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    print('crawling : %s' % (url))
    try:
        response = requests.get(url, headers=headers)
        print('status_code is %s' % response.status_code)
        time.sleep(config['time_sleep'])
        # return response.content
        return response
    except Exception as err:
        print(err)
        return None


def parser(lis, word=''):
    if len(lis) == 0:
        return ''
    elif len(lis) == 1:
        if lis[0] == '':
            return ''
        else:
            return lis[0].strip()
    elif len(lis) > 1:
        return word.join(lis).replace('  ', '').replace('\r', '').replace('\n', '').strip()
