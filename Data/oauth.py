from dotenv import load_dotenv
import os
import tweepy

load_dotenv()
APIkey = os.getenv('APIkey')
APIsecretkey = os.getenv('APIsecretkey')
AccessToken = os.getenv("AccessToken")
AccessTokenSecret = os.getenv("AccessTokenSecret")

auth = tweepy.OAuthHandler(APIkey, APIsecretkey)
auth.set_access_token(AccessToken, AccessTokenSecret)
api = tweepy.API(auth)

print(api.me().name)