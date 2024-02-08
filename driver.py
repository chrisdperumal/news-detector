import newsAPI

keywords = ["ukraine", "russia"]
response = newsAPI.get_articles_with_keyword(keywords)

print(f'No of Articles Retrieved = {response["totalResults"]}')