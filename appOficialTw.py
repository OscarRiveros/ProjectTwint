import tweepy
import json

consumer_key = ""
consumer_secret = ""


acces_token = ""
acces_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# Obtener un TweetLine
for tweet in tweepy.Cursor(api.user_timeline, screen_name="oscarrriveros", tweet_mode="extended").items(1):
    print(json.dumps(tweet._json, indent=2))
# Buscar Tweet
"""for tweet in tweepy.Cursor(api.search, q="COVID19", tweet_mode="extendend").items(10):
    print(tweet._json["text"])"""

# Follow a una cuenta
"""api.create_friendship("MazzoleniJulio")
#Unfollow a una cuenta
api.destroy_friendship("MazzoleniJulio")
#Bloquear a una cuenta
api.create_block("MazzoleniJulio")
#Desbloquear una cuenta
api.destroy_block("MazzoleniJulio")
"""
