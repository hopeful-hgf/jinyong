#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import sys
sys.path.append('..')
import multiprocessing

import redis
import yaml
# import gevent
# from gevent import monkey
# monkey.patch_all()

from common.redisq import RedisQueue


def pipe(src, dst=None):

    conn = redis.Redis(
        host=Setting.redis_ip,
        port=Setting.redis_port,
        password=Setting.redis_pass,
        db=Setting.redis_db)

    src_q = RedisQueue(src, conn=conn)
    if dst:
        dst_q = RedisQueue(dst, conn=conn)

    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            ret = None
            while not src_q.empty():
                try:
                    kwargs['param'] = src_q.get(timeout=Setting.queue_timeout)
                except Exception as err:
                    print(err)
                    raise Exception(
                        'Get element from redis %s timeout!' % src_q.key)
                try:
                    ret = func(*args, **kwargs)
                except Exception as err:
                    src_q.put(kwargs['param'])
                    print(err)
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


class ConfigMeta(object):
    def __getattr__(self, key):
        with open('settings.yaml', 'r') as file:
            self.con = yaml.load(file)
        return self.con.get(key)


Setting = ConfigMeta()


def multi(func, _args=[], sleep=0):
    p = multiprocessing.Process(target=func, args=_args)
    p.start()
    import time
    time.sleep(sleep)
    print('process start ! func :: %s, args :: %s' % (func.__name__, _args))


# def _gevent(func, _args=None):
#     if _args:
#         jobs = [gevent.spawn(func, arg) for arg in _args]
#     else:
#         jobs = [gevent.spawn(func,)]
#     result = gevent.joinall(jobs)
#     return result
