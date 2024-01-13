import tweepy
import requests
import pandas as pd
from datetime import datetime
from datetime import timedelta

def post(text):
    API_KEY = "X8ra26ytbPBrboFAh8Mywa7Wf"
    API_SECRET = "VBt05E8olDk5RPeTTWutgSin1UTZEN4sM715UEvZojftEPgGJ1"
    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAL01lQEAAAAAEEo8FHRqk7kBCnKjmP3pI1738S0%3DmGJH2BXIievfrYepxv53bDS1xQu8ynq2lzGHTZd0zUFrYLHD66"
    CLIENT_ID = "1615860945938698241-UX2fHttX7rSPeL5CPpooDEbjifdXxc"  #access token
    CLIENT_SECRET = "FWfgfOsgxft1svGuRuBoAQPZNa0Ca6IpAT9aqQU7C4cAA" #access token secret

    api_key = "hgrthgy2374RTYFTY"  # CONSUMER_KEY
    api_secret_key = "hGDR2Gyr6534tjkht"  # CONSUMER_SECRET
    access_token = "HYTHTYH65TYhtfhfgkt34"  # ACCESS_TOKEN
    access_token_secret = "ged5654tHFG"  # ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(CLIENT_ID,CLIENT_SECRET)
    api = tweepy.API(auth)

    tweet= "Are Jake Shakes half off at The Milkshake Factory Today?: " + text

    # Generate text tweet
    status = "This is my first post to Twitter using the API"
    api.update_status(status=status)


url = 'https://www.nhl.com/player/jake-guentzel-8477404'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-2]

recent_date = df.values.tolist()[0][1]
recent_goal = df.values.tolist()[0][2]
second_recent_date = df.values.tolist()[1][1]
second_recent_goal = df.values.tolist()[1][2]

if recent_goal > 0:
    tf_goal = True

if (datetime.today() - timedelta(days = 1)).strftime("%b %d").upper() == recent_date and tf_goal == True:
    post("Yes!")
else:
    post("No.")