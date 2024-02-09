from openai import OpenAI
import os
import os
from dotenv import load_dotenv

class chatGPT:
    def __init__(self):
        load_dotenv()
        self.chatGPT_env_acces_key = os.environ.get("CHAT_GPT_API_KEY")
        self.current_quote = None

    def createQuoteFirstTime(self):

        os.environ["OPENAI_API_KEY"] = self.chatGPT_env_acces_key

        client = OpenAI()

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "you are comparing articles of different viewpoints with each other as a neutral source"},
                {"role": "user", "content": "Give me 1 motivational quotes"}
            ]
        )

        first_quote = completion.choices[0].message
        self.current_quote = first_quote
        return first_quote

