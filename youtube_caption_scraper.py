from time import sleep
from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path
import json

channels = {
  "schiff" : [
    "vRP58NX0osw",
    "ps33POXMH_I",
    "q8KnZcwg11g",
    "aLdLQM4NLy8",
    "oRQwlM5JRrs",
    "5w5Wpob16EA",
    "h8C2eRSs2ck",
    "pI0fLZJr_QU",
    "dkfBPYLuGQg",
    "VQWqpAkvVWY",
  ],

  "kitco" : [
    "tz8NuSypNpc",
    "DD1CnjI2Z3k",
    "K7bhSS53GXE",
    "zgR2ci7v7Uk",
    "INeRRH0kAX8",
    "LvovlDVpyLI",
    "X5MB3WTtPk0",
    "e5RhVKdAibo",
    "3t2QEpDXRBE",
  ],

  "stansberry" : [
    "b14xw9RWvKg",
    "RBGz_SXrGY4",
    "IZAjY7VjVOk",
    "39HUeC7jC7E",
    "NIPUgriMhyI",
  ],

  "bullion_news" : [
    "xDWkeHRUHoc",
    "Sl5M8gpwZdY",
    "SDgXTl-FWz8",
    "UQ15XxbgIF0",
    "9W1yLtlwrfQ",
    "b2WoUABVrhs",
    "FQRv-kNzxh8",
    "3BsvY5DSmf8",
    "lMmxwHqL9FI",
    "KSeenv8lDP0",
    "_l7PGWmmWsg",
  ]
}

# for channel_name in channels:
#   channel = channels[channel_name]

#   for video in channel:
#     transcript = YouTubeTranscriptApi.get_transcript(video)
#     path = "./data"
#     Path(path).mkdir(parents=True, exist_ok=True)
#     with open(f"{path}/{channel_name}_{video}.txt", 'w') as file:
#       json.dump(transcript, file, indent=2)
#     sleep(1)

import os

directory = 'data'
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.txt')]

for file in files:
    file_path = os.path.join(directory, file)
    with open(file_path, 'r') as f:
        contents = f.read()

        snippets = json.loads(contents)
        transcript = " ".join(item['text'] for item in snippets)
        print(f"Contents of {file}:")
        print(transcript)
        print("\n" + "-"*40 + "\n")
