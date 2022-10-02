import yake
from bs4 import BeautifulSoup
import requests
import nltk
nltk.download('averaged_perceptron_tagger')

# Extraction given the text.
 
forbidden_words = ["isn’t", "don’t", "word"]
kw_extractor = yake.KeywordExtractor()
text = """
DISADVANTAGE: Farming is hard. So hard in fact that one is tempted to claim ownership over other humans and then have them till the land on your behalf, which is the kind of non-ideal social order that tends to be associated with agricultural communities. Wait, I haven't talked about herders. Herders, man! Always getting the short end of the stick. Herding is a really good and interesting alternative to foraging and agriculture. You domesticate some animals and then you take them on the road with you. The advantages of herding are obvious. First, you get to be a cowboy. Also, animals provide meat and milk, but they also help out with shelter because they can provide wool and leather. The downside is that you have to move around a lot because your herd always needs new grass, which makes it hard to build cities, unless you are the Mongols. [music, horse hooves] By the way, over the next forty weeks you will frequently hear generalizations, followed """
text = '''
The things on the stage can affect the stage itself, stretching and warping it. If the old stage was like unmoving hardwood, Einstein's stage is more like a waterbed. This kind of elastic space can be bent and maybe even torn and patched together, which could make wormholes possible. Let's see what that would look like in 2D. Our universe is like a big flat sheet, bent in just the right way, wormholes could connect two very, very distant spots with a short bridge that you could cross almost instantane­ously.
Enabling you to travel the universe even faster than the speed of light. So, where can we find a wormhole? Presently, only on paper. General relativity says they might be possible, but that doesn't mean they have to exist. General relativity is a mathematic­al theory. It's a set of equations that have many possible answers, but not all maths describes reality.
But they are theoretica­lly possible and there are different kinds. The first kind of wormholes to be theorized were Einstein Rosen Bridges. They describe every black hole as a sort of portal to an infinite parallel universe. Let's try to picture them in 2D again. Empty space time is flat, but curved by objects on it.'''

# text = '''The world has changed in the past few years, with world leaders again explicitly and publicly threatening each other with nuclear weapons. Many experts think the danger of a nuclear strike is higher than it has been in decades. Governments tell their citizens that it's good that we have nuclear weapons, but it's bad when anyone else gets them. That it's somehow necessary to threaten others with mass destruction to keep us safe. But does this make you feel safe? It only takes a small group of people with power to go crazy or rogue, a small misstep or a simple misunderstanding to unleash a catastrophe of unimaginable proportions. Exploding stuff in videos is fun. Exploding things in real life, not so much. There is a solution though!'''


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

language = "en"
max_ngram_size = 2
deduplication_threshold = 0.9
num_keywords = 10

custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=num_keywords, features=None)
wrong_ans_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=num_keywords, features=None)

keywords_tuples = custom_kw_extractor.extract_keywords(text)
print("kw_tupes")
print(keywords_tuples)
options = dict()
    

def findWrong(keyword, tag):
    page = requests.get(f"https://www.dictionary.com/browse/{keyword}")
    
    parser = BeautifulSoup(page.content, 'html.parser')
    found = parser.find_all('p')
    candidates = []
    for word in keyword.split(' '):
        page = requests.get(f"https://www.dictionary.com/browse/{keyword}")
        parser = BeautifulSoup(page.content, 'html.parser')
        found = parser.find_all('p')
        if len(found) == 0: continue
        source = found[0].get_text()
        candidates += source.split()
    if len(candidates) == 0: return [] 

    # print(source)
    # wrong_tuples = wrong_ans_extractor.extract_keywords(source) # All potential wrong answers 
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
    keyword = kw[0].lower()
    # print(keyword)
    related = findWrong(keyword, (nltk.pos_tag([keyword]))[0][1])
    # print(related)
    if (len(related) >= 3):
        best_keyword.append(keyword)
        answers.append(keyword)
        wrong_answers.append(related)