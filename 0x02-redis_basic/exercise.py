#!/usr/bin/env python3

'''exercise file'''

import uuid
import redis
from typing import Union

class Cache:
    '''
    Cache class
    '''
    def __init__(self):
        '''
        init of the class
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        a method that generate a random key
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        '''
        this get data of a key
        '''
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        '''this get a string'''
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''get the integer'''
        return self.get(key, fn=int)
