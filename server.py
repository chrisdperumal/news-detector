from flask import Flask, request, jsonify
from chatGPT import ChatGPTDriver
from newsAPI import NewsFetcher
from getArticleContent import getArticleContent
import extractKeywords
# import sys
# print(sys.path)
import spacy


app = Flask(__name__)
# runs on default on port 5000
# Creating this globally will allow us to remember the entire chat session
chat_gpt_object = ChatGPTDriver()
news_fetcher = NewsFetcher()
article_content_fetcher = getArticleContent

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
    print("These are my keywords")
    print(keywords)
    all_articles = news_fetcher.get_articles_from_keywords(keywords['keywords'])

    num_articles = all_articles['totalResults']

    print("nnum of articles")
    print( num_articles)

    # Retrieve articles in a loop
    if(num_articles == 0):
        return jsonify({"summary_text": "Cannot retrieve articles for this combination of keywords, try using less keywords"}), 200


    if(num_articles < 10) : max_iterations = num_articles
    else: max_iterations = 5

    summaries_string=""
    for i in range(max_iterations):

        article_content = news_fetcher.get_article_content(all_articles['articles'][i]['url'])

        if(article_content == None):
            print("There was no article content extracted")
            continue

        article_content = news_fetcher.sanitize_content(article_content)

        print(f'Content {i}')
        print(article_content)

        summary = chat_gpt_object.get_summary_from_article(article_content)
        summary_text = str(summary.content)  # Assuming summary is a string

        print(f'Summary {i}')
        print(summary_text)
        print()

        summaries_string += f"{i}: {summary_text}"
    
        
    biases_overArching= chat_gpt_object.get_over_arching_biases_from_summaries(summary_text)
    print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
    print(biases_overArching)
    summarized_summaries = chat_gpt_object.get_summary_from_summaries(summary_text)
    print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQq")
    print(summarized_summaries)
    
    
    
    # Convert list to a single string with elements separated by a space
    keywords_string = ' '.join(keywords)

    # For this example, just send back the received JSON
    return jsonify({"summary_text": summarized_summaries, "biases_overArching": biases_overArching}), 200



@app.route('/v1/getkeywords', methods=['POST'])
def handle_post_getkw():
    # Retrieve JSON data from the request
    data = request.get_json()

    title = data.get('title')
    title_keywords =extractKeywords.extract_keywords(title)

    print("Keywords extracted:", title_keywords)
    return jsonify({"keywords": list(title_keywords)}), 200






