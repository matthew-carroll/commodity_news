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
  source_material = get_all_news()
  print("Source material is " + str(len(source_material)) + " characters long")
  print("")

  prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", """
        You are a script writer for a podcast that focuses on the gold market, documenting major price movements and using market and economic data to explain the movements to investors. The goal is to help gold investors understand major price movements and overall gold market dynamics in the context of current events and trends. When there is a major movement, you will be provided with the start and end price over a given timeframe, and you must write an interesting, engaging, and thorough script that will be recorded by the podcast's host.\n
        \n
        The script can be formatted as a series of paragraphs without any titles, placeholders for music, etc. Editors will add these in a later step.\n
        """),
        ("system", """
        Below is your source material, gathered by our research team. Base your script primarily on specific events and facts mentioned in this material, while providing limited commentary based on your broader knowledge of the gold market.\n
        \n
        ### Source Material\n
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




