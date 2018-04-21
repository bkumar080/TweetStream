#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "987163299950268417-HihOYlm1m1gGNeoyoE5gX5E5qSt9N9i"
access_token_secret = "dWJZ9SLY5vdypRV1rw3eUiW0kYKtmZnnnYmBr9tf6oFJr"
consumer_key = "Zs502adIEZFLBa6sY02VqZDpu"
consumer_secret = "7IpAqNi4cWnYCibcOPXiYMyIecEmo0R59mYJGPwGw0QmBr6tt4"


class listener(StreamListener):
	def on_data(self, data):
		print (data)
		return True

	def on_error(self, status):
		print (status)


#     #This handles Twitter authetification and the connection to Twitter Streaming API
# l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, listener())

#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['donald trump', 'putin', 'barack obama'])
