import youtube_dl

def download_video(video_url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Downloads the best video and audio quality
        'outtmpl': '%(title)s.%(ext)s',        # Saves the file with the video title
        'noplaylist': True,                     # Only download the single video
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
