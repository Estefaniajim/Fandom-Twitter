from database import obtainHashTags
import csv
import re

def recognizeHashtags(text):
    hashtag_list = []
    for word in text.split():
        # SPLIT ARRAY INTO SEPARATE WORDS AND LOOK FOR # AT THE START
        if word[0] == '#': 
            #APPEND WHOLE WORD
            hashtag_list.append(word[0:]) 
    return hashtag_list

def obtainMostPopular(file):
    # OPEN FILE FROM WHERE TO LOOK INTO HASHTAGS
    with open(file, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    dictionary = {}
    for i in range(1, len(data)):
        # IGNORE EMPTY ARRAYS IN CSV
        if len(data[i]) > 0:
            hlist = recognizeHashtags(data[i][0])

            for x in hlist:
                # IF IT'S THE FIRST TIME IT'S BEEN FOUND, ADD IT TO THE DICTIONARY AND SET VALUE AS 1 TIME FOUND
                if x not in dictionary:
                    dictionary[x] = 1
                # IF IT ALREADY EXISTS IN DICTIONARY, ADD 1 FOR EACH OCCURRENCE
                elif x in dictionary:
                    dictionary[x] += 1
    # OBTAIN HASHTAGS THAT WE'RE USING RIGHT NOW
    databaseHashtags = obtainHashTags()
    for i in databaseHashtags:
        #ELIMINATE ALL HASHTAGS IN DICTIONARY THAT WE ALREADY USE TO FIND TWEETS
        if i in dictionary:
            del dictionary[i]

    return dictionary


# EXAMPLE USAGE: obtainMostPopular(r"Fandom-Twitter\Data\tweetsData3")
'''RETURNS
{'#BEPARTY': 2, '#Dynamite': 23, '#BestMusicVideo': 19, '#TDYAwards': 13, '#TDYAwards.': 6, '#BTSV': 4,
 '#Taehyung': 5, '#BousnidStars2020': 5, '#Bousnid': 3, '#4thBousnidStars2020': 3, '#btsv': 1,
  '#bousnid': 1, '#LifeGoesOnWithBTS': 2, '#MAMAVOTE': 1, '#Strictly': 1, '#TOTMCI': 1, '#gfvip': 1}
'''




