import sqlite3
from sqlite3 import Error




def create_connection(db_file):
    # CREATE CONNECTION TO DATABASE, CREATES FILE IF DOESN'T EXIST
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table():
    # SQL STATEMENT TO CREATE OUR ONLY TABLE
    connection = create_connection(r"Fandom-Twitter\Data\twitterDatabase.db")
    sqlHashtagsTable = """CREATE TABLE IF NOT EXISTS HashTags (
                                    id integer PRIMARY KEY,
                                    hashtagName text NOT NULL
                                );"""
    try:
        c = connection.cursor()
        c.execute(sqlHashtagsTable)
    except Error as e:
        print(e)


def insertNewHashtag(project):
    # INSERTING DATA INTO OUR UNIQUE TABLE
    connection = create_connection(r"Fandom-Twitter\Data\twitterDatabase.db")
    cur = connection.cursor()
    cur.execute('INSERT INTO HashTags(hashtagName) VALUES(?)', [project])
    connection.commit()
    return cur.lastrowid

def obtainHashTags():
    # OBTAIN ALL CURRENT HASHTAGS IN DATABASE
    connection = create_connection(r"Fandom-Twitter\Data\twitterDatabase.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM HashTags")
    rows = cur.fetchall()
    hashtags = []
    for i in rows:
        hashtags.append(i[1])
    return hashtags

def createTag(tagname):
    # VERIFYING FOR POSSIBLE DUPLICA HASHTAG BEFORE INSERTING
    databaseTags = obtainHashTags()
    duplicate = False
    id = None
    for i in range(len(databaseTags)):
        if databaseTags[i][1] == tagname:
            print("duplicado")
            duplicate = True
    if not duplicate:
        try:
            if (tagname.index("#") == 0):
                id = insertNewHashtag(tagname)
        except:
            print("Not a hashtag")
    return id
            

def mainDatabase():
    # CREATE TABLE IN CASE IT DOESN'T EXIST
    create_table()  
