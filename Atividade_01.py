import nltk

minha_string = "O usuário enfrenta o problema de criar essa lista manualmente."

tokens = nltk.word_tokenize(minha_string)
print(tokens)