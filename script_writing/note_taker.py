from langchain_core.runnables.base import RunnableSequence
from langchain_core.runnables.passthrough import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

def take_notes(transcript):
  prompt_template = PromptTemplate(
      template="""
        You are a researcher for a news program about the gold market. Your job is to read through the attached transcript
        from a podcast we're using as source material, then extract and summarize all information that is relevant to the gold 
        market. Your summaries will be used by the script writing team to write the final podcast script, so include any 
        information that would be helpful for that purpose.
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
        Below is a list of summaries written based on series of podcast transcripts. Each summary contains information
        that is relevant to the gold market and gold prices. Take these summaries and consolidate them into a new list
        of facts, points, and other key information, focusing on information that is relevant to the gold market. This
        will be used by the writing team of a news program as source material to write an in depth news program on the
        current state of the gold market, so tailor your summary for that purpose. Your summary will be provided to
        that team directly, so please limit your response only to the information relevant to that purpose.
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