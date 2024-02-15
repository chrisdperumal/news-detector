from openai import OpenAI
import os
from dotenv import load_dotenv

class ChatGPTDriver:
    def __init__(self):
        load_dotenv()
        os.environ["OPENAI_API_KEY"] = self.chatGPT_env_acces_key

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
    
    
    def get_summary_from_summaries(self, summaries):
        
        request = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert at NLP and processing large volumes of text"},
                {"role": "user", "content": "Summarize these summarized articles to one one sentence summary."},
                {"role": "user", "content": summaries}
            ]
        )

        results = request.choices[0].message.content
        return (results)
    
    def get_over_arching_biases_from_summaries(self, summaries):
           
        request = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in news biases and compare different summarized news articles to each other"},
                {"role": "user", "content": "Tell me if the summaries from the articles I give you have the same news/biases in them. They are numbered. Keep your answer 1 short sentence"},
                {"role": "user", "content": summaries}
            ]
        )

        results = request.choices[0].message.content
        return (results)
    
    def translate_key_words_to_german(self, keywords):
        
        request = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a translator from english into german"},
                {"role": "user", "content": "Translate these words"},
                {"role": "user", "content": keywords}
            ]
        )

        results = request.choices[0].message.content
        return (results)
        
