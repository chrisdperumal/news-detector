from newsapi import NewsApiClient
import urllib
newsapi = NewsApiClient(api_key='35fcaa0b17104f39a0577eafe921d94e')

def get_articles_with_keyword(keywords):
    query_string = " AND ".join(s.lower() for s in keywords)
    # query_string = urllib.parse.quote(query_string)
    response = newsapi.get_everything(q=query_string, sort_by="relevancy")
    return response

def get_num_sources():
    sources = newsapi.get_sources()
    length = len(sources['sources'])
    return length