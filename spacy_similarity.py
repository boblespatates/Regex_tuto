import spacy
nlp = spacy.load('fr_core_news_md')

doc_class = nlp(u'résider souper conforter')
doc = nlp(u'déménager manger être deumeurer installer réconforter dorloter')   # create a Doc from raw text

for token_class in doc_class:
    for token_corpus in doc:
        print(token_class.text, token_corpus.text, token_corpus.similarity(token_class), cosine(token_class, token_corpus))


