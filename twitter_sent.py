import tweepy
import csv
from textblob import TextBlob

#create 4 variables that authenticating with twitter will require,
#we find this in the dashboard after having created our app in the "keys and tokens" tab
consumer_key = 	"jcjTJAVSOItBGUOdZJdm8gVuz"
consumer_secret = "BPGeqO4533fS14zmrEZWcupGM1A1ZQaWMskliOuTR9q5t2sGit"

access_token = "890701400069480448-IE2mCh9yw3c5ON8GRiLW2OS79jTN3Vr"
access_token_secret = "oW3JA5x7XKqkE0moWhP8gyXxgBn3HDKhr0K7v70ph10ze"

#log-in via code
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#create main variable where we do all the twitter magic
api = tweepy.API(auth)
#now that we have our api variable, we can do all sorts of things like
#create, delete and find tweets
#but we will collect tweets that contain a certain keyword

#store list of tweets
public_tweets = api.search('@realDonaldTrump')

with open('twitter_sentiment.csv', 'w') as file:
	sent = (csv.writer(file))
	for i in range(0,4):
		for tweet in public_tweets:
			analysis = TextBlob(tweet.text)
			sent.writerow([tweet.text])
			sent.writerow([analysis.sentiment])
			if analysis.sentiment.polarity > 0:
				sent.writerow(['This tweet is Positive'])
			elif analysis.sentiment.polarity == 0.0:
				sent.writerow(['This tweet is Neutral'])
			else:
				sent.writerow(['This tweet is Negative'])
			sent.writerow([])



#polarity measures how positive or negative something is,
#subjectivity measures how subjective something is compared to how factual it is.
