import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


'''
PRAW:
https://praw.readthedocs.io/en/latest/index.html

VADER:
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.


'''

reddit = praw.Reddit( #client id, secret, agent)


top100 = reddit.subreddit('all').hot(limit=100)
analyze = SentimentIntensityAnalyzer()


for submission in top100:
    IS = analyze.polarity_scores(submission.title)
    print(submission.title)
    print("Intensity ratings: {}".format(IS))
    print(submission.ups)
    print(submission.id)
    print(submission.shortlink)
    print('\n')
