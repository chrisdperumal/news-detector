import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load SpaCy English language model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(title):
    # Tokenize the title using SpaCy
    doc = nlp(title.lower())  # Convert to lowercase for consistency

    # Filter out stopwords and punctuation
    tokens = [token.text for token in doc if token.text not in STOP_WORDS and not token.is_punct]

    # Extract keywords based on remaining tokens
    # You can adjust the logic here to suit your specific needs for keyword extraction
    keywords = set(tokens)  # Convert to set to remove duplicates
    return keywords


def filter_nouns(title_keywords):
    nouns = set()
    for word in title_keywords:
        token = nlp(word)[0]  # Tokenize the word and get the first token
        if token.pos_ == "NOUN":
            nouns.add(word)
    return nouns

# Example usage:
article_title = "Zelensky fires Ukraine's military chief in major shakeup nearly two years into war"
keywords = extract_keywords(article_title)
print("Keywords extracted from the title:", keywords)

nouns_only = filter_nouns(keywords)
print("Nouns only:", nouns_only)
