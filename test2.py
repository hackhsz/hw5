import unittest
import tweepy
import requests
import json
import pdb
import sys


def get_api(list1):
    consumer_key = list1[0]
    consumer_secret = list1[1]
    access_token = list1[2]
    access_token_secret = list1[3]

#consumer_key = "f6vIFt5wzo2Hz2eo6d00JW6M2" 
#consumer_secret = "ILrSC7LmyVXtsMZut8lLJwAuEM7ETWwggmdTqs4y1sFMy0JmSZ"
#access_token = "830963633739984896-vp452Pr3TStmUeJO2nBYe65YxwIamSU"
#access_token_secret = "njm9VOv959TiZgg2il0PlsXCdpMuwDhEHUIf82ZbuhnHN"
## Set up your authentication to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) 
    return api



def get_twitter(userinput,api,cache,cachefilename):
    
    unique_identifier = "twitter_{}".format(userinput)
    
    if unique_identifier in cache:
        print("using cache data for ",userinput)
        twitter_results = cache[unique_identifier]
    else:
        print("getting data from internet ", userinput)
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
    list1=["f6vIFt5wzo2Hz2eo6d00JW6M2", "ILrSC7LmyVXtsMZut8lLJwAuEM7ETWwggmdTqs4y1sFMy0JmSZ", "830963633739984896-vp452Pr3TStmUeJO2nBYe65YxwIamSU", "njm9VOv959TiZgg2il0PlsXCdpMuwDhEHUIf82ZbuhnHN"]
    #api=get_api(list1)
    CACHE_FNAME = 'cache_tweet.json'
    api = get_api(list1)
    
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
    
