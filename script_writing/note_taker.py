from langchain_core.runnables.base import RunnableSequence
from langchain_core.runnables.passthrough import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

def take_notes(transcript):
  prompt_template = PromptTemplate(
      template="""
        Below is a transcript from a popular financial podcast. Your job is to extract concrete facts and events that 
        are relevant to the gold market. These will be used as source material for a news program discussing current 
        events that are influencing gold prices, targeting gold investors. Choose facts and events that are relevant 
        to this purpose and audience, and be detailed enough that the script writing team will have enough material 
        to work from (e.g. include dates, locations, numbers, and specifics over abstract commentary). Below each 
        item, include your reasoning for including it. Your output will be provided directly to the script writing
        team, so only include text that is relevant for that purpose.
        \n
        ### Source Material Transcript\n
        {transcript}
        """,
        input_variables=["transcript"]
  )

  chat_model = ChatOpenAI(model="gpt-4o", temperature=0.7, api_key=os.environ["openai_api_key"])

  parser = StrOutputParser()

  runnable_chain = (
    {"transcript": RunnablePassthrough()} |
    prompt_template |
    chat_model |
    parser
  )

  return runnable_chain.invoke(transcript)

def consolidate_notes(notes):
  prompt_template = PromptTemplate(
      template="""
        Below is a list of key facts and events extracted from a series of financial podcast transcripts. Each contains
        information that is relevant to the gold market and gold prices. Take these facts and consolidate them, 
        combining facts/events that are mentioned multiple times and removing anything that isn't meaningfully relevant 
        to gold prices. This will be used by the writing team of a news program as source material to write an in depth
        news segment on recent major moves in gold prices, so tailor your summary for that purpose. Your output
        be provided to that team directly, so please limit your response to information relevant to that purpose.
        \n
        ### Source Material Summaries\n
        {notes}
        """,
        input_variables=["notes"]
  )

  chat_model = ChatOpenAI(model="gpt-4o", temperature=0.7, api_key=os.environ["openai_api_key"])

  parser = StrOutputParser()

  runnable_chain = (
    {"notes": RunnablePassthrough()} |
    prompt_template |
    chat_model |
    parser
  )

  return runnable_chain.invoke(notes)