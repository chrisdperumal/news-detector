import newsAPI
import chatGPT as chat_gpt_class

keywords = ["ukraine", "russia"]
response = newsAPI.get_articles_with_keyword(keywords)

print(f'No of Articles Retrieved = {response["totalResults"]}')

chat_gpt_object = chat_gpt_class.chatGPT()
quote = chat_gpt_object.createQuoteFirstTime()
print(quote)