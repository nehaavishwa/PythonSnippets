__author__ = 'nvishwakarma'

import nltk
import scipy as s


print(nltk.version_info)
'''
print(nltk.app)
nltk.download()
'''

sw = set(nltk.corpus.stopwords.words('english'))
print("Stop word", list(sw)[:10])

gbFiles = nltk.corpus.gutenberg
print("Glutenberg", gbFiles.fileids()[:-5])

text_in_file = gbFiles.sents("austen-emma.txt")
print("Unfiltered", text_in_file[:5])


for sent in text_in_file:
    filtered = [w for w in sent if w.lower() not in sw]
    #print("Filtered", filtered[:5])
    tagged = nltk.pos_tag(filtered)
    #print(tagged)

    words = []
    for word in tagged:
        if word[1] != 'NNP' and word[1] != 'CD':
            words.append(word[0])
    print("Words", words)

'''
def filteredText(text_in_file):
    for sent in text_in_file:
        filtered = [w for w in sent if w.lower() not in sw]
        #print("Filtered", filtered[:5])
        tagged = nltk.pos_tag(filtered)
    return tagged


def tag_word(text_in_file):
    tagged1 = filteredText(text_in_file)
    print(tagged1)
    for word in tagged1:
        if word[1] != 'NNP' and word[1] != 'CD':
            words.append(word[0])
    return words

tag = filteredText(text_in_file)
print(tag)
'''