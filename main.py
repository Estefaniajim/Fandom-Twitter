from flask import Flask, render_template, request
from dotenv import load_dotenv
from Data.database import obtainHashTags
import os
import tweepy
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    load_dotenv()
    APIkey = os.getenv('APIkey')
    APIsecretkey = os.getenv('APIsecretkey')
    AccessToken = os.getenv("AccessToken")
    AccessTokenSecret = os.getenv("AccessTokenSecret")

    auth = tweepy.OAuthHandler(APIkey, APIsecretkey)
    auth.set_access_token(AccessToken, AccessTokenSecret)
    api = tweepy.API(auth)
    photo_url = api.me().profile_image_url
    photo_url_bigger = photo_url[0:len(photo_url) - 11]
    photo_url_bigger = photo_url_bigger + ".jpg"

    hashTags = obtainHashTags()
    selectedHashTags = []
    for _ in range(0, 5):
        value = random.choice(hashTags)
        while (value in selectedHashTags):
            value = random.choice(hashTags)
        selectedHashTags.append(value)

    return render_template('index.html',
                           user={
                               'name': api.me().screen_name, 'photo': photo_url_bigger},
                           hashtags=[
                               {'name': selectedHashTags[0], 'url': '/fandom'},
                               {'name': selectedHashTags[1], 'url': '/fandom'},
                               {'name': selectedHashTags[2], 'url': '/fandom'},
                               {'name': selectedHashTags[3], 'url': '/fandom'},
                               {'name': selectedHashTags[4], 'url': '/fandom'},
                           ],your_fandoms=[
                               {'name': 'BTS', 'url': '/fandom'},
                               {'name': 'Star Wars', 'url': '/fandom'},
                           ]
                           )


@app.route('/fandom')
@app.route('/fandom/<fandom_name>/<hashtag>')
def fandom(fandom_name="BTS"):
    load_dotenv()
    APIkey = os.getenv('APIkey')
    APIsecretkey = os.getenv('APIsecretkey')
    AccessToken = os.getenv("AccessToken")
    AccessTokenSecret = os.getenv("AccessTokenSecret")

    auth = tweepy.OAuthHandler(APIkey, APIsecretkey)
    auth.set_access_token(AccessToken, AccessTokenSecret)
    api = tweepy.API(auth)
    photo_url = api.me().profile_image_url
    photo_url_bigger = photo_url[0:len(photo_url) - 11]
    photo_url_bigger = photo_url_bigger + ".jpg"

    hashTags = obtainHashTags()
    selectedHashTags = []
    for _ in range(0, 3):
        value = random.choice(hashTags)
        while (value in selectedHashTags):
            value = random.choice(hashTags)
        selectedHashTags.append(value)

    return render_template('fandom.html', fandom_name=fandom_name,
                           user={
                               'name': api.me().screen_name, 'photo': photo_url_bigger},
                           your_fandoms=[
                               {'name': 'BTS', 'url': '#'},
                               {'name': 'Star Wars', 'url': '#'},
                           ],
                           recommended_fandoms=[
                               {'name': 'perros', 'url': '#'},
                               {'name': 'gatos', 'url': '#'},
                               {'name': 'pandas', 'url': '#'},
                           ],
                           hashtags=[
                               {'name': selectedHashTags[0], 'url': '/fandom'},
                               {'name': selectedHashTags[1], 'url': '/fandom'},
                               {'name': selectedHashTags[2], 'url': '/fandom'},
                           ],
                           tweets=[
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                               {'name': 'asdf', 'handle': 'zxcv', 'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ante enim, consectetur a libero suscipit, varius mattis lacus. Nulla facilisi. Sed consequat lorem varius molestie efficitur. Praesent vitae accumsan risus. Phasellus convallis rhoncus mi id laoreet. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque nec sapien at dolor varius euismod. Nulla eget pretium neque.',
                                'replies': "123", 'retweets': '123', 'likes': '234', 'date': "12/12/20", 'photo': 'https://pbs.twimg.com/profile_images/1012717264108318722/9lP-d2yM_400x400.jpg'},
                           ])

if __name__ == "__main__":
    app.run(debug=True)