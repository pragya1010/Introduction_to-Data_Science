import tweepy
import sys
from textblob import TextBlob
import matplotlib.pyplot as plt



#Authenticate
consumer_key = 'XXXX'
consumer_secret ='XXXX'
access_token = 'XXXX'
access_token_secret = 'XXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 3 - Retrieve Tweets
#public_tweets = api.search('Trump')
tag = 'Trump'
num = 100
public_tweets = tweepy.Cursor(api.search, q = tag, result_type="recent").items(num)

# CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
# and label each one as either 'positive' or 'negative', depending on the sentiment
# You can decide the sentiment polarity threshold yourself

#

def percentage(part, whole):
    percentage = 100* (float(part)/float(whole))
    return percentage

neutral  = 0
positive = 0
negative = 0
polarity = 0
wpositive = 0
spositive = 0
wnegative = 0
snegative = 0

for tweet in public_tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    # if analysis.sentiment.polarity == 0:
    #     neutral+=1
    # elif analysis.sentiment.polarity < 0.0:
    #     negative+=1
    # elif analysis.sentiment.polarity > 0.0:
    #     positive +=1
    if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
        neutral += 1
    elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
        wpositive += 1
    elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
        positive += 1
    elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
        spositive += 1
    elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
        wnegative += 1
    elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
        negative += 1
    elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
        snegative += 1


# positive = percentage(positive, num)
# negative = percentage(negative, num)
# neutral = percentage(neutral, num)
positive = percentage(positive, num)
wpositive = percentage(wpositive, num)
spositive = percentage(spositive, num)
negative = percentage(negative, num)
wnegative = percentage(wnegative, num)
snegative = percentage(snegative, num)
neutral = percentage(neutral, num)

polarity = polarity/ num
print("polarity: {}".format(polarity))
print("Positive: {}, wpositive: {}, spositive: {}, Negative: {}, wnegative: {},snegative: {},  Neutral: {}".
      format(positive, wpositive,spositive, negative,wnegative,snegative ,neutral))

if (polarity == 0):
        print("Neutral")
elif (polarity > 0 and polarity <= 0.3):
        print("Weakly Positive")
elif (polarity > 0.3 and polarity <= 0.6):
        print("Positive")
elif (polarity > 0.6 and polarity <= 1):
        print("Strongly Positive")
elif (polarity > -0.3 and polarity <= 0):
        print("Weakly Negative")
elif (polarity > -0.6 and polarity <= -0.3):
        print("Negative")
elif (polarity > -1 and polarity <= -0.6):
        print("Strongly Negative")

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')


print("Results on ", tag)

# if polarity == 0:
#     print("Neutral")
# elif polarity > 0:
#     print("Positive")
# elif polarity <0 :
#     print("Negative")

# finding average of how people are reacting

labels = ['Positive [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]','Strongly Positive [' + str(spositive) + '%]', 'Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]', 'Strongly Negative [' + str(snegative) + '%]']
sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
colors = ['yellowgreen','lightgreen','darkgreen', 'gold', 'red','lightsalmon','darkred']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on ' + tag + ' by analyzing ' + str(num) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()


#
#     # Step 4 Perform Sentiment Analysis on Tweets
#     analysis = TextBlob(tweet.text)
#     print(analysis)
#     print(analysis.sentiment)
#     print("")