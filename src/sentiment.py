# -*- coding: utf-8 -*-
# sentiment.py
from snownlp import SnowNLP

def analyze_sentiment(text):
    if not text: return 0.5
    return SnowNLP(text).sentiments

