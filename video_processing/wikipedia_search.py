import wikipedia
from bs4 import BeautifulSoup
import re

with open('wiki_words') as f:
    lines = f.readlines()

for line in lines:
    h_articles = wikipedia.search(line, 1, suggestion = False)

    res = []

    print(h_articles)

    def clean_text(text):
        new_text = text
        new_text = re.sub('\[[0-9]*\]', '', new_text)
        return new_text

    def split_sentences(text):
        res = re.split(r"\. |\! |\? |[\r\n]", text)
        for (i, r) in enumerate(res):
            res[i] = r.strip()
        while('' in res):
            res.remove('')
        return res

    def process_text(text):
        text = text.lower()
        sentences = split_sentences(text)
        return sentences

    for article in h_articles:
        page = wikipedia.page(title=article)
        page_html = page.html()
        page_soup = BeautifulSoup(page_html, 'html.parser')
        para = page_soup.find_all('p')
        for p in para:
            p_text = p.get_text()
            p_clean = clean_text(p_text)
            s_clean = process_text(p_clean)
            res.extend(s_clean)

    # for r in res:
    #     print(r)






