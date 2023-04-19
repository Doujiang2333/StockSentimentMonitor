# -*- coding: utf-8 -*-
# scraper.py
import requests
from bs4 import BeautifulSoup
import json
import time

def fetch_data(stock_name):
    # 新浪财经
    sina_url = f"https://search.sina.com.cn/?q={stock_name}&c=news&range=title&num=10&sort=time"
    sina_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    sina_response = requests.get(sina_url, headers=sina_headers)
    sina_soup = BeautifulSoup(sina_response.text, "html.parser")
    sina_news_list = sina_soup.find_all("div", class_="r-info r-info2")

    # 腾讯财经
    tencent_url = f"https://r.inews.qq.com/gw/pc_search/result?is_pc=1&hippy_custom_version=10&search_type=all&search_count_limit=10&page=0&query={stock_name}"
    tencent_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    tencent_response = requests.get(tencent_url, headers=tencent_headers)
    tencent_soup = BeautifulSoup(tencent_response.text, "html.parser")
    tencent_news_list = [("腾讯财经", i.get('newsList')[0].get('longtitle'), i.get('newsList')[0].get('abstract'), i.get('newsList')[0].get('shareUrl')) \
                         for i in json.loads(tencent_soup.text).get('secList') if i.get('newsList')]

    news_content = []

    # 新浪财经数据处理
    for news in sina_news_list:
        title = news.find("a").text
        content = news.find("p", class_="content").text
        href = news.find("a").get("href")
        news_content.append(("新浪财经", title, content, href))

    # 腾讯财经数据处理
        news_content.extend(tencent_news_list)
    time.sleep(1)
    return news_content
