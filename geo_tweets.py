# Save co-ordinates from tweets as csv file

import json
import pandas as pd
# import bokeh
# from bokeh.plotting import figure, show
from numpy import NaN 

# get tweets from file
def load_twitter_data(tweets_data_path):
    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    return tweets_data

# get tweet text and co-ordinates of tweets with location data
def pop_tweets(path):
    tweets_data = load_twitter_data(path)
    tweets = pd.DataFrame()

    tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
    tweets['long'] = list(map(lambda tweet: tweet['coordinates']['coordinates'][0]  if tweet['coordinates'] != None else NaN, tweets_data))
    tweets['latt'] = list(map(lambda tweet: tweet['coordinates']['coordinates'][1]  if tweet['coordinates'] != None else NaN, tweets_data))

    return tweets[tweets.latt.notnull()]
    
fname1 = 'tweets_poke.txt'
fname2 = 'tweets_poke2.txt'
fname3 = 'tweets_poke3.txt'

geo_tweets1 = pop_tweets(fname1)
geo_tweets2 = pop_tweets(fname2)
geo_tweets3 = pop_tweets(fname3)

geo_tweets = pd.concat([geo_tweets1, geo_tweets2, geo_tweets3], ignore_index=True)

print('total geo_tweets:', len(geo_tweets)) # Tweets with location data
print geo_tweets[1:4] #sanitycheck

# Save geo data
df1 = pd.DataFrame(geo_tweets.long)
df2 = pd.DataFrame(geo_tweets.latt)
df1.to_csv('poke_long.csv', sep='\t', encoding='utf-8', index =False)
df2.to_csv('poke_latt.csv', sep='\t', encoding='utf-8', index = False)

