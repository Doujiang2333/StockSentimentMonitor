# -*- coding: utf-8 -*-
# db.py
import sqlite3

def create_table_if_not_exists():
    conn = sqlite3.connect("../data/stock_sentiment.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS sentiment_data (
                    id INTEGER PRIMARY KEY,
                    stock_name TEXT,
                    sentiment REAL,
                    source TEXT,
                    title TEXT,
                    content TEXT
                )""")
    conn.commit()
    conn.close()

def get_existing_titles():
    conn = sqlite3.connect("../data/stock_sentiment.db")
    c = conn.cursor()
    c.execute("SELECT title FROM sentiment_data ORDER BY id DESC LIMIT 2048")
    existing_titles = [row[0] for row in c.fetchall()]
    conn.close()
    return existing_titles

def save_to_database(stock_name, sentiment, source, title, content):
    conn = sqlite3.connect("../data/stock_sentiment.db")
    c = conn.cursor()
    c.execute("INSERT INTO sentiment_data (stock_name, sentiment, source, title, content) VALUES (?, ?, ?, ?, ?)", (stock_name, sentiment, source, title, content))
    conn.commit()
    conn.close()