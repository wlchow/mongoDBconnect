#!/usr/bin/env python3
import sys
import mongoDBconnect
import pprint

retryConnect = int(sys.argv[1])
mongoDBURI = str(sys.argv[2])
print("\nURI %s" % (mongoDBURI))

connection = mongoDBconnect.mongoDBconnect(retryConnect, mongoDBURI)

if connection is not None:
    collection = connection.test.employees
    pprint.pprint(collection.find_one())
    mongoDBconnect.mongoDBdisconnect(connection)
