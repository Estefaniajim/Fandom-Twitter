from dotenv import load_dotenv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from database import obtainHashTags
import os
import requests
import json
import csv
import sys
import time

# Setting the API keys
load_dotenv()
APIkey = os.getenv('APIkey')
APIsecretkey = os.getenv('APIsecretkey')
AccessToken = os.getenv("AccessToken")
AccessTokenSecret = os.getenv("AccessTokenSecret")

# Obtain hashtags from database
hashTagsDatabase = obtainHashTags()

# Getting the hashtags
hashtagsData = requests.get('https://estefaniajim.github.io/Fandom-Twitter/Data/Hashtags.json')
hashtags = json.loads(hashtagsData.text)
for pos, string in enumerate(hashtags):
    if string[0] == "#":
        hashtags[pos] = "/" + string
print("Got the hashtags . . .")


# Listener class
class StreamListener(StreamListener):
    def __init__(self, api=None):
        self.api = api
        csvFile = open("tweetsData3", 'w')
        print("Created the cvs . . .", end=" ")
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['text',
                            'created_at',
                            'geo',
                            'lang',
                            'place',
                            'coordinates',
                            'user.favouritesCount',
                            'user.statusesCount',
                            'user.description',
                            'user.location',
                            'user.id',
                            'user.createdAt',
                            'user.verified',
                            'user.following',
                            'user.url',
                            'user.listedCount',
                            'user.followersCount',
                            'user.defaultProfileImage',
                            'user.utcOffset',
                            'user.friendsCount',
                            'user.defaultProfile',
                            'user.name',
                            'user.lang',
                            'user.screenName',
                            'user.geoEnabled',
                            'user.profileBackgroundColor',
                            'user.profileImageUrl',
                            'user.timeZone',
                            'id',
                            'favoriteCount',
                            'retweeted',
                            'source',
                            'favorited',
                            'retweetCount'])

    def on_status(self, status):
        print("Collecting tweets . . .", end=" ")
        csvFile = open("tweetsData3", 'a')
        csvWriter = csv.writer(csvFile)
        if not 'RT @' in status.text:
            try:
                csvWriter.writerow([status.text,
                                    status.created_at,
                                    status.geo,
                                    status.lang,
                                    status.place,
                                    status.coordinates,
                                    status.user.favourites_count,
                                    status.user.statuses_count,
                                    status.user.description,
                                    status.user.location,
                                    status.user.id,
                                    status.user.created_at,
                                    status.user.verified,
                                    status.user.following,
                                    status.user.url,
                                    status.user.listed_count,
                                    status.user.followers_count,
                                    status.user.default_profile_image,
                                    status.user.utc_offset,
                                    status.user.friends_count,
                                    status.user.default_profile,
                                    status.user.name,
                                    status.user.lang,
                                    status.user.screen_name,
                                    status.user.geo_enabled,
                                    status.user.profile_background_color,
                                    status.user.profile_image_url,
                                    status.user.time_zone,
                                    status.id,
                                    status.favorite_count,
                                    status.retweeted,
                                    status.source,
                                    status.favorited,
                                    status.retweet_count])
            except Exception as e:
                print("An exception occurred: ")

                print(e)
                pass
        csvFile.close()
        return

    def on_error(self, status_code):
        if status_code == 420:
            return False
        else:
            print("An error occurred: " + status_code)

    def on_timeout(self):
        print(sys.stderr, "On timeout . . . ")
        time.sleep(10)
        print("Lets hope I dont get banned")
        return

    def on_delete(self, status_id, user_id):
        print("Got a delete note. . .", end=" ")
        return

    def on_limit(self, track):
        print("Rate limited . . . ")
        return True


# Getting the tweets
def getTweets(hashtags):
    auth = OAuthHandler(APIkey, APIsecretkey)
    auth.set_access_token(AccessToken, AccessTokenSecret)
    streamListener = StreamListener()
    stream = Stream(auth, streamListener)
    while True:
        try:
            stream.filter(track=hashtags)
        except:
            continue

print(hashTagsDatabase)
getTweets(hashTagsDatabase)
