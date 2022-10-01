import moviepy.editor as mp

import speech_recognition as sr


# my_clip = mp.VideoFileClip(r"C:\Users\Meme_\Downloads\Y2Mate.is - Decolonization and Nationalism Triumphant Crash Course World History #40-T_sGTspaF4Y-144p-1654751102151 (online-video-cutter.com) (1).mp4")
# my_clip.audio.nchannels = 1
# my_clip.audio.write_audiofile(r"my_result.wav", fps=8000)



# # obtain path to "english.wav" in the same folder as this script
# from os import path
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "my_result.wav")

# # use the audio file as the audio source
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source)  # read the entire audio file
#     try:
#         print("Sphinx thinks you said " + r.recognize_sphinx(audio))
#     except sr.UnknownValueError:
#         print("Sphinx could not understand audio")
#     except sr.RequestError as e:
#         print("Sphinx error; {0}".format(e))
from google.cloud import speech
import io
client = speech.SpeechClient()

# path = 'resources/commercial_mono.wav'
with io.open("my_result.wav", "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    language_code="en-US",
    # Enable automatic punctuation
    enable_automatic_punctuation=True,
)

response = client.recognize(config=config, audio=audio)

print("Done")
print(response)
for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print("-" * 20)
    print("First alternative of result {}".format(i))
    print("Transcript: {}".format(alternative.transcript))