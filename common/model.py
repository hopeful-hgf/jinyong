# !/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
from datetime import datetime
import yaml

try:
    import psycopg2
    from playhouse.pool import PooledPostgresqlExtDatabase

    with open('settings.yaml','r') as file:
        config = yaml.load(file)
    db = PooledPostgresqlExtDatabase(
        config['database'],
        max_connections=8,
        stale_timeout=300,
        user=config['user'],
        host=config['host'],
        password=config['password'],
        autorollback=True,
        register_hstore=False)
except ImportError:
    db = SqliteDatabase('Jinyong.sqlite')


class BaseModel(Model):
    class Meta:
        database = db


class Jinyong(BaseModel):
    id = IntegerField(primary_key=True, verbose_name='id')
    title = CharField(max_length=150, verbose_name='章节')
    name = CharField(max_length=20, verbose_name='小说')
    url = CharField(max_length=100, verbose_name='url')
    content = TextField(null=True, verbose_name='内容')
    created_at = DateTimeField(default=datetime.now, verbose_name='创建时间')


if __name__ == '__main__':
    try:
        Jinyong.create_table()
    except Exception, err:
        print err
