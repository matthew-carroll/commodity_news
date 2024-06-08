import asyncio
import json
import os

from script_writing import note_taker
from data_scraping import youtube_caption_scraper as captions
from data_scraping import youtube_channel_scraper as youtube
from data_scraping import data_sources as data

def take_all_notes(channel_ids):
  for channel_name in channel_ids:
    channel_id = channel_ids[channel_name]
    files = captions.get_all_news_file_names(channel_id)
    total_notes = ""

    for file in files:
      file_path = os.path.join("data", file)
      with open(file_path, 'r') as f:
        print("Loading news from file: " + file)
        contents = f.read()

        snippets = json.loads(contents)
        text_content = " ".join(item['text'] for item in snippets)

        notes = note_taker.take_notes(text_content)

        print("\nCOMPLETED NOTES\n")
        print(notes)

        total_notes += notes + "\n\n------------------\n\n"

      notes_path = os.path.join("data", f"notes_{channel_id}.txt")
      with open(notes_path, 'w') as f:
        f.write(total_notes)

if __name__ == "__main__":
  take_all_notes(data.channel_ids)