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
