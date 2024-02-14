import requests

from bs4 import BeautifulSoup
class getArticleContent:
    @staticmethod
    def fetch_article_content(url):
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

