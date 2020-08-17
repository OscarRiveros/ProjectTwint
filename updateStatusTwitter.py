import tweepy
import json

consumer_key = ""
consumer_secret = ""

acces_token = ""
acces_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# Enviar Tweet a mi cuenta
# api.update_status(".")
# Obtener un TweetLine
for tweet in tweepy.Cursor(api.user_timeline, screen_name="@user", tweet_mode="extended").items(1):
    print(json.dumps(tweet._json, indent=2))
