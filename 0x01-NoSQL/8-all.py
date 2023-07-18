#!/usr/bin/env python3

"""
contains function def list_all(mongo_collection)
"""

from pymongo.collection import Collection


def list_all(mongo_collection: Collection):
    """
    List all documents in the given collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.

    Returns:
        list: A list containing all the documents in the collection.
              Returns an empty list if there are no documents in the collection.
    """
    documents = list(mongo_collection.find())
    return documents
