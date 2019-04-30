#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import psycopg2
import psycopg2.extras

# -----------------------------------------------------------------------


class DBFetcher(object):
    def __init__(self):
        super(DBFetcher, self).__init__()

        self._db_config = {
            'host': os.environ.get('DATABASE_HOST', None),
            'dbname': os.environ.get('DATABASE_NAME', None),
            'user': os.environ.get('DATABASE_USER', None),
            'password': os.environ.get('DATABASE_PASSWORD', None)
        }

        self._db_connect = psycopg2.connect(**self._db_config)
        self._db_cursor = self._db_connect.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)

    def fetch(self, sql: str) -> list:
        """:return: [ { key: value }, ... ]"""
        self._db_cursor.execute(sql)
        return self._db_cursor.fetchall()

    def execute(self, sql: str):
        self._db_cursor.execute(sql)
        self._db_connect.commit()

    def __del__(self):
        self._db_cursor.close()
        self._db_connect.close()

# -----------------------------------------------------------------------


if __name__ == '__main__':
    pass
