import pke

import numpy as np
from sense2vec import Sense2Vec

from textwrap3 import wrap

import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer

import random
import numpy as np

import nltk

from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize

from nltk.corpus import stopwords
import string
import pke
import traceback


from flashtext import KeywordProcessor

from collections import OrderedDict
from sklearn.metrics.pairwise import cosine_similarity

from similarity.normalized_levenshtein import NormalizedLevenshtein

from sentence_transformers import SentenceTransformer


import gradio as gr

# -*- coding: utf-8 -*-
"""Question Generation using NLP - Data Science Milan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SSf6va2loI8VDSh0qota2FQiE4SMLwPT

## Author of this notebook : Ramsri Goutham Golla

Linkedin: https://www.linkedin.com/in/ramsrig/

Twitter : https://twitter.com/ramsri_goutham

Udemy Course: **[Question generation using NLP Course](https://www.udemy.com/course/question-generation-using-natural-language-processing/?referralCode=C8EA86A28F5398CBF763)**

## Installation of libraries
"""

# !pip install --quiet transformers==4.5.0
# !pip install --quiet sentencepiece==0.1.95
# !pip install --quiet textwrap3==0.9.2
# !pip install --quiet nltk==3.2.5

# Commented out IPython magic to ensure Python compatibility.
# !pip install --quiet ipython-autotime
# %load_ext autotime

"""## Example 1

Text taken from: 
https://gadgets.ndtv.com/internet/news/dogecoin-price-rally-surge-elon-musk-tweet-twitter-working-developers-improve-transaction-efficiency-2442120
"""

from textwrap3 import wrap

text = """Elon Musk has shown again he can influence the digital currency market with just his tweets. After saying that his electric vehicle-making company
Tesla will not accept payments in Bitcoin because of environmental concerns, he tweeted that he was working with developers of Dogecoin to improve
system transaction efficiency. Following the two distinct statements from him, the world's largest cryptocurrency hit a two-month low, while Dogecoin
rallied by about 20 percent. The SpaceX CEO has in recent months often tweeted in support of Dogecoin, but rarely for Bitcoin.  In a recent tweet,
Musk put out a statement from Tesla that it was “concerned” about the rapidly increasing use of fossil fuels for Bitcoin (price in India) mining and
transaction, and hence was suspending vehicle purchases using the cryptocurrency.  A day later he again tweeted saying, “To be clear, I strongly
believe in crypto, but it can't drive a massive increase in fossil fuel use, especially coal”.  It triggered a downward spiral for Bitcoin value but
the cryptocurrency has stabilised since.   A number of Twitter users welcomed Musk's statement. One of them said it's time people started realising
that Dogecoin “is here to stay” and another referred to Musk's previous assertion that crypto could become the world's future currency."""

for wrp in wrap(text, 150):
  print (wrp)
print ("\n")

"""Musk tweeted that his electric vehicle-making company tesla will not accept payments in bitcoin because of environmental concerns. He also said that
the company was working with developers of dogecoin to improve system transaction efficiency. The world's largest cryptocurrency hit a two-month low,
while doge coin rallied by about 20 percent. Musk has in recent months often tweeted in support of crypto, but rarely for bitcoin.

## Example 2

http://read.gov/aesop/007.html
"""

# text = """A Lion lay asleep in the forest, his great head resting on his paws. A timid little Mouse came upon him unexpectedly, and in her fright and haste to
# get away, ran across the Lion's nose. Roused from his nap, the Lion laid his huge paw angrily on the tiny creature to kill her.  "Spare me!" begged
# the poor Mouse. "Please let me go and some day I will surely repay you."  The Lion was much amused to think that a Mouse could ever help him. But he
# was generous and finally let the Mouse go.  Some days later, while stalking his prey in the forest, the Lion was caught in the toils of a hunter's
# net. Unable to free himself, he filled the forest with his angry roaring. The Mouse knew the voice and quickly found the Lion struggling in the net.
# Running to one of the great ropes that bound him, she gnawed it until it parted, and soon the Lion was free.  "You laughed when I said I would repay
# you," said the Mouse. "Now you see that even a Mouse can help a Lion." """

