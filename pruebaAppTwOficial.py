import tweepy
import json

consumer_key = ""
consumer_secret = ""


acces_token = ""
acces_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# Obtener mi informacion
"""data = api.me()
print json.dumps(data._json, indent=2)"""
# Obtener informacion de otro usuario
"""data = api.get_user("@user")
print json.dumps(data._json, indent=2)"""
# Obtener followers de usuarios
#data = api.followers(screen_name="MazzoleniJulio")
"""for user in data:
    print json.dumps(user._json, indent=2)
    print len(data)"""

for user in tweepy.Cursor(api.followers, screen_name="@user").items(100):
    print json.dumps(user._json, indent=2)
