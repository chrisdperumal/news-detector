import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(title):    
    doc = nlp(title.lower())  
    
    tokens = []
    for token in doc:
        if token.text not in nlp.Defaults.stop_words and not token.is_punct:
            tokens.append(token.text)

    return set(tokens) 


def filter_nouns(title_keywords):
    nouns = set()
    for word in title_keywords:
        token = nlp(word)[0] # 0 menans to access actual "word" of token, s
        if token.pos_ == "NOUN":
            nouns.add(word)
    return nouns


