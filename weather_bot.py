import os
import tweepy
from dotenv import load_dotenv
from tweepy import OAuthHandler

# Loads .env variables
load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")

client = tweepy.Client(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

# Testing to see if I can post tweets to Twitter
try:
    tweet = client.create_tweet(text="Testing My Twitter Robot")
    print("Success! The tweet should have been posted")
    print(f"ID: {tweet.data["id"]}")
except Exception as e:
    print(f"Error: {e}")