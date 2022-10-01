from sent2vec.vectorizer import Vectorizer
from scipy import spatial
import numpy as np

def sentences2clusters(sentences):

    threshold = 0.05 #TODO Find a good threshold
    #TODO remove once the parser is working
    sentences = [
        "The computers in recent times have become relevant too particularly in the areas of storage and dissemination of information.",
        "The ease with which the computer function, i.e. the speed, accuracy, and readiness", 
        "With the usefulness of the computer, it has become fashionable for organizations to be computerized, that is, a computer department is created to serve the whole organization and expert or professionals are employed to manage the department.",  
        "It is today becoming increasingly difficult for computer illiterates to get good employments, as computer literacy is now a pre-requisite for most jobs. The world is becoming a global village through the use of a computer, thus there is a need for everyone to be computer Educated.",
        "The computer age was characterized by the generation of computers, which signified that the computer had passed through stages of evolution or development.",
        "Before we could arrive at the present-day computers, it has undergone stages of development known as the generation of computer.", #should cut here 

        "A computer is an electronic device used to store retrieve and manipulate data.",
        "A computer also defines as a programmable electromechanical device that accepts instruction (program) to direct the operations of the computers.",
        "Examples, i. Store: To put data somewhere for safekeeping, ii. Retrieve: To get and bring the data back., iii. Process: To calculate compare arrange.", #should cut here

        "Computer science (sometimes called computation science or computing science, but not to be confused with computational science or software engineering) is the study of processes that interact with data and that can be represented as data in the form of programs.",
        "It enables the use of algorithms to manipulate, store, and communicate digital information.",
        "A computer scientist studies theory of computation and the practice of designing software systems.",
        "Its fields can be divided into theoretical and practical disciplines. Computational complexity theory is highly abstract, while computer graphics emphasize real-world applications.",
        "Programming language theory considers approaches to the description of computational processes, while computer programming itself involves the use of programming languages and complex systems.",
        "Human-computer interaction considers the challenges in making computers useful, usable, and accessible."

    ]
    vectorizer = Vectorizer()
    vectorizer.run(sentences)
    vectors = vectorizer.vectors

    n_sentences = len(vectors)

    clusters = [[0]]
    for i in range(1, n_sentences):
        if spatial.distance.cosine(vectors[i-1], vectors[i]) < threshold:
            clusters.append([])
        clusters[-1].append(i)
    return clusters
