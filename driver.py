from newsAPI import NewsFetcher
from chatGPT import ChatGPTDriver


# This class only used for testing purposes. We use server.py to connect to the chrome extension

news_fetcher = NewsFetcher()
chat_gpt_object = ChatGPTDriver()

# Fetch articles with specified keywords
keywords = ["Python", "Programming"]
all_articles = news_fetcher.get_articles_from_keywords(keywords)

print(f'No of Articles Retrieved = {all_articles["totalResults"]}')

all_articles = news_fetcher.get_articles_from_keywords(keywords)
num_articles = all_articles['totalResults']

# Retrieve articles in a loop
if(num_articles == 0): exit()

if(num_articles < 10) : max_iterations = num_articles
else: max_iterations = 10

for i in range(num_articles):
    # chat_gpt_object = ChatGPTDriver()
    article_content = news_fetcher.get_article_content(all_articles['articles'][i]['url'])

    if(article_content == None):
        continue

    print(f'Content {i}')
    print(article_content)

    summary = chat_gpt_object.get_summary_from_article(article_content)
    summary_text = str(summary.content)  # Assuming summary is a string

    print(f'Summary {i}')
    print(summary_text)
    print()
