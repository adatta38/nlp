import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
text = "Mary had a little lamb. Her fleece was white as snow"
from nltk.tokenize import word_tokenize, sent_tokenize
sents = sent_tokenize(text)
print(sents)

words = [word_tokenize(sent) for sent in sents]
print(words)
# Output
# [['Mary', 'had', 'a', 'little', 'lamb', '.'], ['Her', 'fleece', 'was', 'white', 'as', 'snow']]


# for sent in sents:
#    words = word_tokenize(sent)
#    print(words)
# Output
# ['Mary had a little lamb.', 'Her fleece was white as snow']
# [['Mary', 'had', 'a', 'little', 'lamb', '.']]
# [['Her', 'fleece', 'was', 'white', 'as', 'snow']]

from nltk.corpus import stopwords
from string import punctuation
customStopWords = set(stopwords.words('english') + list(punctuation))

wordsWOStopwords = [word for word in word_tokenize(text) if word not in customStopWords]
print(wordsWOStopwords)

# Output
# ['Mary', 'little', 'lamb', 'Her', 'fleece', 'white', 'snow']



from nltk.collocations import *
# bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(wordsWOStopwords)
sorted(finder.ngram_fd.items())
