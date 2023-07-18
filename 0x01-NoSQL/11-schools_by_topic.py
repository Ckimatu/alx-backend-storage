#!/usr/bin/env python3

"""
contains function schools_by_topic(mongo_collection, topic)
"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    - topic (string) will be topic searched
    """
    return mongo_collection.find({"topics": topic})
