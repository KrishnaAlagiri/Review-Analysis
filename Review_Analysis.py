#!/usr/local/bin/python
import tweepy
import ConfigParser
from textblob import TextBlob

#Step 0 - Parsing
config = ConfigParser.ConfigParser()
config.read('Setting.conf')
print config.get('DB','DB_DATABASE')
consumer_key = config.get('TWITTER','CONSUMER_KEY')
consumer_secret = config.get('TWITTER','CONSUMER_SECRET')
access_token = config.get('TWITTER','ACCESS_TOKEN')
access_token_secret = config.get('TWITTER','ACCESS_TOKEN_SECRET')

# Step 1 - Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Step 2 - Retrieve Tweets
Product = str(input())
public_tweets = api.search(Product)


#Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    #Step 3 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
