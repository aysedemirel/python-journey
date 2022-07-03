import tweepy
import time
#insert your Twitter keys here
consumer_key ='xxxxxxx'
consumer_secret='xxxxxxx'
access_token='xxxxxxx'
access_token_secret='xxxxxxx'
twitter_handle='handle'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

list= open('twitter_followers.txt','w')

if(api.verify_credentials):
    print ('We successfully logged in')

user = tweepy.Cursor(api.followers, screen_name=twitter_handle).items()

while True:
    try:
        u = next(user)
        list.write(u.screen_name +' \n')

    except:
        time.sleep(15*60)
        print ('We got a timeout ... Sleeping for 15 minutes')
        u = next(user)
        list.write(u.screen_name +' \n')
list.close()