#!/usr/bin/env python3

"""
contains function update_topics(mongo_collection, name, topics)
"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    - name (string) will be the school name to update
    - topics (list of strings) will be the list of topics
    approached in the school
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
