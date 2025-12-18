import os
import requests
import tweepy
from dotenv import load_dotenv
from tweepy import OAuthHandler

# Loads .env variables
load_dotenv()

# bearer_token = os.getenv("BEARER_TOKEN")
# consumer_key = os.getenv("CONSUMER_KEY")
# consumer_secret = os.getenv("CONSUMER_SECRET")
# access_token = os.getenv("ACCESS_TOKEN")
# access_secret = os.getenv("ACCESS_SECRET")

client = tweepy.Client(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

def get_weather(city = "Chicago"):
    weather_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={weather_key}&units=imperial"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print(f"Name: {data["name"]}")
        print(f"Temperature: {data["main"]["temp"]} F")
        print(f"Description: {data["weather"][0]["description"]}")
    except Exception as e:
        print(f"Error: {e}")

get_weather()

# # Testing to see if I can post tweets to Twitter
# try:
#     tweet = client.create_tweet(text="Testing My Twitter Robot")
#     print("Success! The tweet should have been posted")
#     print(f"ID: {tweet.data["id"]}")
# except Exception as e:
#     print(f"Error: {e}")