import asyncio
import json
import os

from script_writing import note_taker
from data_scraping import youtube_caption_scraper as captions

transcripts = """
Title: "Gold Rush: The Unthinkable Collapse"

Introduction:

[Upbeat intro music plays]

Host 1 (Jane): Welcome back, listeners, to "Gold Rush: The Unthinkable Collapse," where we dive into the most bizarre and unexpected financial scenarios. I'm Jane Richards.

Host 2 (Tom): And I'm Tom Harris. Today, we're exploring a wild hypothetical: What if gold prices were to fall significantly? Hold onto your seats because this is going to be a rollercoaster of a scenario!

Jane: Gold has long been considered a safe haven in times of economic uncertainty. But what could possibly cause this precious metal's value to plummet? Let's jump into our story.

[Transition music]

Scenario: "The Tech Treasure Trove"

Tom: Picture this: It's the year 2025. The world is buzzing with technological advancements, and a groundbreaking discovery is about to shake the financial world to its core.

Jane: A team of scientists working on a deep-sea exploration project in the Pacific Ocean stumbles upon an enormous underwater mountain range filled with vast deposits of a new, highly conductive material they call "Techium."

Tom: Techium is quickly found to be superior to gold in every aspect—conductivity, durability, and even cost-effectiveness. The tech industry, always hungry for better materials, starts adopting Techium for everything from smartphones to spacecraft.

Jane: Investors panic. As news spreads about Techium's discovery and its potential to replace gold in electronics, the demand for gold plummets. People start offloading their gold investments, fearing they’ll be left with a relic of the past.

Tom: Central banks, sensing the shift, begin diversifying their reserves away from gold. This adds to the selling pressure, and gold prices start to tumble.

[Sound effect: coins clinking]

Jane: Meanwhile, a series of high-profile thefts of gold artifacts from museums around the world adds to the chaos. The stolen gold floods the market, increasing supply and driving prices even lower.

Tom: On top of that, a new global environmental regulation restricts gold mining to protect endangered ecosystems, further reducing gold's appeal as a safe investment.

Jane: With gold prices in freefall, traditional gold mining companies pivot to Techium extraction, contributing to the new metal's rapid rise in prominence.

[Sound effect: underwater drilling]

Tom: Governments and financial institutions around the world begin to adopt Techium as part of their official reserves, marking a significant shift in global economic policies.

Jane: In this brave new world, gold is no longer the king of metals. Instead, it's Techium that commands respect and holds value, fundamentally altering the financial landscape.

Tom: This scenario, while highly speculative, illustrates how a single discovery and a series of cascading events could lead to an unprecedented collapse in gold prices.

[Transition music]

Conclusion:

Jane: So there you have it, folks. A wild ride through a hypothetical scenario where gold's reign as the ultimate safe-haven asset comes to an end. Remember, while this is just a fictional tale, it shows how interconnected and unpredictable our world can be.

Tom: Thanks for joining us on "Gold Rush: The Unthinkable Collapse." If you enjoyed this episode, don't forget to subscribe and leave us a review. Until next time, stay curious and keep imagining the unthinkable!

[Outro music fades out]


[Intro Music]

Host: Welcome to "Science Today," the podcast that brings you the latest discoveries and breakthroughs in the world of science. I'm your host, [Host's Name], and today, we're diving into an extraordinary discovery that has the potential to revolutionize technology and industry: the recent finding of Unobtainium in Zimbabwe.

[Music fades out]

Host: For years, Unobtainium has been the stuff of legends in scientific circles—a hypothetical material with incredible properties, often featured in science fiction. But now, what was once thought to be purely fictional has become a reality. Let's explore this groundbreaking discovery and what it could mean for our future.

Host: The discovery was made by a team of geologists and mineralogists from the University of Zimbabwe, working in collaboration with international researchers. Located in the Zambezi Valley, this region has long been known for its rich deposits of various minerals, but nothing quite like Unobtainium has ever been found—until now.

Guest 1: [Dr. Sarah Nyathi, Lead Geologist, University of Zimbabwe] "When we first identified the unusual properties of the mineral samples, we were both excited and skeptical. It took months of rigorous testing and analysis to confirm that what we had was indeed Unobtainium."

Host: So, what exactly is Unobtainium, and why is it such a big deal? Unobtainium is believed to possess extraordinary characteristics, including unparalleled conductivity, immense strength, and extreme resistance to heat and radiation. These properties make it incredibly valuable for a range of applications, from aerospace engineering to advanced electronics and even medical devices.

Guest 2: [Dr. John Taylor, Materials Scientist] "The potential applications of Unobtainium are vast. For example, its conductivity could revolutionize the way we build circuits and batteries, leading to more efficient and durable electronic devices. In aerospace, its strength and light weight could lead to the development of more advanced spacecraft and aircraft."

Host: The implications of this discovery are immense. Imagine smartphones with batteries that last for weeks, supercomputers with unprecedented processing power, and space missions that can travel farther and faster than ever before. Unobtainium could truly change the game.

[Soundbite from a news report]

Reporter: "The discovery of Unobtainium in Zimbabwe has sparked a flurry of excitement in the scientific community. Experts are calling it one of the most significant mineral finds of the century."

Host: However, with such potential also comes challenges. Extracting and refining Unobtainium is no simple task. The processes required are complex and expensive, and there are also environmental and ethical considerations to take into account.

Guest 3: [Dr. Emily Carter, Environmental Scientist] "We need to ensure that the extraction of Unobtainium is done sustainably and ethically. This means developing methods that minimize environmental impact and ensuring that local communities benefit from the resources found in their regions."

Host: In addition to the technical challenges, there's also the question of geopolitics. Zimbabwe's government and international stakeholders will need to navigate the economic and political landscape carefully to ensure that the benefits of this discovery are shared equitably.

Host: Despite these challenges, the discovery of Unobtainium represents a monumental step forward. It reminds us of the boundless potential of science and the endless mysteries that our planet still holds. Who knows what other incredible discoveries await us just beneath the surface?

[Outro Music begins]

Host: That's all for today's episode of "Science Today." We hope you enjoyed this deep dive into the world of Unobtainium. Be sure to subscribe and tune in next week for more exciting updates from the world of science. I'm your host, [Host's Name], signing off. Stay curious!

[Outro Music fades out]

[End of transcript]
"""

def take_all_notes():
  prefixes = [
    "schiff",
    "bullion_news",
    "kitco",
    "stansberry",
  ]

  for prefix in prefixes:
    files = captions.get_all_news_file_names(prefix)
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

      notes_path = os.path.join("data", f"notes_{prefix}.txt")
      with open(notes_path, 'w') as f:
        f.write(total_notes)

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

consolidate_all_notes()