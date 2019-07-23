#!/usr/bin/env python3

# Author: Will Chow <will.chow@mongodb.com>
# Date: July 23, 2019

from pymongo import MongoClient
from pymongo.errors import *

def mongoDBconnect(retryConnect,
        host = 'localhost',
        port = 27017,
        username = None,
        password = None,
        authSource = 'admin',
        authMechanism = 'SCRAM-SHA-1',
        replicaSet = None,
        ssl = False,
        readConcernLevel = 'majority',
        readPreference = 'primary',
        w = 'majority',
        retryWrites = True ):

   for attempt in range(retryConnect):
      try:
         if username is None and password is None:
            # Assume that most of the info is in the URI
             client = MongoClient(host = host,
                        readConcernLevel = readConcernLevel,
                        readPreference = 'primary',
                        w = w,
                        retryWrites = retryWrites)
         else:
             client = MongoClient(host = host,
                        port = port,
                        username = username,
                        password = password,
                        authSource = authSource,
                        authMechanism = authMechanism,
                        ssl = ssl,
                        readConcernLevel = readConcernLevel,
                        w = w,
                        retryWrites = retryWrites)
         # Note Starting with version 3.0 the MongoClient constructor no longer blocks while connecting
         # to the server or servers, and it no longer raises ConnectionFailure if they are unavailable,
         # nor ConfigurationError if the user’s credentials are wrong.
         client.admin.command('ismaster')
      except PyMongoError as e:
         # Possible exceptions are ConnectionFailure, OperationFailure, ConfigurationError
         # so just use PyMongoError which is the base class for all PyMongo exceptions
         print("On attempt: %d, Could not connect to MongoDB: %s" % (attempt, e))
         continue
      print("Connected!")
      break
   else:
      # We failed all attempts to connect
      print("Could not connect to MongoDB after %d attempts" % (retryConnect))
      return None

   return client

def mongoDBdisconnect(client):
    if client is not None:
       client.close()
    return
