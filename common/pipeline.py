#!/usr/bin/env python
# -*- coding: utf-8 -*-


import redis,yaml
from redisq import RedisQueue
import functools
with open('settings.yaml') as file:
    config = yaml.load(file)
conn = redis.Redis(host=config['redis_ip'],
                   port=config['redis_port'],
                   password=config['redis_pass'],
                   db=config['redis_db'])


def pipe(src, dst=None):
    src_q = RedisQueue(src, conn=conn)
    if dst:
        dst_q = RedisQueue(dst, conn=conn)

    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            ret = None
            while not src_q.empty():
                try:
                    kwargs['param'] = src_q.get(timeout=config['queue_timeout'])
                except Exception, err:
                    print err
                    raise Exception('Get element from redis %s timeout!' % src_q.key)
                try:
                    ret = func(*args, **kwargs)
                except Exception, err:
                    src_q.put(kwargs['param'])
                    print err
                    # raise Exception(err)
                if dst:
                    if isinstance(ret, list):
                        for r in ret:
                            dst_q.put(r)
                    else:
                        # for i in range(100):  # debug
                        dst_q.put(ret)
                # break  # debug
            return ret

        return inner

    return outer


# __all__ = [pipe]

