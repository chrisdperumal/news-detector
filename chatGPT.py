from openai import OpenAI
import os
from dotenv import load_dotenv

class ChatGPTDriver:
    def __init__(self):
        load_dotenv()
        # os.environ["OPENAI_API_KEY"] = self.chatGPT_env_acces_key
        self.client = OpenAI()

        self.current_quote = None

    def createQuoteFirstTime(self):

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "you are comparing articles of different viewpoints with each other as a neutral source"},
                {"role": "user", "content": "Give me 1 motivational quotes"}
            ]
        )

        first_quote = completion.choices[0].message
        self.current_quote = first_quote
        return first_quote

    def get_summary_from_article(self, article):

        request = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert at NLP and processing large volumes of text"},
                {"role": "user", "content": "Summarize this article in 60 words or less"},
                {"role": "user", "content": article}
            ]
        )

        results = request.choices[0].message
        return (results)
