# twitter-stream-mongo

Twitter Streaming APIから取得したTweetをMongoDBに蓄積する

## 実行手順

### 準備

```shell
pip install tweepy
pip install pymongo
git clone https://github.com/y-matsuki/twitter-stream-mongo.git
```

### MongoDB起動

```shell
cd twitter-stream-mongo
mongod --dbpath data/mongo
```

### 実行

```shell
cd twitter-stream-mongo
python process_stream.py
```

## Tweetの取得範囲

```javascript
// index.htmlの36,37行目の範囲を
new google.maps.LatLng(35.65, 139.69),
new google.maps.LatLng(35.655, 139.71)
// TweetStreamのフィルタに設定する
twitterStream.filter(locations=[139.69, 35.65, 139.71, 35.655])
```
