import os
import requests
import sys
from pytube import YouTube

def cleanme(zort):
    return zort.replace('"', '').replace("'", "").replace(":", "").replace("|", "").replace("#","").replace("*","").replace("<","").replace(">","").replace("/","").replace("\\","").replace("ł","l").replace("?","¿")

try: # make it input
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    
        yt = YouTube(video_url)
        clean_title = cleanme(yt.title)

        user_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        videodownloadpath = os.path.join(user_desktop, "music", "musics")
        thumbnail_image_file = os.path.join(user_desktop, "music", "thumbnails", f"{clean_title}_thumbnail.jpg")
        
        specific_thumbnail_url = f'https://img.youtube.com/vi/{yt.video_id}/maxresdefault.jpg' # add other resolutions here

        response = requests.get(specific_thumbnail_url)
        with open(thumbnail_image_file, 'wb') as file:
            file.write(response.content)
        
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path=videodownloadpath, filename=f"{clean_title}.mp3")

        result = f"Downloaded {clean_title} successfully!"
        print(result)
    else:
        result = 'No input received'
        print(result)

except Exception as e:
    if len(sys.argv) > 1:
        result = f"An error occurred: {str(e)}."
        print(result)
    else:
        result = 'No input received'
        print(result)
