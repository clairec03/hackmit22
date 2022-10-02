import re, json, string, math

from scipy import spatial
from sentence_transformers import SentenceTransformer


def splitSentences(transcript):
    res = re.split(r"\. |\! |\? |[\r\n]", transcript)
    for (i, r) in enumerate(res):
        res[i] = r.strip()
    while '' in res:
        res.remove('')
    return res


def isalpha(char):
    return char in string.ascii_letters


def removePunctuation(word):
    if word[-1] in string.punctuation or not isalpha(word[-1]):
        word = (word[:-1])
    if word[0] in string.punctuation or not isalpha(word[-1]) or word[0] == '"':
        word = word[1:]
    return word.lower()


def sentencesTosegments(sentences):
    threshold = 0.55
    minSegmentSize = 6
    segments = [[0]]
    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
    vectors = model.encode(sentences)
    for i in range(1, len(vectors)):
        spatialDistance = spatial.distance.cosine(vectors[i-1], vectors[i])
        # print(spatialDistance)
        if spatialDistance < threshold and len(segments[-1]) >= minSegmentSize:
            segments.append([])
        segments[-1].append(i)
    return segments


def findTimestamps(wordTimes, sentences, segments):
    totalWords = 0
    sentenceLengths = []
    for sentence in sentences:
        sentenceWords = len(sentence.split())
        sentenceLengths.append(sentenceWords)
        totalWords += sentenceWords

    finalTimes = []
    for (start, _) in segments:
        wordIndex = sum(sentenceLengths[:start])
        finalTimes.append(math.ceil(wordTimes[wordIndex][1]))

    return finalTimes


def main():
    transcriptTimestampJson = open('../transcripts/johnGreen.json')
    d = json.load(transcriptTimestampJson)
    transcript = d["transcript"]
    wordTimes = d["timestamps"]
    print("Number of words is:", len(wordTimes))

    sentences = splitSentences(transcript)
    print("\nStarting to find segment groups...")

    def firstLast(l):
        return (l[0], l[-1])
    segments = list(map(firstLast, sentencesTosegments(sentences)))
    print(f"\n{len(segments)} segments found!\n")

    L = findTimestamps(wordTimes, sentences, segments)
    print("\nMarked timestamps!\n")
    
    L = list(zip(L, segments))
    #!  L is an int * (int * int) list, where the first element is a time stamp
    # in seconds, and the int tuple is the start and ending sentences of
    # each corresponding sentence
    print(L)


main()