# text = """Hi, I'm John Green. This is crash course world history. And today we're going to talk about decolonization. The Empire's European states formed in the 19th century proved about as stable and long-lasting as Genghis Khan's leading to so many of the nation states. We know and love today. Yes. I'm looking at you Burundi. Did you ever know your mind your everything?  And don't cut to the intro I think like an angel.  So unless you're over 60 and let's face it internet. You're not you've only ever known a world of nation states. But as we've seen from Egypt to Alexander the Great to China to Rome to the Mongols who for once are not the exception here.  To the Ottomans and the Americas Empire has long been the dominant way. We've organized ourselves politically or at least the way that other people have organized us. It's a great Mr. Green. So to them Star Wars would have been like a completely different movie. Most of them would have been like go Empire Crush those Rebels. Yeah. Also, they'd be like, what is this screen that displays crisp moving images of events that are not currently occurring also not to get off topic but you never learned what happens after the rebel victory in Star Wars and as we've learned from the French Revolution to the Arab Spring Revolution is often the easy part." """
# text = """You remember early when I said that Gandhi harken back to a mythologized Indian past.  Well, it turns out.  that  hunger striking in India goes back all the way to like the 5th Century. BCE hunger strikes have been used around the world including British in American suffer Jets who hunger struck to get the vote and in pre-christian Ireland when you felt wrong by someone it was common practice to sit on their doorstep and hunger strike until you're grievance was addressed and sometimes it even works. I really admire you hunger Strikers, but I lacked the courage of your convictions. Also, this is an amazing cupcake.  Both long room since Independence, India has largely been a success story. Although we will talk about the complexity of India's emerging global capitalism next week for now though. Let's travel east to Indonesia a huge nation of over 13,000 islands that has largely been ignored here on crash course world history due to our longstanding bias against islands. Like we haven't even mentioned Greenland on this show the greenlanders, of course haven't complained because they don't  So the Dutch exploited their Island colonies with the system of culture stessil in which all peasants had to set aside one-fifth of their land to grow cash crops for export to the Netherlands this accounted for 25% of the total Dutch national budget and it explains why they have all kinds of fancy buildings despite technically living underwater. They're like sea monkeys this system was rather less popular in Indonesia, and the Dutch didn't offer much in exchange. They couldn't even defend their colony from the Japanese who occupied it for most of World War Two during which time the Japanese furthered the cause of Indonesian nationalism by placing native Indonesians in more prominent positions of power including sukarno who became Indonesia's first prime minister after the war the Dutch with British help try to hold on to their Indonesian colonies with so-called police actions, which went on for more than four years before Indonesia." """
text = """They're like sea monkeys this system was rather less popular in Indonesia, and the Dutch didn't offer much in exchange. They couldn't even defend their colony from the Japanese who occupied it for most of World War Two during which time the Japanese furthered the cause of Indonesian nationalism by placing native Indonesians in more prominent positions of power including sukarno who became Indonesia's first prime minister after the war the Dutch with British help try to hold on to their Indonesian colonies with so-called police actions, which went on for more than four years before Indonesia. Finally won its independence in 1950 over in the French colonies of Indochina so called because they were neither Indian nor Chinese things were even more violent. The end of colonization was disastrous in Cambodia where the 17-year reign of noradam cyano gave way to the rise of the Khmer Rouge.  Massacred a stunning 21% of cambodia's population between 1975 and 1979 in Vietnam the French fought communist LED nationalists, especially Ho Chi Minh from almost the moment World War Two ended until 1954 when the French were defeated and then the Americans heard that there was a land War available in Asia. So they quickly took over from the French and communist did not fully control Vietnam until 1975 despite still being ostensibly communist Vietnam. Now manufacturers all kinds of stuff that we like in America, especially sneakers more about that next week too." """

for wrp in wrap(text, 150):
  print (wrp)
print ("\n")

"""# **Summarization with T5**"""

import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
summary_model = T5ForConditionalGeneration.from_pretrained('t5-base')
summary_tokenizer = T5Tokenizer.from_pretrained('t5-base')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
summary_model = summary_model.to(device)

import random
import numpy as np

def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

set_seed(42)

import nltk
nltk.download('punkt')
nltk.download('brown')
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize

def postprocesstext (content):
  final=""
  for sent in sent_tokenize(content):
    sent = sent.capitalize()
    final = final +" "+sent
  return final


