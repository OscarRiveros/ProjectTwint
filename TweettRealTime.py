import tweepy
import json


class TweetListener(tweepy.StreamListener):

    def on_connect(self):
        print("Estoy conectado")

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print("Error", status_code)


consumer_key = "jZkt2LMgliaUeucoxNkQFHEWm"
consumer_secret = "AOK4p9Vhtof310ulZP7NL4CQ0q2HaR0x1tAlG8EYdGyyEhYpjY"


acces_token = "325792140-nu0tqcsLRwEfzqy08KljmENAg6ROHrOO0DFIvLtQ"
acces_token_secret = "hDabgZG9AMdQKlHyqN57I2sx7nsPWCPuqX6IIYUh3uSLy"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


stream = TweetListener()
streaminApi = tweepy.Stream(auth=api.auth, listener=stream)


streaminApi.filter(
    # follow=["325792140"]#EL ID DEL USUARIO A QUIEN QUIERAS SEGUIR sus twettline
    # track=["PUTAS"]#Trackear tweet por palabras que se estan tuiteando en el momento
    locations=[-56.8278718445, -25.7828682864, -55.0920320008, -24.4399395286]
)
