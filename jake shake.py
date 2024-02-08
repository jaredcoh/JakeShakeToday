import tweepy
import requests
import pandas as pd
from datetime import datetime, timedelta

def post(text):

    BEARER_TOKEN = '<insertdata>'

    API_KEY = '<insertdata>'
    API_SECRET_KEY = '<insertdata>'
    ACCESS_TOKEN = '<insertdata>'
    ACCESS_TOKEN_SECRET = '<insertdata>'


    # Authenticate with Twitter
    auth = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET_KEY, access_token=ACCESS_TOKEN,
                    access_token_secret=ACCESS_TOKEN_SECRET)
    # Compose the tweet
    tweet_text = "Are Jake Shakes half off at The Milkshake Factory (@MShakeFactory) Today?: " + text

    # Post the tweet
    auth.create_tweet(text=tweet_text)

import requests

def get_scores_for_date(date):

    # Construct the API URL
    api_url = f'https://api-web.nhle.com/v1/score/{date}?expand=schedule.linescore'

    # Make a GET request to the API
    response = requests.get(api_url)

# Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
    else:
        print("ERROR")


    games = data.get('games', [])
    he_score = False
    # Iterate through each game
    for game in games:

        # Iterate through each goal in the game
        for goal in game['goals']:
            scorer_name = goal['name']['default']
            scorer_team = goal['teamAbbrev']
            strength = goal['strength']
            time_in_period = goal['timeInPeriod']


            if scorer_name == "J. Guentzel":
                print(f"Date: {game['gameDate']}")
                print(f"Venue: {game['venue']['default']}")
                print(f"\nScorer: {scorer_name}")
                print(f"Team: {scorer_team}")
                print(f"Strength: {strength}")
                print(f"Time in Period: {time_in_period}")
                he_score = True
                # If you want to display the player's image (mugshot), you can include the following line
    return he_score



def get_yesterday_date():
    # Get the current date
    today = datetime.now()

    # Calculate yesterday's date by subtracting one day
    yesterday = today - timedelta(days=1)

    # Format the date as needed
    yesterday_date = yesterday.strftime("%Y-%m-%d")
    print(yesterday_date)
    return yesterday_date

def main():
    if get_scores_for_date(get_yesterday_date()):
        post("Yes!")
    else:
        post("No.")
