#!/usr/bin/env python3
""" 9-update_topics """


def update_topics(mongo_collection, name, topics):
    '''
    This will update all topics
    '''
    result = mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}})
    return result.modified_count
