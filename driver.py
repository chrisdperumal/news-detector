import newsAPI
import chatGPT as cgpt

# This class only used for testing purposes. We use server.py to connect to the chrome extension

keywords = ["ukraine", "russia"]
response = newsAPI.get_articles_from_keywords(keywords)

print(f'No of Articles Retrieved = {response["totalResults"]}')

# chat_gpt_object = cgpt.chatGPT()
# quote = chat_gpt_object.createQuoteFirstTime()
print(response['articles'][0]['content'])