from flask import Flask, request, jsonify
import newsAPI
from chatGPT import ChatGPTDriver
from newsAPI import NewsFetcher

app = Flask(__name__)

# Creating this globally will allow us to remember the entire chat session
chat_gpt_object = ChatGPTDriver()
news_fetcher = NewsFetcher()

#make calls to this server from chrome extension

@app.route("/")
def hello_world():
    hello_world_string = "<p>Welcome to News Analyzer</p>"
    return(hello_world_string)

#This endpoint listends to the POST request made by JavaScript
@app.route('/v1/keywords', methods=['POST'])
def handle_post():
    # Retrieve JSON data from the request
    keywords = request.get_json()
    all_articles = newsAPI.get_articles_from_keywords(keywords)
    num_articles = all_articles['totalResults']

    # You can process the data here
    article = all_articles['articles'][0]['content']
    summary = chat_gpt_object.get_summary_from_article(article) 

    print(summary)

    # For this example, just send back the received JSON
    return jsonify({"received": summary}), 200