from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s


#consumer key, consumer secret, access token, access secret.
ckey="tUlQTiVnvbUaZikbD3tgX5a0u"
csecret="HQnydy0rBJo297K7bYj5EKEyoMALQ25jmfZKh71xajaZQYzlmQ"
atoken="587441240-g8F4hEJzQjlkW03lLVbKvesfZneTKeBuMRRdWdY3"
asecret="0hqtiUmJGIIwrLvExJRfIzUhBkL5rb97JweIEXr8OrQ7V"


class listener(StreamListener):
    def __init__(self,keyword):
        self.keyword = keyword

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        print(tweet.encode('utf-8'),self.keyword)
        sentiment_value, confidence = s.sentiment(tweet)
        '''if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(tweet.encode("utf-8"))
            output.write('\n')
            output.close()'''
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

class tweet_stream_controller:

    def __init__(self,keyword):
        self.keyword = keyword

    def start_stream(self):
        self.twitterStream = Stream(auth, listener(self.keyword))
        self.twitterStream.filter(track=[self.keyword],languages=['en'],is_async=True)

    def end_stream (self):
        self.twitterStream.disconnect()

