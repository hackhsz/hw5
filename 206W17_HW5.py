import unittest
import tweepy
import requests
import json
import twitter_info
import pdb
import sys





## SI 206 - W17 - HW5
## COMMENT WITH: Shizhong Hu
## Your section day/time: Thursday 6pm
## Any names of people you worked with on this assignment: None

######## 500 points total ########

## Write code that uses the tweepy library to search for tweets with a phrase of the user's choice (should use the Python input function), and prints out the Tweet text and the created_at value (note that this will be in GMT time) of the first THREE tweets with at least 1 blank line in between each of them, e.g.

## TEXT: I'm an awesome Python programmer.
## CREATED AT: Sat Feb 11 04:28:19 +0000 2017

## TEXT: Go blue!
## CREATED AT: Sun Feb 12 12::35:19 +0000 2017




def get_api():
    consumer_key = twitter_info.consumer_key
    consumer_secret = twitter_info.consumer_secret
    access_token = twitter_info.access_token
    access_token_secret = twitter_info.access_token_secret
## Set up your authentication to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) # Set up library to grab stuff from twitter with your authentication, and return it in a JSON-formatted way
    return api



def get_twitter(userinput,api,cache,cachefilename):
    
    unique_identifier = "twitter_{}".format(userinput)
    
    if unique_identifier in cache:
        print("using cache data for ",userinput)
        print("\n")
        twitter_results = cache[unique_identifier]
    else:
        print("getting data from internet ", userinput)
        print("\n")
        twitter_results = api.search(userinput)
        cache[unique_identifier] = twitter_results
        f = open(cachefilename,'w')
        f.write(json.dumps(cache))
        f.close
    tweet_texts = []
    tweet_time = []
    for tweet in twitter_results["statuses"]:
        tweet_texts.append(tweet["text"])
        #        pdb.set_trace()
        tweet_time.append(tweet["created_at"])
    tweet_texts = tweet_texts[:3]
    tweet_time = tweet_time[:3]
    dict1 = {}
    dict1 = dict(zip(tweet_texts,tweet_time))
    return dict1


def printfun(dict1):
    for key,value  in dict1.items():
        print("TEXT:", key)
        print("CREATED AT:", value)
        print("\n")

def main(argv):
    CACHE_FNAME = 'cache_tweet.json'
    api = get_api()
    
    try:
        cache_file = open(CACHE_FNAME,'r')
        cache_contents = cache_file.read()
        
        CACHE_DICTION = json.loads(cache_contents)
        cache_file.close()
    
    except:
        CACHE_DICTION = {}
    
    myinput = input("please input here :")
    ressults={}
    ressults = get_twitter(myinput,api,CACHE_DICTION,CACHE_FNAME)
    printfun(ressults)


if __name__ == "__main__":
    main(sys.argv[1:])








