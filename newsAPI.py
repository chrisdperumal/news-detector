from newsapi import NewsApiClient
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load the English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

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

    def get_article_content(self, url):
        try:
         response = requests.get(url)
         if response.status_code == 200:
             soup = BeautifulSoup(response.text, 'html.parser')
             # Find and extract all text content
             text_content = ' '.join([p.get_text() for p in soup.find_all('p')])
             return text_content
         else:
             print("Error: Unable to fetch content. Status code:", response.status_code)
             return None
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return None

    def sanitize_content(self, content, max_tokens=3500):
        # reduce the number of tokens
        # remove stop words
        # remove urls and hyperlinks
        # remove extra/unnecessary spaces
               
        
        doc = nlp(content)

        # Extract tokens from the processed document
        tokens = [token.text for token in doc]

        # Extract tokens, but without stop words
        tokens = [token.text for token in doc if token.text.lower() not in STOP_WORDS]

        # Limit the number of tokens
        tokens = tokens[:max_tokens]
            # Convert the tokens back to a single string
        text = ' '.join(tokens)

        return text



