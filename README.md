# mongoDBconnect

A mongoDB connection library that allows you to retry connections, handle
exceptions and specify defaults. This was a learning experiment.

Sample
```
./testConnect.py 2 "mongodb+srv://mongodb.net" 27017 some_user some_password true

./testConnect.py 1 localhost 27017 user pwd false
./testConnectURI.py 3 "mongodb+srv://xxx:xxx@mongodb.net/test?retryWrites=true&w=majority"
```
