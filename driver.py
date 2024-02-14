from newsAPI import NewsFetcher
from chatGPT import ChatGPTDriver


# This class only used for testing purposes. We use server.py to connect to the chrome extension

news_fetcher = NewsFetcher()
chat_gpt_object = ChatGPTDriver()

# Fetch articles with specified keywords
keywords = ['new', 'exhausted', 'find', 'struggles', 'line', 'ukraine', 'men']
all_articles = news_fetcher.get_articles_from_keywords(keywords)
print("Article content!!")

print(all_articles['articles'][0]['content'])
# Specify the file name where you want to save the content
file_name = "article_content.txt"

# Write the content to the file
with open(file_name, "w") as file:
    file.write(all_articles['articles'][0]['content'])

print("Content successfully written to", file_name)
print("After article")
summary = chat_gpt_object.get_summary_from_article(all_articles['articles'][0]['content'])


print(f'No of Articles Retrieved = {all_articles["totalResults"]}')

# chat_gpt_object = cgpt.chatGPT()
# quote = chat_gpt_object.createQuoteFirstTime()
#print(all_articles['articles'][0]['content'])
print("this is my summary")
print(summary)