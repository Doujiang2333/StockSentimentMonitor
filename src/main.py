# -*- coding: utf-8 -*-
# main.py
from config import FILTER_KEY_WORDS, STOCK_LIST
from scraper import fetch_data
from sentiment import analyze_sentiment
from db import create_table_if_not_exists, get_existing_titles, save_to_database
from email_util import send_email

class Counter(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]

def find_by_keywords(text, filter_list=FILTER_KEY_WORDS):
    for pair_words in FILTER_KEY_WORDS:
        for word in pair_words:
            if not word in text:
                return False
        else:
            return True
    else:
        return False

def main():
    create_table_if_not_exists()
    existing_titles = set(get_existing_titles())
    negative_sentiments = Counter()
    
    for stock_name in STOCK_LIST:
        news_list = fetch_data(stock_name)
        for source, title, content, href in news_list:
            if title not in existing_titles:
                sentiment = (analyze_sentiment(title) + analyze_sentiment(content)) / 2
                save_to_database(stock_name, sentiment, source, title, content)
                existing_titles.add(title)
                if not find_by_keywords(title):
                    negative_sentiments[f'{stock_name}'].append(f"{source}_{sentiment:.2f}:《{title}》{content}\n{href}\n\n")
                    
    if negative_sentiments:
        email_content = ""
        for stock_name, neg_news in negative_sentiments.items():
            email_content = email_content + f"【{stock_name}】舆情监控提醒\n" + "".join(neg_news)
        send_email(email_content)

if __name__ == "__main__":
    main()

