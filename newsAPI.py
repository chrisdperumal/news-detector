from newsapi import NewsApiClient
import urllib
import os
from dotenv import load_dotenv

load_dotenv()
newsapi = NewsApiClient(api_key=os.environ.get("NEWS_API_KEY"))

def get_articles_with_keyword(keywords):
    query_string = " AND ".join(s.lower() for s in keywords)
    # query_string = urllib.parse.quote(query_string)
    response = newsapi.get_everything(q=query_string, sort_by="relevancy")
    return response

def get_num_sources():
    sources = newsapi.get_sources()
    length = len(sources['sources'])
    return length