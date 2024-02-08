import requests
from bs4 import BeautifulSoup

def extract_title_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string
        return title
    except Exception as e:
        print("An error occurred:", str(e))
        return None

# Example usage:
article_url = "https://www.post-gazette.com/sports/penguins/2024/02/08/pittsburgh-penguins-tv-broadcast-josh-getzoff-colby-armstrom/stories/202402050110"
title = extract_title_from_url(article_url)
if title:
    print("Title of the article:", title)
else:
    print("Failed to extract the title from the provided URL.")