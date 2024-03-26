#!/usr/bin/env python3
""" 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    '''
    Insert a new collection into a collection
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
