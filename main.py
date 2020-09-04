import GetOldTweets3 as got
import pandas as pd
import time
import pyautogui
import csv

username = 'realDonaldTrump'
count = 20

def get_tweets(username, count):
    tweetCriteria = got.manager.TweetCriteria().setUsername(username).setMaxTweets(count)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    user_tweets = [tweet.text for tweet in tweets if tweet.text != ""]

    tweets_df = pd.DataFrame(user_tweets, columns = 'Text')
    tweets_df.to_csv('tweets.csv', quoting=csv.QUOTE_ALL)

    spam(username, count)

def spam(username, count):
    file = open('tweets.csv', 'r')
    reader = csv.reader(file)
    next(reader)
    for tweet in reader:
        print(tweet[1])
        pyautogui.typewrite(tweet[1])
        pyautogui.press('enter')

get_tweets(username, count)