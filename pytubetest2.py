import os
from pytube import YouTube
video_url = input("Enter a YouTube video URL: ")
try:
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    user_desktop = os.path.join(os.path.expanduser("~"), "Desktop")    
    audio_stream.download(output_path=user_desktop, filename=f"{yt.title}.mp3")
    print("Audio downloaded successfully!")
except Exception as e:
    print(f"An error occurred: {str(e)}")
