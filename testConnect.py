#!/usr/bin/env python3
import sys
import mongoDBconnect
import pprint

retryConnect = int(sys.argv[1])
host = str(sys.argv[2])
port = int(sys.argv[3])
username = str(sys.argv[4])
password = str(sys.argv[5])
ssl = sys.argv[6].lower() == 'true'
print("\nhost %s" % (host))

connection = mongoDBconnect.mongoDBconnect(retryConnect,
                    host,
                    port,
                    username,
                    password,
                    ssl = ssl,
                    w = 1,
                    retryWrites = True)

if connection is not None:
   collection = connection.test.employees
   pprint.pprint(collection.find_one())
   mongoDBconnect.mongoDBdisconnect(connection)
