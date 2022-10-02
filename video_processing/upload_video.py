import moviepy.editor as mp
from google.cloud import storage
import json
import re
from random import randint, randrange
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./ke-file.json"

my_clip = mp.VideoFileClip(r"Nukes.mp4")
my_clip.audio.write_audiofile(r"my_result.wav")

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )
    link = blob.path_helper(bucket_name, destination_blob_name)
    return "gs://" + re.sub('/o/', '/', link)

rando_name = randint(10000, 99999)

file_uri = upload_blob("audio-samples-hack-mit", "my_result.wav", str(rando_name))

json_object = json.dumps({'file_uri':file_uri}, indent=4)
with open("audio_uri.json", "w") as outfile:
    outfile.write(json_object)