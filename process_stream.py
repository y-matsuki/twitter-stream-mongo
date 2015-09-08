#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import logging
import uuid

from oauth2client.client import SignedJwtAssertionCredentials
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# Twitter
token = ""
token_key = ""
con_secret = ""
con_secret_key = ""
# MongoDB
db = client.twitter

class MyStreamListener(StreamListener):
    def on_data(self, raw_data):
        json_data = json.loads(raw_data)
        if 'text' in json_data:
            print(json.dumps(json_data))
            tweet_id = json_data["id"]
            db.tweet.update_one({"id":tweet_id}, {"$set": json_data}, upsert=True)
            return True
        return False

    def on_error(self, status_code):
        print(status_code)


auth = OAuthHandler(con_secret, con_secret_key)
auth.set_access_token(token, token_key)

twitterStream = Stream(auth, MyStreamListener())
twitterStream.filter(locations=[139.69, 35.65, 139.71, 35.66])