def summarizer(text,model,tokenizer):
  text = text.strip().replace("\n"," ")
  text = "summarize: "+text
  # print (text)
  max_len = 512
  encoding = tokenizer.encode_plus(text,max_length=max_len, pad_to_max_length=False,truncation=True, return_tensors="pt").to(device)

  input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

  outs = model.generate(input_ids=input_ids,
                                  attention_mask=attention_mask,
                                  early_stopping=True,
                                  num_beams=3,
                                  num_return_sequences=1,
                                  no_repeat_ngram_size=2,
                                  min_length = 75,
                                  max_length=300)


  dec = [tokenizer.decode(ids,skip_special_tokens=True) for ids in outs]
  summary = dec[0]
  summary = postprocesstext(summary)
  summary= summary.strip()

  return summary


summarized_text = summarizer(text,summary_model,summary_tokenizer)


print ("\noriginal Text >>")
for wrp in wrap(text, 150):
  print (wrp)
print ("\n")
print ("Summarized Text >>")
for wrp in wrap(summarized_text, 150):
  print (wrp)
print ("\n")

"""# **Answer Span Extraction (Keywords and Noun Phrases)**"""

# !pip install --quiet git+https://github.com/boudinfl/pke.git@dc4d5f21e0ffe64c4df93c46146d29d1c522476b
# !pip install --quiet flashtext==2.7

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import pke
import traceback

def get_nouns_multipartite(content):
    out=[]
    try:
        extractor = pke.unsupervised.MultipartiteRank()
        #    not contain punctuation marks or stopwords as candidates.
        pos = {'PROPN','NOUN'}
        #pos = {'PROPN','NOUN'}
        stoplist = list(string.punctuation)
        stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
        stoplist += stopwords.words('english')
        extractor.load_document(input=content, stoplist=stoplist)
        extractor.candidate_selection(pos=pos)
        # 4. build the Multipartite graph and rank candidates using random walk,
        #    alpha controls the weight adjustment mechanism, see TopicRank for
        #    threshold/method parameters.
        extractor.candidate_weighting(alpha=1.1,
                                      threshold=0.75,
                                      method='average')
        keyphrases = extractor.get_n_best(n=15)
        

        for val in keyphrases:
            out.append(val[0])
    except:
        out = []
        traceback.print_exc()

    return out

from flashtext import KeywordProcessor


def get_keywords(originaltext,summarytext):
  keywords = get_nouns_multipartite(originaltext)
  print ("keywords unsummarized: ",keywords)
  keyword_processor = KeywordProcessor()
  for keyword in keywords:
    keyword_processor.add_keyword(keyword)

  keywords_found = keyword_processor.extract_keywords(summarytext)
  keywords_found = list(set(keywords_found))
  print ("keywords_found in summarized: ",keywords_found)

  important_keywords =[]
  for keyword in keywords:
    if keyword in keywords_found:
      important_keywords.append(keyword)

  return important_keywords[:4]


imp_keywords = get_keywords(text,summarized_text)
print (imp_keywords)

"""# **Question generation with T5**"""

question_model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_squad_v1')
question_tokenizer = T5Tokenizer.from_pretrained('ramsrigouthamg/t5_squad_v1')
question_model = question_model.to(device)

def get_question(context,answer,model,tokenizer):
  text = "context: {} answer: {}".format(context,answer)
  encoding = tokenizer.encode_plus(text,max_length=384, pad_to_max_length=False,truncation=True, return_tensors="pt").to(device)
  input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

  outs = model.generate(input_ids=input_ids,
                                  attention_mask=attention_mask,
                                  early_stopping=True,
                                  num_beams=5,
                                  num_return_sequences=1,
                                  no_repeat_ngram_size=2,
                                  max_length=72)


  dec = [tokenizer.decode(ids,skip_special_tokens=True) for ids in outs]


  Question = dec[0].replace("question:","")
  Question= Question.strip()
  return Question



for wrp in wrap(summarized_text, 150):
  print (wrp)
print ("\n")

for answer in imp_keywords:
  ques = get_question(summarized_text,answer,question_model,question_tokenizer)
  print (ques)
  print (answer.capitalize())
  print ("\n")

"""# **Gradio UI Visualization**"""

# !pip install --quiet gradio==1.6.4

import gradio as gr

context = gr.inputs.Textbox(lines=10, placeholder="Enter paragraph/content here...")
output = gr.outputs.HTML(  label="Question and Answers")


