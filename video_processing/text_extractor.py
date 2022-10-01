import yake
from bs4 import BeautifulSoup
import requests
# from rake_nltk import Rake
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')

# r = Rake()

# Extraction given the text.
 
forbidden_words = ["Wiktionary", "Wikipedia"]
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

# r.extract_keywords_from_text(text)
# print(r.get_ranked_phrases())


language = "en"
max_ngram_size = 1 
deduplication_threshold = 0.9
numOfKeywords = 20 
# text.count('.')
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
tuples = custom_kw_extractor.extract_keywords(text)
keywords = []
options = {}
wrong_ans_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None) 
for kw in tuples:
    keyword = kw[0].lower()
    keywords.append(keyword)
    # get URL
    # print(keyword)
    page = requests.get(f"https://en.wikipedia.org/wiki/{keyword}") 
    parser = BeautifulSoup(page.content, 'html.parser')
    source = parser.find_all('p')[0].get_text()
    wrong_tuples = wrong_ans_extractor.extract_keywords(source) 
    wrong_ans = []
    counter = 0
    for tup in wrong_tuples:
        related = tup[0].lower()
        if tup[0] not in forbidden_words and related != keyword:
            wrong_ans.append(related.lower())
            counter += 1
        if (counter == 3):
            break
    # wrong_ans = [tup[0] for tup in wrong_tuples]
    if (wrong_ans != []): options[keyword.lower()] = wrong_ans 
print(options)