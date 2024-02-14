from flask import Flask, request, jsonify
from chatGPT import ChatGPTDriver
from newsAPI import NewsFetcher
import extractKeywords

app = Flask(__name__)
# runs on default on port 5000
# Creating this globally will allow us to remember the entire chat session
chat_gpt_object = ChatGPTDriver()
news_fetcher = NewsFetcher()

#make calls to this server from chrome extension

@app.route("/")
def hello_world():
    hello_world_string = "<p>Welcome to News Analyzer</p>"
    return(hello_world_string)

@app.route('/v1/getSummary', methods=['POST'])
def handle_post():
    print("Hello Maxi")
    # Retrieve JSON data from the request
    keywords = request.get_json()
    all_articles = news_fetcher.get_articles_from_keywords(keywords)
    num_articles = all_articles['totalResults']

    # You can process the data here
    article = all_articles['articles'][0]['content']
    summary = chat_gpt_object.get_summary_from_article(article)


    summary_text = str(summary)  # Assuming summary is a string
    print(summary_text)

    # For this example, just send back the received JSON
    return jsonify({"summary_text": summary_text}), 200



@app.route('/v1/getkeywords', methods=['POST'])
def handle_post_getkw():
    # Retrieve JSON data from the request
    data = request.get_json()
    
    title = data.get('title')
    title_keywords =extractKeywords.extract_keywords(title)
    
    print("Keywords extracted:", title_keywords)
    return jsonify({"keywords": list(title_keywords)}), 200



