import os
from time import sleep
from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path
import json

# Downloads transcripts for videos, on a per-channel basis, to local files.
#
# The transcripts are saved to the "data" directory.
#
# The "channels" argument is a dictionary where the keys self-chosen channel names and the values are lists of video IDs.
#
# For example:
#
# {
#   "schiff" : [
#     "vRP58NX0osw",
#   ],
#   "bullion_news" : [
#     "xDWkeHRUHoc",
#   ]
# }
def download_youtube_transcripts(channels):
  # Ensure that the local data directory exists.
  news_directory_path.mkdir(parents=True, exist_ok=True)

  for channel_name in channels:
    channel_video_ids = channels[channel_name]

    for video_id in channel_video_ids:
      print("Downloading transcripts for channel " + channel_name + " and video " + video_id)
      download_youtube_transcript_to_file(video_id, f"{news_directory_path}/{channel_name}_{video_id}.txt")
      sleep(1)

def download_youtube_transcript_to_file(video_id, file_path):
  try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    with open(file_path, 'w') as file:
      json.dump(transcript, file, indent=2)
  except:
    print("FAILED to download transcript for video: " + video_id)

def dump_all_downloaded_transcripts_to_console():
  files = get_all_news_file_names()

  for file in files:
      file_path = os.path.join(news_directory_path, file)
      with open(file_path, 'r') as f:
          contents = f.read()
          snippets = json.loads(contents)
          transcript = " ".join(item['text'] for item in snippets)

          print(f"Contents of {file}:")
          print(transcript)
          print("\n" + "-"*40 + "\n")

# Returns all the news transcript file names that begin with the given "prefix".
#
# For example, all news whose file names begin with "kitco_".
def get_all_news_file_names(prefix=""):
  return [f for f in os.listdir(news_directory_path) if os.path.isfile(os.path.join(news_directory_path, f)) and f.startswith(prefix) and f.endswith('.txt')]

news_directory_path = Path("./data")
