from flask import Flask, request, jsonify
from chatGPT import ChatGPTDriver
from newsAPI import NewsFetcher
from getArticleContent import getArticleContent
import extractKeywords
import sys
print(sys.path)
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

    # You can process the data here
    article_url = all_articles['articles'][0]['url']
    
   # randomURL = 'https://www.bbc.com/news/world-europe-68255490'
    articleContent = article_content_fetcher.fetch_article_content(article_url)
    
    # Tokenize the article content
    tokens = tokenize_text(articleContent)
    print(tokens)
    
    
    # You can process the truncated content here to get the summary
    summary = chat_gpt_object.get_summary_from_article(tokens)

    print("OOOOOOOOOOOOOOOOOOOOOO ")

    print("This is my SUMMMMAAARY ")
    print(summary)
    print("OOOOOOOOOOOOOOOOOOOOOO ")

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



import spacy

# Load the English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

def tokenize_text(text, max_tokens=3000):
    # Process the text with spaCy
    doc = nlp(text)
    
    # Extract tokens from the processed document
    tokens = [token.text for token in doc]
    
    # Limit the number of tokens
    tokens = tokens[:max_tokens]
        # Convert the tokens back to a single string
    text = ' '.join(tokens)
    
    return text


