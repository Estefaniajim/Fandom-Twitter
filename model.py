from csv import DictReader

def getTweets():
    with open("Data/tweetsData2") as file:
        reader = DictReader(file)
        dic = {}
        for line,row in enumerate(reader):
            dic[line] = [row['user.name'], row["user.screenName"], row["text"], row["retweetCount"], row["favoriteCount"], row["created_at"], row["user.profileImageUrl"]]
    return dic

def getNTweets(n):
    tweets = []
    dic = getTweets()
    for i in range(n):
        tweets.append(dic[i])
    return tweets
