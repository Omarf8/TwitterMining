import os
import requests
import tweepy
from dotenv import load_dotenv
from tweepy import OAuthHandler

# Loads .env variables
load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

def get_weather(city):
    """Fetch Weather from OpenWeatherMap"""
    weather_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=imperial"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather_info = {
            "city" : data["name"],
            "temp" : data["main"]["temp"],
            "feels_like" : data["main"]["feels_like"],
            "description" : data["weather"][0]["description"],
            "humidity" : data["main"]["humidity"],
            "wind_speed" : data["wind"]["speed"]
        }

        print(f"Successfully fetched weather data for {city}")
        return weather_info

    except Exception as e:
        print(f"Error: {e}")
        return None

def create_tweet_format(info):
    if not info:
        return None

    lower_description = info["description"].lower()

    if "clear" in lower_description:
        emoji = "☀️"
    elif "rain" in lower_description:
        emoji = "🌧️"
    elif "cloud" in lower_description:
        emoji = "☁️"
    elif "snow" in lower_description:
        emoji = "❄️"
    elif "storm" in lower_description:
        emoji = "🌩️"
    else:
        emoji = "⛅️"

    tweet = f"""{emoji} Weather Update for {info["city"]}

    🌡️ Temperature: {info["temp"]:.1f} F
    ⭐️ Conditions: {info["description"].capitalize()}
    💧 Humidity: {info["humidity"]}%
    💨 Wind: {info["wind_speed"]} mph
    """

    return tweet

def post_weather_update(city):
    print(f"Getting Weather for {city}...")

    weather = get_weather(city)
    if not weather:
        print("Cannot create tweet without weather info")
        return False

    tweet_text = create_tweet_format(weather)
    if not tweet_text:
        print("Cannot create tweet without tweet format")
        return False

    print("Tweet to be posted:")
    print(tweet_text)

    try:
        tweet = client.create_tweet(text=tweet_text)
        print("Tweet Posted Successfully")
        print(f"ID: {tweet.data["id"]}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    post_weather_update("Chicago")