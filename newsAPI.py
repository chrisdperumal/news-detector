from newsapi import NewsApiClient
import os
from dotenv import load_dotenv

class NewsFetcher:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        # Initialize NewsApiClient with API key
        self.newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

    def get_articles_from_keywords(self, keywords):
        """
        Fetch articles based on the given list of keywords.

        :param keywords: List of keywords to search for.
        :return: Response from the News API.
        """
        print("In newsfetcher")
        print(keywords)
        query_string = " AND ".join(s.lower() for s in keywords)
        response = self.newsapi.get_everything(q=query_string, sort_by="relevancy")
        return response

    def get_num_sources(self):
        """
        Get the total number of sources available in the News API.

        :return: The number of sources.
        """
        sources = self.newsapi.get_sources()
        length = len(sources['sources'])
        return length
