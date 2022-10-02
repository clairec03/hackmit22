from this import d
from text_extractor import best_keyword, text, answers, wrong_answers 
import requests
import json

# API_URL = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-question-generation-ap"
headers = {"Authorization": f"Bearer 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"}
API_URL = "https://api-inference.huggingface.co/models/Narrativa/mT5-base-finetuned-tydiQA-question-generation"
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def oldquery(payload):
        response = requests.post("https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-question-generation-ap", headers=headers, json=payload)
        return response.json()	

def get_questions_answers(query_str):
        d = {}
        kw = best_keyword[0]
        output = query([f"answer: {kw}: {query_str}"]).split(':')
        d['question'] = output[1]
        d['answer'] = answers[0]
        d['options'] = wrong_answers[0][:3]
        return d

query_str =  '''Computer science (sometimes called computation science or computing science, but not to be confused with computational science or software engineering) is the study of processes that interact with data and that can be represented as data in the form of programs.,
        It enables the use of algorithms to manipulate, store, and communicate digital information.,
        A computer scientist studies theory of computation and the practice of designing software systems.,
        Its fields can be divided into theoretical and practical disciplines. Computational complexity theory is highly abstract, while computer graphics emphasize real-world applications.,
        Programming language theory considers approaches to the description of computational processes, while computer programming itself involves the use of programming languages and complex systems.,
        Human-computer interaction considers the challenges in making computers useful, usable, and accessible.'''

query_str = text
print(best_keyword)

final_json = []
for i in range(len(best_keyword)):
        kw = best_keyword[i]
        # print("printing keyword")
        # print(kw)
        # output = query({"inputs": f"answer: {kw} context: {query_str}"})
        res = dict()
        output = query([f"answer: {kw}: {query_str}"])
        print("printing NEW output")
        print(output)
        print("printing OLD output")
        oldout = (oldquery({"inputs": f"answer: {kw} context: {query_str}"}))

        # out = output[0]
        # question = out['generated_text'].split(': ')
        # print(question[1])
        answer = answers[i]
        print("good answer:")
        print(answer)
        print("bad answer:")
        print(wrong_answers[i])
        options = wrong_answers[i].append(answers[i])
        print(options)
        res_q = {'question': output, 'answer': answer, 'options':wrong_answers[i]}
        final_json.append(res_q)
        final_json.append({'question': oldout, 'answer': answer, 'options':wrong_answers[i]})


out_file = open("questions.json", "w")
  
json.dump(final_json, out_file, indent = 4)
  
out_file.close()
