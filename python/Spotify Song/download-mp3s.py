from pathlib import Path
import yt_dlp as youtube_dl
import pandas
import os



def DownloadVideosFromTitles(los):
	ids = []
	for index, item in enumerate(los):
		vid_id = ScrapeVidId(item)
		ids += [vid_id]
	print("Downloading songs")
	DownloadVideosFromIds(ids)


def DownloadVideosFromIds(lov):
	SAVE_PATH = str(os.path.join(Path.home(), "Downloads/songs"))
	try:
		os.mkdir(SAVE_PATH)
	except:
		print("download folder exists")
	ydl_opts = {
		'format': 'bestaudio/best',
		'ffmpeg_location': 'C:/ffmpeg/bin',  # 👈 Add this line (use forward slashes `/`)
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
		'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(lov)

from youtubesearchpython import VideosSearch

def ScrapeVidId(query):
    print(f"Searching YouTube for: {query}")
    search = VideosSearch(query, limit=1)
    result = search.result()["result"]
    if result:
        return result[0]["id"]
    return None


def __main__():
    print("Checking if songs.csv exists...")
    if not os.path.exists('songs.csv'):
        print("Error: songs.csv not found. Run app.py first.")
        return

    print("Reading songs.csv...")
    data = pandas.read_csv('songs.csv')
    data = data['column'].tolist()

    print(f"Found {len(data)} songs!")

    if len(data) == 0:
        print("Error: songs.csv is empty!")
        return

    print("Starting download...")
    DownloadVideosFromTitles(data)

print("Running script...")
__main__()
print("Script finished.")
