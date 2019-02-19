# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 21:45:24 2019
"""



def sentimentAnalysisFunction(TweetsData):
    from textblob import TextBlob
    import sys, tweepy
    import matplotlib.pyplot as plt
    import pickle
    import numpy as np
    import datetime
    from collections import Counter
    
    def percentage(part, whole):
        return 100*float(part)/float(whole);
    
    positive = 0
    negative = 0
    polarity = 0
    neutral = 0
    count = 0

    for  tweet in TweetsData:
        analysis = TextBlob(tweet.text)
        polarity += analysis.sentiment.polarity
        count = count + 1
        if(analysis.sentiment.polarity < 0.00):
            negative += 1
        elif(analysis.sentiment.polarity == 0):
            neutral += 1
        elif(analysis.sentiment.polarity > 0.00):
            positive += 1
        
        

    positivePercentage = percentage(positive, count)
    negativePercentage = percentage(negative, count)
    neutralPercentage = percentage(neutral, count)

    positive = format(positivePercentage,'.2f')
    negative = format(negativePercentage,'.2f')
    neutral = format(neutralPercentage,'.2f')
    

    labels = ['Positive '+str(positive)+'%','Neutral:' +str(neutral)+'%','Negative:' +str(negative)+'%']
    sizes = [positive,neutral,negative]
    colors = ['yellowgreen','gold','red']
    patches,texts = plt.pie(sizes, colors = colors, startangle = 90)
    plt.legend (patches,labels,loc = 'best')
    plt.title('How people are reacting on Tweets by analyzing ' + str(count) +' Tweets')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
