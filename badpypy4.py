from pytube import Playlist
import os
import sys
import requests

def cleanme(zort):
    return zort.replace('"', '').replace("'", "").replace(":", "").replace("|", "").replace("#","").replace("?","").replace("*","").replace("<","").replace(">","").replace("/","").replace("\\","").replace("ł","l")

try:
    if len(sys.argv) > 1:
        playlist_url = sys.argv[1]
        playlist = Playlist(playlist_url)
        playlist_title_cleaned = cleanme(playlist.title)
        user_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        videodownloadpath = os.path.join(user_desktop, "music", "musics")
        thumbnails_path = os.path.join(user_desktop, "music", "thumbnails")

        os.makedirs(videodownloadpath, exist_ok=True)
        os.makedirs(thumbnails_path, exist_ok=True)

        print(f'Downloading playlist: {playlist_title_cleaned}')
        
        for video in playlist.videos:
            clean_title = cleanme(video.title)
            
            thumbnail_url = f'https://img.youtube.com/vi/{video.video_id}/maxresdefault.jpg'
            response = requests.get(thumbnail_url)
            thumbnail_image_file = os.path.join(thumbnails_path, f"{clean_title}_thumbnail.jpg")
            with open(thumbnail_image_file, 'wb') as file:
                file.write(response.content)

            audio_stream = video.streams.filter(only_audio=True).first()
            audio_stream.download(output_path=videodownloadpath, filename=f"{clean_title}.mp3")

        result = 'Download completed!'
        print(result)
    else:
        result = 'No input received'
        print(result)

except Exception as e:
    result = f"An error occurred: {str(e)}"
    print(result)
