#!/usr/local/bin/python
# Product Review Analysis
# Created by Krishna Alagiri, https://github.com/KrishnaAlagiri

import tweepy, msvcrt, configparser
from textblob import TextBlob


#Step 0 - Parsing
print("Parsing Informations from Setting.conf....")
config = configparser.ConfigParser()

# Uncomment the below before executing
#config.read('Setting.conf.ini')
# Comment the below before executing
config.read('C:\\Users\\Shrikrish\\Documents\\GitHub\\Setting.ini')

consumer_key = config.get('TWITTER','CONSUMER_KEY')
consumer_secret = config.get('TWITTER','CONSUMER_SECRET')
access_token = config.get('TWITTER','ACCESS_TOKEN')
access_token_secret = config.get('TWITTER','ACCESS_TOKEN_SECRET')

# Step 1 - Authenticate
print("Authenticating....")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Step 2 - Retrieve Tweets
print("Authenticated :)")
print()
Product = str(input("Enter Product Name: "))
public_tweets = api.search(Product,"en","english",99)
print("")

average_polarity=0.00
num = 0
for tweet in public_tweets:
    print(tweet.text)
    #Step 3 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    if(analysis.sentiment.subjectivity!=0):
        num = num + 1
        average_polarity = average_polarity + (analysis.sentiment.subjectivity*analysis.sentiment.polarity)
        print(analysis.sentiment)
        print("")

print("")
average_polarity = average_polarity/num
print("Average Polarity (-1 -> 1) for ", Product, "is ", average_polarity)
print("Press any key to exit......")
msvcrt.getch()
