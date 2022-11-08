import spacy

nlp = spacy.load("en_core_web_sm")

Garden_path_Sentences = ["The old man the boat.",
                         "The complex houses married and single soldiers and their families.",
                         "The horse raced past the barn fell.",
                         "The florist sent the flowers was pleased.",
                         "The cotton clothing is made of grows in Mississippi.",
                         "The sour drink from the ocean."]

for sample in Garden_path_Sentences:
    doc = nlp(sample)
    doc.text.split()
    print([token.orth_ for token in doc])

    # tokenisation
    print([(i, i.label_, i.label) for i in doc.ents])  # entity recognition

# For the fifth sentence Spacy gave mississipi as entity.
