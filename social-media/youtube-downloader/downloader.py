import yt_dlp

"""
Python Automation Hub - YouTube Downloader
A tool to download single videos and playlists with real-time progress.
"""

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\r⬇ Downloading: {percent} | Speed: {speed} | ETA: {eta}", end="", flush=True)
    elif d['status'] == 'finished':
        print(f"\n✅ Done: {d['filename']}")

ydl_opts = {
    'noplaylist': False,
    'progress_hooks': [progress_hook],
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s.%(ext)s',
}

def download(urls):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            print(f"\n🎵 Starting: {url}")
            try:
                ydl.download([url])
            except Exception as e:
                print(f"❌ Failed: {url} — {e}")

if __name__ == "__main__":
    print("🎶 YouTube Downloader — Enter URLs (one per line). Empty line to start:")
    urls = []
    while True:
        url = input("> ").strip()
        if not url:
            break
        urls.append(url)
    if urls:
        download(urls)
    else:
        print("No URLs provided.")