#!/usr/bin/env python3
""" 11-schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    '''
    list all documents in a collection
    '''
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
