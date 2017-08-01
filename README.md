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
## Results
@bsblcardvandals @realDonaldTrump @GOP I have no idea how you guys continually find such magic in prosaic sports cards. Love it.  
"Sentiment(polarity=0.3333333333333333, subjectivity=0.7000000000000001)"  
This tweet is Positive

@realDonaldTrump You resigned???  
"Sentiment(polarity=0.0, subjectivity=0.0)"  
This tweet is Neutral

"RT @funder: .@realDonaldTrump-  
Please don't make us have #SignSanctionsBill trend. Sign the bill. What In the world are u waiting for?
#T…"  
"Sentiment(polarity=0.0, subjectivity=0.0)"  
This tweet is Neutral  

RT @peplamb: @realDonaldTrump #GOD protect our #Nation #RedeemerLives 🙏❤️💖 #OneNationUnderGOD https://t.co/FBr863h5f5  
"Sentiment(polarity=0.0, subjectivity=0.0)"  
This tweet is Neutral  

"@realDonaldTrump Let Ryan and McConnell Understand, This is A Vote that Must and Will Go Through!! No Matter What !!"  
"Sentiment(polarity=0.0, subjectivity=0.0)"  
This tweet is Neutral  

"RT @tomricks1: @realDonaldTrump Sure, if you're deranged."  
"Sentiment(polarity=0.5, subjectivity=0.8888888888888888)"  
This tweet is Positive

RT @realDonaldTrump: A great day at the White House!  
"Sentiment(polarity=0.4, subjectivity=0.375)"  
This tweet is Positive

@realDonaldTrump Another round of people getting fired . no real direction for the West Wing.... You call this great ? Get together  
"Sentiment(polarity=0.16666666666666666, subjectivity=0.4833333333333334)"  
This tweet is Positive

RT @realDonaldTrump: A great day at the White House!  
"Sentiment(polarity=0.4, subjectivity=0.375)"  
This tweet is Positive

@realDonaldTrump Time to start acting presidential #fakeituntilumakeit  
"Sentiment(polarity=0.0, subjectivity=0.0)"  
This tweet is Neutral

"RT @Harlan: How long before @LindseyGrahamSC stabs General Kelly &amp; @realDonaldTrump in the back?
This week for sure.
#DrainTheSwamp #MAGA…"  
"Sentiment(polarity=0.125, subjectivity=0.4472222222222222)"  
This tweet is Positive

@realDonaldTrump Why does Jared still have security clearance? Why haven't you resigned yet?  What shade of orange… https://t.co/37qslCunj4  
"Sentiment(polarity=0.0, subjectivity=0.0)"  
This tweet is Neutral

@JacobAWohl @realDonaldTrump Inaugural Address suggests otherwise.  
"Sentiment(polarity=0.0, subjectivity=0.0)"  
This tweet is Neutral

@realDonaldTrump No one believes anything you say  
"Sentiment(polarity=0.0, subjectivity=0.0)"  
This tweet is Neutral

"@HSahinen @revndm @LindseyGrahamSC @realDonaldTrump Well,  he was lawfully elected in a bitter contest.  The Left t… https://t.co/zVzA5YbcZD"  
"Sentiment(polarity=-0.03333333333333333, subjectivity=0.16666666666666666)"  
This tweet is Negative

## Conclusion
We can see that this method of sentiment analysis is quite rudimentary, as further inspection into the tweet may show that it is actually not as positive or negative as the analysis shows it to be. This seems to be the case when the analysis uses keywords like "good" to determine positivity when in context it may be used negatively.  
To improve on this project, more accurate sentiment analysis would require breaking down each tweet into tuples containing each word of the tweet. Then we could judge each word separately in terms of their sentiment by neutrality, positivity, negativity, and subjectivity, finally combining each value as an aggregated whole.  
