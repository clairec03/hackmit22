import yake
from bs4 import BeautifulSoup
import requests
import nltk
nltk.download('averaged_perceptron_tagger')

# Extraction given the text.
 
forbidden_words = ["isn’t", "don’t", "word"]
kw_extractor = yake.KeywordExtractor()
text = """
DISADVANTAGE: Farming is hard. So hard in fact that one is tempted to claim ownership
over other humans and then have them till the land on your behalf, which is the kind
of non-ideal social order that tends to be associated with agricultural communities.
So why did agriculture happen?
Wait, I haven't talked about herders. Herders, man! Always getting the short end of the stick.
Herding is a really good and interesting alternative to foraging and agriculture. You domesticate
some animals and then you take them on the road with you. The advantages of herding are
obvious. First, you get to be a cowboy. Also, animals provide meat and milk, but they also
help out with shelter because they can provide wool and leather.
The downside is that you have to move around a lot because your herd always needs new grass,
which makes it hard to build cities, unless you are the Mongols. [music, horse hooves]
By the way, over the next forty weeks you will frequently hear generalizations, followed
"""

text = '''Computer science (sometimes called computation science or computing science, but not to be confused with computational science or software engineering) is the study of processes that interact with data and that can be represented as data in the form of programs.,
        It enables the use of algorithms to manipulate, store, and communicate digital information.,
        A computer scientist studies theory of computation and the practice of designing software systems.,
        Its fields can be divided into theoretical and practical disciplines. Computational complexity theory is highly abstract, while computer graphics emphasize real-world applications.,
        Programming language theory considers approaches to the description of computational processes, while computer programming itself involves the use of programming languages and complex systems.,
        Human-computer interaction considers the challenges in making computers useful, usable, and accessible.'''

text = '''Playing around with nuclear weapons in videos is fun.
There's a visceral joy in blowing things up, and a horrifying fascination with things like fireballs, shockwaves, and radiation.
And while it does help put our destructive power in perspective, it's not the best way of understanding the real impact of a nuclear explosion. This isn't about silly stacks of TNT, or about how bright an explosion is. Nuclear weapons are about you.
So we've partnered with the Red Cross and Red Crescent movement to explore what would really happen if a nuclear weapon were detonated in a major city today. Not nuclear war, just one explosion.'''

text.strip()

lower = ord('a')
upper = ord('z')

def isalpha(char): # because the original python function fails to filter all strange characters
    order = ord(char)
    return (lower <= order and order <= upper)

import string
def removePunctuation(word):
    if (word == ''): return word
    if word[-1] in string.punctuation or not isalpha(word[-1]):
        word = (word[:-1])
    if (word == ''): return word
    if word[0] in string.punctuation or not isalpha(word[-1]) or word[0] == '“':
        word = word[1:] 
    return word.lower()

encodings = nltk.pos_tag(text.split()) # (string * string) list

language = "en"
max_ngram_size = 1
deduplication_threshold = 0.9
num_keywords = 10

custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=num_keywords, features=None)
wrong_ans_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=num_keywords, features=None)

keywords_tuples = custom_kw_extractor.extract_keywords(text)

options = dict()
    

def findWrong(keyword, tag):
    page = requests.get(f"https://www.dictionary.com/browse/{keyword}")
    
    parser = BeautifulSoup(page.content, 'html.parser')
    found = parser.find_all('p')
    if len(found) == 0: return found
    source = found[0].get_text()
    # print(source)
    # wrong_tuples = wrong_ans_extractor.extract_keywords(source) # All potential wrong answers 
    candidates = source.split() 
    # print(candidates)
    res = []
#    candidates = [candidate[0] for candidate in wrong_tuples] # Potential wrong words
    mappings = nltk.pos_tag(candidates) # Potential wrong words with tags
    for mapping in mappings:
        candidate = mapping[0].lower()
        candidate_tag = mapping[1]
        # print(f"_tag {candidate_tag}")
        # print(f"candidate: {candidate}, tag: {tag}")
        if candidate_tag == tag and keyword != candidate and candidate not in forbidden_words:
            tobeappended = removePunctuation(candidate)
            if (tobeappended != ''): res.append(tobeappended)
    return res

best_keyword = []
answers = []
wrong_answers = []
for kw in keywords_tuples:
    keyword = kw[0]
    # print(keyword)
    related = findWrong(keyword, (nltk.pos_tag([keyword]))[0][1])
    # print(related)
    if (len(related) >= 3):
        best_keyword.append(related)
        answers.append(keyword)
        wrong_answers.append(related)