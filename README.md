# Commodity News
AI generated news about commodity prices.

## Setup Requirements
The project expects a `.env` file at the root of the repo that contains various keys.

```
GOOGLE_API_KEY=''
```

## System Overview

### Data source: YouTube transcripts
The system currently uses transcripts from popular YouTube channels that cover the gold market. At the moment, we have a hardcoded set of videos that we're pulling transcripts from, but the long term plan is to query these transcripts dynamically based on the date of the most recent major gold price movement.

### Stage 1: Processing source material
The note taker module processes each transcript into a structured summary, citing specific events and facts that are relevant to the recent gold price movement and justifying its reason for including that fact.

### Stage 2: Source material consolidation
The consolidator module iterates through notes for each episode, creating a single document with redundant information consolidated and irrelevant facts discarded.

### Stage 3: Script writing
The script writer module uses the resulting source material, as well as a dynamically provided gold price movement, to write an engaging script explaining the reasons for the price movement and what it means for gold investors.

### Stage 4: Recording
The resulting script is handed off to the ElevenLabs API to be turned into a realistic voice recording of the episode. This is currently done manually using the web interface.

### Stage 5: Video Editing
The resulting audio recording is programmatically combined with other media to create a final video for upload to a YouTube channel. This is not yet implemented.

## Learnings and Challenges

### Managing source material
The main challenge we've faced is turning raw source material into structured and concise information that can be effectively used to create a compelling, detailed, and accurate script. Using all of the transcripts directly leads to the context window being exceeded, as well as the context being polluted by a large amount of irrelevant information. We considered a vector store with relevancy search but opted for an LLM note taker instead to help ensure the resulting information was highly structured and relevant.

### Creating a detailed, accurate script
We initially ran into issues where the system would produce scripts that were too broad and abstract, talking about high level, general economic topics instead of specific facts that are relevant to the given gold price movement. We reworked the note taker and consolidator prompts to preserve key facts and events in the final notes, then modified the script writer prompt to focus primarily on these facts rather than general commentary. We saw a major improvement in the specificity and detail of the resulting scripts.

## APIs

### Gold Price APIs
We use two APIs for gold prices. They're interchangeable. We use two so that we get twice the request count.

https://metalpriceapi.com/documentation

https://www.goldapi.io/

Both services require API keys for access. The API keys are free.

Store the API keys in environment variables with the following names:

 * METALPRICE_API_KEY
 * GOLDAPIIO_API_KEY

