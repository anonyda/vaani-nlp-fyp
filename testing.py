import spacy

nlp = spacy.load('./NLP-model')
input = nlp("He has high fever take crocin for three days twice a day")

for ent in input.ents:
    print(ent.text, ent.label_)

# tag_entities = [(x, x.ent_iob_, x.ent_type_) for x in nlp(input)]
# print(tag_entities)