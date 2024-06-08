import dotenv
import os
from datetime import datetime, timedelta

from data_scraping import data_sources as data
from data_scraping import youtube_channel_scraper as youtube
from data_scraping import youtube_caption_scraper as captions

dotenv.load_dotenv()

start_time = (datetime.now() - timedelta(weeks=2)).strftime('%Y-%m-%d')
print("Start time: " + start_time)

latest_videos_per_channel = youtube.get_latest_videos_for_channels(os.getenv("GOOGLE_API_KEY"), data.channel_ids, start_time)

# Download transcripts for the given channels and videos to local files.
captions.download_youtube_transcripts(latest_videos_per_channel)
