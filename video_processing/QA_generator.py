import argparse
import glob
import os
import json
import time
import logging
import random
from itertools import chain
from string import punctuation

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader

from transformers import (
    AdamW,
    T5ForConditionalGeneration,
    T5Tokenizer,
    get_linear_schedule_with_warmup
)
class QueGenerator():
  def __init__(self):
    self.que_model = T5ForConditionalGeneration.from_pretrained('C:/Users/Meme_/Downloads/t5_que_gen/t5_que_gen_model/t5_base_que_gen/')
    self.ans_model = T5ForConditionalGeneration.from_pretrained('C:/Users/Meme_/Downloads/t5_que_gen/t5_ans_gen_model/t5_base_ans_gen/')

    self.que_tokenizer = T5Tokenizer.from_pretrained('C:/Users/Meme_/Downloads/t5_que_gen/t5_que_gen_model/t5_base_tok_que_gen/')
    self.ans_tokenizer = T5Tokenizer.from_pretrained('C:/Users/Meme_/Downloads/t5_que_gen/t5_ans_gen_model/t5_base_tok_ans_gen/')
    
    self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    self.que_model = self.que_model.to(self.device)
    self.ans_model = self.ans_model.to(self.device)
  
  def generate(self, text):
    answers = self._get_answers(text)
    questions = self._get_questions(text, answers)
    output = [{'answer': ans, 'question': que} for ans, que in zip(answers, questions)]
    return output
  
  def _get_answers(self, text):
    # split into sentences
    sents = sent_tokenize(text)

    examples = []
    for i in range(len(sents)):
      input_ = ""
      for j, sent in enumerate(sents):
        if i == j:
            sent = "[HL] %s [HL]" % sent
        input_ = "%s %s" % (input_, sent)
        input_ = input_.strip()
      input_ = input_ + " </s>"
      examples.append(input_)
    
    batch = self.ans_tokenizer.batch_encode_plus(examples, max_length=512, pad_to_max_length=True, return_tensors="pt")
    with torch.no_grad():
      outs = self.ans_model.generate(input_ids=batch['input_ids'].to(self.device), 
                                attention_mask=batch['attention_mask'].to(self.device), 
                                max_length=32,
                                # do_sample=False,
                                # num_beams = 4,
                                )
    dec = [self.ans_tokenizer.decode(ids, skip_special_tokens=False) for ids in outs]
    answers = [item.split('[SEP]') for item in dec]
    answers = chain(*answers)
    answers = [ans.strip() for ans in answers if ans != ' ']
    return answers
  
  def _get_questions(self, text, answers):
    examples = []
    for ans in answers:
      input_text = "%s [SEP] %s </s>" % (ans, text)
      examples.append(input_text)
    
    batch = self.que_tokenizer.batch_encode_plus(examples, max_length=512, pad_to_max_length=True, return_tensors="pt")
    with torch.no_grad():
      outs = self.que_model.generate(input_ids=batch['input_ids'].to(self.device), 
                                attention_mask=batch['attention_mask'].to(self.device), 
                                max_length=32,
                                num_beams = 4)
    dec = [self.que_tokenizer.decode(ids, skip_special_tokens=False) for ids in outs]
    return dec
que_generator = QueGenerator()
text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum \
and first released in 1991, Python's design philosophy emphasizes code \
readability with its notable use of significant whitespace."


text2 = '''Computer science (sometimes called computation science or computing science, but not to be confused with computational science or software engineering) is the study of processes that interact with data and that can be represented as data in the form of programs.,
        It enables the use of algorithms to manipulate, store, and communicate digital information.,
        A computer scientist studies theory of computation and the practice of designing software systems.,
        Its fields can be divided into theoretical and practical disciplines. Computational complexity theory is highly abstract, while computer graphics emphasize real-world applications.,
        Programming language theory considers approaches to the description of computational processes, while computer programming itself involves the use of programming languages and complex systems.,
        Human-computer interaction considers the challenges in making computers useful, usable, and accessible.'''

text3  = '''I mean Britain lost its 13 colonies, but later controlled half of Africa and all of India and what makes the recent decolonization. So special is that at least so far? No empires have emerged to replace the ones that fell and this was largely due to World War Two because on some level the Allies were fighting to stop Nazi imperialism Hitler wanted to take over Central Europe and Africa and probably the Middle East and the Allied defeat of the Nazis discredited the whole idea of Empire. So the English French and Americans couldn't very well say to the Colonial troops, who'd fought alongside them. Thank you so much for helping us to thwart Germany's imperialistic Ambitions as a reward. Please hand in your rifle in return to your state of subjugation. Most of the big Colonial Powers, especially France Britain and Japan had been significantly weakened by World War Two by which I mean that large swaths of them look like this. So post-war decolonization happened all over the place the British colony that had once been India became three independent nations, by the way. '''


def clean_responses(responses):

    for i in range(len(responses)):
        responses[i]['answer'] = responses[i]['answer'].replace('<pad>','').replace('</s>','').strip()
        responses[i]['question'] = responses[i]['question'].replace('<pad>','').replace('</s>','').strip()
    responses = [response for response in responses if len(response['answer']) > 0]
    return responses

print(clean_responses(que_generator.generate(text)))
print("---------------------------------------------\n")
print(clean_responses(que_generator.generate(text2)))
print("---------------------------------------------\n")
print(clean_responses(que_generator.generate(text3)))