def generate_question(context):
    summary_text = summarizer(context,summary_model,summary_tokenizer)
    for wrp in wrap(summary_text, 150):
      print (wrp)
    np =  get_keywords(context,summary_text)
    print ("\n\nNoun phrases",np)
    output=""
    for answer in np:
      ques = get_question(summary_text,answer,question_model,question_tokenizer)
      # output= output + ques + "\n" + "Ans: "+answer.capitalize() + "\n\n"
      output = output + "<b style='color:blue;'>" + ques + "</b>"
      # output = output + "<br>"
      output = output + "<b style='color:green;'>" + "Ans: " +answer.capitalize()+  "</b>"
      output = output + "<br>"

    summary ="Summary: "+ summary_text
    for answer in np:
      summary = summary.replace(answer,"<b>"+answer+"</b>")
      summary = summary.replace(answer.capitalize(),"<b>"+answer.capitalize()+"</b>")
    output = output + "<p>"+summary+"</p>"
    
    return output

iface = gr.Interface(
  fn=generate_question, 
  inputs=context, 
  outputs=output)
iface.launch(debug=True)

"""# **Filter keywords with Maximum marginal Relevance**"""

# !pip install --quiet keybert==0.2.0
# !pip install --quiet strsim==0.0.3
# !pip install --quiet sense2vec==1.0.2

# !wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
# !tar -xvf  s2v_reddit_2015_md.tar.gz

import numpy as np
from sense2vec import Sense2Vec
s2v = Sense2Vec().from_disk('s2v_old')

from sentence_transformers import SentenceTransformer
# paraphrase-distilroberta-base-v1
sentence_transformer_model = SentenceTransformer('msmarco-distilbert-base-v3')

from similarity.normalized_levenshtein import NormalizedLevenshtein
normalized_levenshtein = NormalizedLevenshtein()

def filter_same_sense_words(original,wordlist):
    filtered_words=[]
    base_sense =original.split('|')[1] 
    print (base_sense)
    for eachword in wordlist:
      if eachword[0].split('|')[1] == base_sense:
        filtered_words.append(eachword[0].split('|')[0].replace("_", " ").title().strip())
    return filtered_words

def get_highest_similarity_score(wordlist,wrd):
    score=[]
    for each in wordlist:
      score.append(normalized_levenshtein.similarity(each.lower(),wrd.lower()))
    return max(score)

def sense2vec_get_words(word,s2v,topn,question):
    output = []
    print ("word ",word)
    try:
      sense = s2v.get_best_sense(word, senses= ["NOUN", "PERSON","PRODUCT","LOC","ORG","EVENT","NORP","WORK OF ART","FAC","GPE","NUM","FACILITY"])
      most_similar = s2v.most_similar(sense, n=topn)
      # print (most_similar)
      output = filter_same_sense_words(sense,most_similar)
      print ("Similar ",output)
    except:
      output =[]

    threshold = 0.6
    final=[word]
    checklist =question.split()
    for x in output:
      if get_highest_similarity_score(final,x)<threshold and x not in final and x not in checklist:
        final.append(x)
    
    return final[1:]

def mmr(doc_embedding, word_embeddings, words, top_n, lambda_param):

    # Extract similarity within words, and between words and the document
    word_doc_similarity = cosine_similarity(word_embeddings, doc_embedding)
    word_similarity = cosine_similarity(word_embeddings)

    # Initialize candidates and already choose best keyword/keyphrase
    keywords_idx = [np.argmax(word_doc_similarity)]
    candidates_idx = [i for i in range(len(words)) if i != keywords_idx[0]]

    for _ in range(top_n - 1):
        # Extract similarities within candidates and
        # between candidates and selected keywords/phrases
        candidate_similarities = word_doc_similarity[candidates_idx, :]
        target_similarities = np.max(word_similarity[candidates_idx][:, keywords_idx], axis=1)

        # Calculate MMR
        mmr = (lambda_param) * candidate_similarities - (1-lambda_param) * target_similarities.reshape(-1, 1)
        mmr_idx = candidates_idx[np.argmax(mmr)]

        # Update keywords & candidates
        keywords_idx.append(mmr_idx)
        candidates_idx.remove(mmr_idx)

    return [words[idx] for idx in keywords_idx]

from collections import OrderedDict
from sklearn.metrics.pairwise import cosine_similarity

