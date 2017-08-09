#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 17:01:40 2017

@author: guneevkaur
"""


import twitter
from textblob import TextBlob
import numpy as np

api= twitter.Api(consumer_key ='VlpGONYTyAhJUx9PLQpIArsyN',
consumer_secret = 'TNG1WywE8KJ2WAz3gQOuEo1t4zRrjQGagZit1u2QZEN2Wdag0K',
access_token_key='868519422683754496-V70azTQoybotl09fA48qSYxJ2XQWz9S',
access_token_secret='SWhadCYtKQPRfYD3BUNLT5FxNg6qBwf7inIXe9CwcVl5M')

#Getting a list of status object where every object represent a tweet 
tweets= api.GetUserTimeline(screen_name='realDonaldTrump',count=10)


#converting it to a dictionary and storing it to a list 
#tweets = [i.asdict() for i in t]
#print tweets[0]


pub_tweets = []

for tweet in tweets:
    pub_tweets.append(tweet.text)
  

#pub_tweets =public_tweets.encode('ascii','ignore')

print pub_tweets 


tweet_count = len(pub_tweets)                    
senti = np.chararray((1,tweet_count), itemsize = 8)
emotion = np.empty([1, tweet_count])

for i in range (tweet_count):
    analysis = TextBlob(pub_tweets[i])
    
    emotion[0, i] = analysis.sentiment.polarity      #storing polarity for tweets
    #sentiment according to polarity thresholds of negative, 0 and positive 
    #values respectively
    if emotion [0, i] < 0:
        senti[0, i] = 'negative'
    elif emotion [0, i] == 0:
        senti[0, i] ='neutral'
    else:
        senti[0, i] = 'positive'
        
file = open('sentiment_analysis.csv', 'w')

for i in range (tweet_count):
    
    file.write((pub_tweets[i]).encode('utf-8'))
    print pub_tweets[i]
    
    file.write(', ')
    
    file.write(str(senti[0, i]));
              
    file.write('\n')

file.close()
