from newsAPI import NewsFetcher
from chatGPT import ChatGPTDriver


# This class only used for testing purposes. We use server.py to connect to the chrome extension

news_fetcher = NewsFetcher()
chat_gpt_object = ChatGPTDriver()

# Fetch articles with specified keywords
keywords = ["Python", "Programming"]
all_articles = news_fetcher.get_articles_from_keywords(keywords)

print(f'No of Articles Retrieved = {all_articles["totalResults"]}')

# chat_gpt_object = cgpt.chatGPT()
# quote = chat_gpt_object.createQuoteFirstTime()
print(all_articles['articles'][0]['content'])