from pytubefix import Playlist
import re
import sys

def check_url_case(url):
    """
    Check if a URL contains both uppercase and lowercase letters.
    Returns True if it contains both, False otherwise.
    """
    video_id = url.split("v=")[1].split("&")[0]  # Extract video ID
    
    has_lowercase = bool(re.search(r'[a-z]', video_id))
    has_uppercase = bool(re.search(r'[A-Z]', video_id))
    
    return has_lowercase and has_uppercase

def analyze_playlist(playlist_url):
    """
    Analyze all videos in a playlist and find those without both uppercase and lowercase.
    """
    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)
        
        print(f"Analyzing playlist: {playlist.title}")
        print(f"Found {len(playlist.video_urls)} videos in the playlist")
        print("-" * 50)
        
        matching_videos = []
        
        # Check each video in the playlist
        for index, url in enumerate(playlist.video_urls):
            try:
                has_both_cases = check_url_case(url)
                
                if not has_both_cases:
                    # Get video title
                    video_title = playlist.videos[index].title
                    matching_videos.append((video_title, url))
                    print(f"Found matching video: {video_title}")
            except Exception as e:
                print(f"Error processing video {url}: {str(e)}")
        
        # Print results
        print("\n" + "=" * 50)
        if matching_videos:
            print(f"Found {len(matching_videos)} videos without both uppercase and lowercase letters:")
            for idx, (title, url) in enumerate(matching_videos, 1):
                print(f"{idx}. {title}")
                print(f"   URL: {url}")
        else:
            print("No videos found without both uppercase and lowercase letters.")
            
        return matching_videos
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Get playlist URL from command line argument
        playlist_url = sys.argv[1]
    else:
        # Get playlist URL from user input
        playlist_url = input("Enter YouTube playlist URL: ")
    
    analyze_playlist(playlist_url)