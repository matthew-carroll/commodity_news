import os
import dotenv
from elevenlabs import play
from elevenlabs import stream
from elevenlabs import save
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

dotenv.load_dotenv()

print("API key: " + os.getenv("ELEVENLABS_API_KEY"))
client = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
  timeout=600
)

with open("data/script.txt", "r") as f:
  script = f.read()

  # print("Generating audio...")
  # response = client.generate(
  #   text=script,
  #   voice="George",
  #   model="eleven_multilingual_v2",
  #   # stream=True
  # )

  # # print("Playing audio...")
  # # stream(audio)

  # print("Saving audio...")
  # save(audio, "data/speaking.mp3")

  # Calling the text_to_speech conversion API with detailed parameters
  response = client.text_to_speech.convert(
      voice_id="JBFqnCBsd6RMkjVDRZzb", # Adam pre-made voice
      optimize_streaming_latency="0",
      output_format="mp3_22050_32",
      text=script,
      model_id="eleven_multilingual_v2", # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
      voice_settings=VoiceSettings(
          stability=0.0,
          similarity_boost=1.0,
          style=0.0,
          use_speaker_boost=True,
      ),
  )

  # Writing the audio to a file
  print("Saving audio to file in chunks...")
  save_file_path = f"data/speaking.mp3"
  with open(save_file_path, "wb") as f:
      for chunk in response:
          if chunk:
              f.write(chunk)
  print(f"{save_file_path}: A new audio file was saved successfully!")

  print("Done!")