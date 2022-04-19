import spacy


nlp = spacy.load("en_core_web_sm")
doc = nlp('we need 2 tickets to Dublin, and 1/2 a spoon of milk')
l = []

for token in doc:
    token_text, token_pos = token.text, token.pos_
    if token_pos == 'PROPN' or token_pos == 'NUM':
        l.append(token_text)

string = " ".join(l)
for i in l:
    print(f'{i}: {string.count(i)}')
