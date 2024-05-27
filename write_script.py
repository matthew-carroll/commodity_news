from script_writing import script_writer as writer
import asyncio

asyncio.run(
  writer.write_one_shot_script(
    """Date: May 21, 2024
Gold Price: $2449

Date: May 23, 2024
Gold Price: $2359"""
  )
)
