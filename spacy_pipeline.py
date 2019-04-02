import spacy
lang = 'en'
pipeline = ['tagger', 'parser', 'ner']
data_path = '/usr/local/lib/python3.5/dist-packages/en_core_web_sm/en_core_web_sm-2.0.0'

cls = spacy.util.get_lang_class(lang)   # 1. get Language instance, e.g. English()
nlp = cls()                             # 2. initialise it
for name in pipeline:
    component = nlp.create_pipe(name)   # 3. create the pipeline components
    nlp.add_pipe(component)             # 4. add the component to the pipeline
nlp.from_disk(data_path)


doc = nlp.make_doc(u'This is a sentence')   # create a Doc from raw text
for name, proc in nlp.pipeline:             # iterate over components in order
    doc = proc(doc)                         # apply each component

for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
          [child for child in token.children])