def get_distractors_wordnet(word):
    distractors=[]
    try:
      syn = wn.synsets(word,'n')[0]
      
      word= word.lower()
      orig_word = word
      if len(word.split())>0:
          word = word.replace(" ","_")
      hypernym = syn.hypernyms()
      if len(hypernym) == 0: 
          return distractors
      for item in hypernym[0].hyponyms():
          name = item.lemmas()[0].name()
          #print ("name ",name, " word",orig_word)
          if name == orig_word:
              continue
          name = name.replace("_"," ")
          name = " ".join(w.capitalize() for w in name.split())
          if name is not None and name not in distractors:
              distractors.append(name)
    except:
      print("Wordnet distractors not found")
    return distractors

def get_distractors (word,origsentence,sense2vecmodel,sentencemodel,top_n,lambdaval):
  distractors = sense2vec_get_words(word,sense2vecmodel,top_n,origsentence)
  print("distractors ",distractors)
  if len(distractors) ==0:
    return distractors
  distractors_new = [word.capitalize()]
  distractors_new.extend(distractors)
  # print ("distractors_new .. ",distractors_new)

  embedding_sentence = origsentence+ " "+word.capitalize()
  # embedding_sentence = word
  keyword_embedding = sentencemodel.encode([embedding_sentence])
  distractor_embeddings = sentencemodel.encode(distractors_new)

  # filtered_keywords = mmr(keyword_embedding, distractor_embeddings,distractors,4,0.7)
  max_keywords = min(len(distractors_new),5)
  filtered_keywords = mmr(keyword_embedding, distractor_embeddings,distractors_new,max_keywords,lambdaval)
  # filtered_keywords = filtered_keywords[1:]
  final = [word.capitalize()]
  for wrd in filtered_keywords:
    if wrd.lower() !=word.lower():
      final.append(wrd.capitalize())
  final = final[1:]
  return final

sent = "What cryptocurrency did Musk rarely tweet about?"
keyword = "Bitcoin"

# sent = "What did Musk say he was working with to improve system transaction efficiency?"
# keyword= "Dogecoin"


# sent = "What company did Musk say would not accept bitcoin payments?"
# keyword= "Tesla"


# sent = "What has Musk often tweeted in support of?"
# keyword = "Cryptocurrency"

print("Hellow")

print(get_distractors(keyword,sent,s2v,sentence_transformer_model,40,0.2))

"""# **Gradio Visualization with MCQs**"""

import gradio as gr

context = gr.inputs.Textbox(lines=10, placeholder="Enter paragraph/content here...")
output = gr.outputs.HTML(  label="Question and Answers")
radiobutton = gr.inputs.Radio(["Wordnet", "Sense2Vec"])

def generate_question(context,radiobutton):
  summary_text = summarizer(context,summary_model,summary_tokenizer)
  for wrp in wrap(summary_text, 150):
    print (wrp)
  # np = getnounphrases(summary_text,sentence_transformer_model,3)
  np =  get_keywords(context,summary_text)
  print ("\n\nNoun phrases",np)
  print("\n\nH11")
  output=""
  for answer in np:
    ques = get_question(summary_text,answer,question_model,question_tokenizer)
    print("\n\nH1")
    if radiobutton=="Wordnet":
      print("\n\nH12")
      distractors = get_distractors_wordnet(answer)
    else:
      print("\n\nH13")
      distractors = get_distractors(answer.capitalize(),ques,s2v,sentence_transformer_model,40,0.2)
    # output= output + ques + "\n" + "Ans: "+answer.capitalize() + "\n\n"
    output = output + "<b style='color:blue;'>" + ques + "</b>"
    # output = output + "<br>"
    output = output + "<b style='color:green;'>" + "Ans: " +answer.capitalize()+  "</b>"
    print("\nDistractors\n")
    print(distractors)
    if len(distractors)>0:
      for distractor in distractors[:4]:
        output = output + "<b style='color:brown;'>" + distractor+  "</b>"
    output = output + "<br>"

  summary ="Summary: "+ summary_text
  for answer in np:
    summary = summary.replace(answer,"<b>"+answer+"</b>")
    summary = summary.replace(answer.capitalize(),"<b>"+answer.capitalize()+"</b>")
  output = output + "<p>"+summary+"</p>"
  return output


iface = gr.Interface(
  fn=generate_question, 
  inputs=[context,radiobutton], 
  outputs=output)
iface.launch(debug=True)