#!/usr/bin/env python
# coding=utf-8

from common import crawler, parser, dlog
logger = dlog(__file__)

def search(word):
    url = 'https://www.google.com.hk/search?hl=en&q=%s' % word
    html = crawler(url)
    urls = html.xpath('//h3/a/@href')
    print(len(urls))
    for i in range(len(urls)):
        try:
            url = urls[i]
            title = html.xpath('//h3/a/text()')[i]
            content = parser(html.xpath('//*[@class="rc"]/div//text()'))[i]
            print(url, title)
            print('content : %s' %content)
        except Exception as err:
            logger.info(err)


if __name__ == '__main__':
    word = 'python'
    search(word)
