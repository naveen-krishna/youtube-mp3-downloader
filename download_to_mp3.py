#!/usr/bin/env python3
"""
Batch-download audio from a list of URLs and convert to MP3.
- Supports playlists: each playlist gets its own folder
- Mix playlists are automatically limited to first 50 items
- Regular playlists download all items
ONLY use for content you have rights to download (public-domain / CC / your own).
"""

import subprocess
import sys
import json
import re
from pathlib import Path

# Config
URLS_FILE = Path("urls.txt")     # one URL per line
OUTPUT_BASE_DIR = Path("output") # root folder for downloads
YTDLP_CMD = "yt-dlp"
FFMPEG_PATH = "ffmpeg"

BASE_OPTIONS = [
    "--extract-audio",
    "--audio-format", "mp3",
    "--audio-quality", "0",
    "--embed-thumbnail",
    "--add-metadata",
    "--no-mtime",
    "--retries", "5",
    "--fragment-retries", "5",
    "--continue",
    "--no-playlist-reverse",  # Preserve original playlist order
]

def check_prereqs():
    from shutil import which
    missing = []
    if not which(YTDLP_CMD):
        missing.append(YTDLP_CMD)
    if not which(FFMPEG_PATH):
        missing.append(FFMPEG_PATH)
    if missing:
        print("ERROR: Missing executables:", ", ".join(missing))
        sys.exit(2)

def read_urls():
    if not URLS_FILE.exists():
        print(f"ERROR: {URLS_FILE} not found.")
        sys.exit(1)
    with URLS_FILE.open("r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip() and not ln.startswith("#")]
    if not lines:
        print("ERROR: No valid URLs found.")
        sys.exit(1)
    return lines

def get_playlist_info(url):
    """Fetch playlist title and count."""
    try:
        result = subprocess.run(
            [YTDLP_CMD, "--dump-single-json", "--flat-playlist", url],
            capture_output=True, text=True, check=True
        )
        data = json.loads(result.stdout)
        
        title = data.get("title", "Unknown_Playlist")
        # Count entries in the playlist
        entries = data.get("entries", [])
        count = len(entries) if entries else 0
        
        return title, count
    except Exception as e:
        print(f"Could not fetch playlist info for {url}: {e}")
        return "Unknown_Playlist", 0

def is_mix_playlist(url):
    """Detect if this is a YouTube Mix playlist."""
    # YouTube Mix playlists have list=RD followed by a long string
    mix_pattern = r'list=RD[A-Z0-9_-]+'
    return bool(re.search(mix_pattern, url)) or "list=RD" in url

def is_regular_playlist(url):
    """Detect if this is a regular YouTube playlist."""
    # Regular playlists have list=PL followed by alphanumeric characters
    playlist_pattern = r'list=PL[A-Z0-9_-]+'
    return bool(re.search(playlist_pattern, url)) or "playlist?list=PL" in url

def is_single_video(url):
    """Detect if this is a single video URL."""
    # Single video URLs have watch?v= but no list parameter
    return "watch?v=" in url and "list=" not in url

def download(urls):
    for url in urls:
        print(f"\nChecking: {url}")
        
        if is_mix_playlist(url):
            # Handle YouTube Mix playlists
            playlist_name, count = get_playlist_info(url)
            safe_name = "".join(c if c.isalnum() or c in " -_" else "_" for c in playlist_name)
            output_dir = OUTPUT_BASE_DIR / safe_name
            output_dir.mkdir(parents=True, exist_ok=True)
            output_template = str(output_dir / "%(autonumber)02d - %(title)s.%(ext)s")
            
            print(f"Detected YouTube Mix playlist: {playlist_name}")
            print(f"Mix playlists can be infinite, limiting to first 50 songs")
            print(f"Note: Mix playlist order may vary from YouTube display order")
            
            cmd = [YTDLP_CMD] + BASE_OPTIONS + [
                "--output", output_template, 
                url, 
                "--yes-playlist",
                "--playlist-start", "1", 
                "--playlist-end", "50",
                "--autonumber-start", "1"
            ]

        elif is_regular_playlist(url):
            # Handle regular YouTube playlists
            playlist_name, count = get_playlist_info(url)
            safe_name = "".join(c if c.isalnum() or c in " -_" else "_" for c in playlist_name)
            output_dir = OUTPUT_BASE_DIR / safe_name
            output_dir.mkdir(parents=True, exist_ok=True)
            output_template = str(output_dir / "%(autonumber)02d - %(title)s.%(ext)s")
            
            print(f"Detected regular playlist: {playlist_name}")
            print(f"Playlist contains {count} items")
            print(f"Files will be numbered in playlist order")
            
            cmd = [YTDLP_CMD] + BASE_OPTIONS + [
                "--output", output_template, 
                url, 
                "--yes-playlist",
                "--autonumber-start", "1"
            ]

        elif is_single_video(url):
            # Handle single video URLs
            output_dir = OUTPUT_BASE_DIR
            output_dir.mkdir(parents=True, exist_ok=True)
            output_template = str(output_dir / "%(title)s.%(ext)s")
            
            print("Detected single video")
            
            cmd = [YTDLP_CMD] + BASE_OPTIONS + [
                "--output", output_template, 
                url, 
                "--no-playlist"
            ]

        else:
            # Fallback for unknown URL types
            print("Unknown URL type, treating as single video")
            output_dir = OUTPUT_BASE_DIR
            output_dir.mkdir(parents=True, exist_ok=True)
            output_template = str(output_dir / "%(title)s.%(ext)s")
            
            cmd = [YTDLP_CMD] + BASE_OPTIONS + [
                "--output", output_template, 
                url, 
                "--no-playlist"
            ]

        print(">>> Running:", " ".join(cmd))
        try:
            subprocess.check_call(cmd)
        except subprocess.CalledProcessError as e:
            print(f"Download failed for {url} (exit {e.returncode})")

def main():
    check_prereqs()
    urls = read_urls()
    download(urls)
    print("\nAll done. MP3 files saved in:", OUTPUT_BASE_DIR.resolve())

if __name__ == "__main__":
    main()
