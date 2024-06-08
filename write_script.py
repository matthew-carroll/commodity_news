from script_writing import script_writer as writer
import asyncio

with open("data/script.txt", "w") as destination:
  asyncio.run(
    writer.write_one_shot_script(
      """Date: May 24, 2024
  Gold Price: $2342

  Date: June 7, 2024
  Gold Price: $2287""",
      destination
    )
  )
