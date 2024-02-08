import requests

def fetch_article(api_key, query, language):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}&pageSize=1&language={language}"
    response = requests.get(url)
    data = response.json()
    
    if data["totalResults"] > 0:
        article = data["articles"][0]
        print("Title:", article["title"])
        print("Source:", article["source"]["name"])
        print("Published At:", article["publishedAt"])
        print("Content:", article["content"])
    else:
        print("No articles found for the query:", query)

api_key = "371a76c13f6c43cb828a1933781f7947"
query = "Duquesne"
language = "us"  # Specify the language here, e.g., "en" for English
fetch_article(api_key, query, country)