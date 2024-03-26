#!/usr/bin/env python3
""" 8-all """


def list_all(mongo_collection):
    '''
    list all documents in a collection
    '''
    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents
