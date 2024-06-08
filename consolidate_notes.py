import os

from script_writing import note_taker
from data_scraping import youtube_caption_scraper as captions

def consolidate_all_notes():
  files = captions.get_all_news_file_names("notes")
  total_notes = ""

  for file in files:
    file_path = os.path.join("data", file)
    with open(file_path, 'r') as f:
      print("Loading notes from file: " + file)
      notes = f.read()
      consolidate_notes = note_taker.consolidate_notes(notes)
      print(consolidate_notes)

      total_notes += note_taker.consolidate_notes(notes) + "\n\n"
  
  print("\n")
  print("NOTES CONSOLIDATED")
  print(total_notes)
  print("\n")

  notes_path = os.path.join("data", f"consolidated_notes.txt")
  with open(notes_path, 'w') as f:
    f.write(total_notes)

if __name__ == "__main__":
  consolidate_all_notes()