import yake
kw_extractor = yake.KeywordExtractor()
text = """spaCy is an open-source software library for advanced natural language processing, 
written in the programming languages Python and Cython. The library is published under the 
MIT license and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion.whether you'll be easily persuaded by empty political rhetoric; and whether you'll be"""
language = "en"
max_ngram_size = 1 
deduplication_threshold = 0.9
numOfKeywords = text.count('.')
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
tuples = custom_kw_extractor.extract_keywords(text)
keywords = []
for kw in tuples:
    keywords.append(kw[0])
print(keywords)