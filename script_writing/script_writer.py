import os
import json

from langchain_core.runnables.base import RunnableSequence
from langchain_core.runnables.passthrough import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from data_scraping import youtube_caption_scraper as captions

# Prints a podcast script to console based on a single-shot of context data + a single prompt.
async def write_one_shot_script(prompt):
  source_material = get_consolidated_notes()
  print("Source material is " + str(len(source_material)) + " characters long")
  print("")

  prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", """
        You are a script writer for Commodity News, a podcast that focuses on major gold price movements. The goal is
        to explain a given recent major movement based on facts in the attached source material. You are provided with 
        the start and end price over a given timeframe, and you must write an interesting, engaging, and thorough script 
        that will be recorded by the podcast's host.\n
        \n
        Your writing style is straightforward and confident, characterized by strong informed positions. You present
        information in a way that gives listeners confidence in your authority on the gold market, as well as in
        the thoroughness of your research process. Avoid passive and uncertain language like "may cause", "can lead to", 
        "would be", "possibly", etc., instead opting for active, assertive, and definitive language, e.g. "causes", "leads to", 
        "often is", etc. For example, instead of saying "interest rates can sometimes lead to price movements", say 
        "recent speculation about interest rates is undoubtedly shifting investor sentiment about gold". Be opinionated
        and definitive.
        \n
        The script can be formatted as a series of paragraphs without any titles, placeholders for music, etc. 
        Editors will add these in a later step.\n
        \n
        Below is your source material, gathered by our research team. Write a script that explains the given
        price movement using the specific events and facts mentioned in this material, while providing limited 
        commentary based on your knowledge of the general dynamics of the gold market. Share conclusions on
        why the price movement occurred and what it means for current and potential gold investors. Ignore any
        material that isn't relevant to the given gold price movement. Only cite information that is directly
        pertinent to the given gold price movement.\n
        \n
        ### Source Material\n
        \n
        {source_material}
        """),
        ("human", "{prompt}")
    ]
  )

  chat_model = ChatOpenAI(model="gpt-4o", temperature=1, api_key=os.environ["openai_api_key"])

  parser = StrOutputParser()

  runnable_chain = (
    {"source_material": RunnablePassthrough(), "prompt": RunnablePassthrough()} |
    prompt_template |
    chat_model |
    parser
  )

  output_stream = runnable_chain.astream({"source_material": source_material, "prompt": prompt})

  async for chunk in output_stream:
    print(chunk, sep='', end='', flush=True)

def get_all_news():
  files = captions.get_all_news_file_names("schiff")
  total_news = ""

  for file in files:
      file_path = os.path.join("data", file)
      with open(file_path, 'r') as f:
          print("Loading news from file: " + file)
          contents = f.read()

          snippets = json.loads(contents)
          total_news += " ".join(item['text'] for item in snippets)
      
      total_news += "\n\n"
  
  print("")
  return total_news[0:50000]

def get_all_notes():
  files = captions.get_all_news_file_names("notes")
  total_notes = ""

  for file in files:
      file_path = os.path.join("data", file)
      with open(file_path, 'r') as f:
          print("Loading news from file: " + file)
          notes = f.read()
          total_notes += notes + "\n\n-------------\n\n"
  
  return total_notes

def get_consolidated_notes():
    file_path = os.path.join("data", "consolidated_notes.txt")
    with open(file_path, 'r') as f:
        print("Loading consolidated notes")
        notes = f.read()
        return notes
