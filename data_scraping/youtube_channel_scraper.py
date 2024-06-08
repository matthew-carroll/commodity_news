from googleapiclient.discovery import build
import dotenv
import datetime

# channel_ids should be a map from a human-readable channel name to a channel ID.
#
# {
#   "schiff": "...",
#   "2is1": "...",
# }
#
# Returns a map from channel IDs to a list of video IDs:
#
# {
#  "klh345lk34": [...],
#  "72nv3n734f": [...],
# }
def get_latest_videos_for_channels(api_key, channel_ids, start_date, end_date=None):
    latest_videos = {}

    for channel_name in channel_ids:
      channel_id = channel_ids[channel_name]
      videos = get_latest_videos_for_channel(api_key, channel_id, start_date, end_date)
      latest_videos[channel_id] = videos
    
    return latest_videos


def get_latest_videos_for_channel(api_key, channel_id, start_date, end_date):
    youtube = build('youtube', 'v3', developerKey=api_key)

    print("Channel ID: " + channel_id)

    # Convert dates to RFC 3339 format
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').isoformat() + 'Z'
    print("Start date sent to youtube: " + start_date)

    if (end_date != None):
      end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').isoformat() + 'Z'

    video_ids = []

    request = youtube.search().list(
        part='id',
        channelId=channel_id,
        publishedAfter=start_date,
        publishedBefore=end_date,
        maxResults=10
    )
    response = request.execute()

    for item in response.get('items', []):
        if item['id']['kind'] == 'youtube#video':
            video_ids.append(item['id']['videoId'])

    return video_ids

if __name__ == "__main__":
    dotenv.load_dotenv()

    channel_id = "UCOqoxEetp1w7AUVPI9zuWqw"

    # Example date range
    start_date = '2024-04-01'
    # end_date = '2024-06-08'
    end_date = None

    video_ids = get_latest_videos_for_channel(os.getenv("GOOGLE_API_KEY"), channel_id, start_date, end_date)
    print("Video IDs between {} and {}:".format(start_date, end_date))
    for video_id in video_ids:
        print(video_id)
