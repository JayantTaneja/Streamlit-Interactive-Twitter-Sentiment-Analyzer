import re
import snscrape.modules.twitter as sntwitter
import pandas as pd
from Sentiment import *



def clean(tweet):    
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", "{}".format(tweet)).split())


def scrape_tweets(search_query, n=10,start=0, end=0):
    
    tweets_list2 = []
    tweets_list3 = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('{} since:{} until:{} lang:en'.format(search_query, start, end)).get_items()):
        if i>=n:
            break
        tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
        po, su = sentiment(tweet.content)
        tweets_list3.append([tweet.date, tweet.id, clean(tweet.content), po, su, tweet.user.username])
        
    # Creating a dataframe from the tweets list above
    tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
    tweets_df3 = pd.DataFrame(tweets_list3, columns=['Datetime', 'Tweet Id', 'Text', 'Polarity', 'Subjectivity', 'Username'])

    return tweets_df2, tweets_df3
