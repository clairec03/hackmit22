from text_extractor import best_keyword, text, answers, wrong_answers 
import requests

# API_URL = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-question-generation-ap"
headers = {"Authorization": f"Bearer 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"}
API_URL = "https://api-inference.huggingface.co/models/Narrativa/mT5-base-finetuned-tydiQA-question-generation"
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def oldquery(payload):
        response = requests.post("https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-question-generation-ap", headers=headers, json=payload)
        return response.json()	

query_str =  '''Computer science (sometimes called computation science or computing science, but not to be confused with computational science or software engineering) is the study of processes that interact with data and that can be represented as data in the form of programs.,
        It enables the use of algorithms to manipulate, store, and communicate digital information.,
        A computer scientist studies theory of computation and the practice of designing software systems.,
        Its fields can be divided into theoretical and practical disciplines. Computational complexity theory is highly abstract, while computer graphics emphasize real-world applications.,
        Programming language theory considers approaches to the description of computational processes, while computer programming itself involves the use of programming languages and complex systems.,
        Human-computer interaction considers the challenges in making computers useful, usable, and accessible.'''

query_str = text
print(best_keyword)
for i in range(len(best_keyword)):
        kw = best_keyword[i]
        # print("printing keyword")
        # print(kw)
        # output = query({"inputs": f"answer: {kw} context: {query_str}"})
        output = query([f"answer: {kw}: {query_str}"])
        print("printing NEW output")
        print(output)
        print("printing OLD output")
        print(oldquery({"inputs": f"answer: {kw} context: {query_str}"}))
        # out = output[0]
        # question = out['generated_text'].split(': ')
        # print(question[1])
        answer = answers[i]
        print("good answer:")
        print(answer)
        print("bad answer:")
        print(wrong_answers[i])