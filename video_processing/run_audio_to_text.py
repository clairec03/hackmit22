import json

from google.cloud import speech

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./ke-file.json"

import io
client = speech.SpeechClient()

f = open('audio_uri.json')

uri_json = json.load(f)
audio = speech.RecognitionAudio(uri=uri_json['file_uri'])

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="en-US",
    audio_channel_count=2,
    # Enable automatic punctuation
    # enable_automatic_punctuation=True,
    enable_word_time_offsets=True,
    model="latest_long"
)

operation = client.long_running_recognize(config=config, audio=audio)

result = operation.result(timeout=1800)

res = []
transcript_final = ""

for result in result.results:
    alternative = result.alternatives[0]
    print("Transcript: {}".format(alternative.transcript))
    print("Confidence: {}".format(alternative.confidence))

    transcript_final += (alternative.transcript + " ")

    for word_info in alternative.words:
        word = word_info.word
        start_time = word_info.start_time
        end_time = word_info.end_time

        res_cur = (word, start_time.total_seconds())
        res.append(res_cur)

        print(
            f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}"
        )


result = {'transcript':transcript_final, 'timestamps':res}

json_object = json.dumps(result, indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
