# twitter-stream-mongo

## setup

```
pip install tweepy
pip install pymongo
git clone https://github.com/y-matsuki/twitter-stream-mongo.git
```

## database

```
cd twitter-stream-mongo
mongod --dbpath data/mongo
```

## run

```
cd twitter-stream-mongo
python process_stream.py
```
