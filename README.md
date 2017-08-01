# Mini-Project-Twitter-Sentiment-Analysis

## Background

This mini project involves calling tweets from the twitter api that contains a chosen keyword. We then perform rudimentary sentiment analysis on these tweets returning whether the tweet is positive or negative into a csv file along with the tweets.  

## Dependencies
If you haven't already downloaded the tweepy and TextBlob dependencies, do so by inputting the following in the terminal:
pip install tweepy  
pip install textblob  

## Code
Now we can import them in the beginning of our code. We also import csv because we are writing our results to a csv file.  
```python
import tweepy
import csv
from textblob import TextBlob
```  
Not shown here, we have created a twitter app at apps.twitter.com/apps/new(a very easy process just requiring a phone number verified twitter account for registration) in order to obtain our consumer key, consumer secret, access token, and access token secret. These 4 variables are required for us to authenticate with twitter and login. For authentication we use our variable named auth, using the OAuthHandler function. We then call the set_access_token function on the auth variable in order to fully create our authentication variable.  
The API function takes a single authentication variable, and with this we can do all sorts of things like create, delete, and find tweets. In this project we will be searching tweets containing a keyword.
```python 
#we find this in the dashboard after having created our app in the "keys and tokens" tab
consumer_key = 	"enter consumer key"
consumer_secret = "enter consumer secret"

access_token = "enter access token"
access_token_secret = "enter token secret"

#log-in via code
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#create main variable where we do all the twitter magic
api = tweepy.API(auth)
```  
The particular keyword we will be using today is '@realDonaldTrump'.  
We store the list of tweets in a variable called public_tweets using the api.search function. Each search returns 15 tweets; desiring more, we iterate it 5 times so we can get more. We then perform sentiment analysis using the tweepy dependency, which we get from analysis.sentiment. A simple boolean chunk determines whether it is positive or negative.
```python
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
```
csvtomd twitter_sent.csv
