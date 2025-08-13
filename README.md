# YouTube Playlist to MP3 Downloader 🎵

> **Just built something that solves a real problem I've been facing!**

## The Challenge

Finding good quality MP3 downloads for offline listening is surprisingly difficult, especially when you want to enjoy your favorite YouTube playlists during long car rides or when you're offline.

## The Solution

I created a Python-based YouTube playlist to MP3 downloader that automatically:
- Downloads entire playlists from YouTube
- Converts them to high-quality MP3 format
- Embeds metadata and thumbnails
- Organizes files perfectly for offline use

## Perfect Use Cases

- **Car Travel**: Keep downloaded playlists in your car for offline listening during long drives
- **Gym Sessions**: No internet connection needed once downloaded
- **Personal Music Library**: Build your own MP3 collection from YouTube playlists
- **Offline Listening**: Anywhere you want your favorite music without relying on internet connectivity

## Key Features

✅ **Supports Multiple Formats**: Regular playlists, mix playlists, and single videos  
✅ **Automatic Numbering**: Files are numbered in playlist order  
✅ **Large Playlist Support**: Handles playlists efficiently  
✅ **Car Audio Ready**: Perfect for car audio systems  
✅ **Offline Ready**: No internet needed once downloaded  
✅ **High Quality**: MP3 conversion with metadata and thumbnails  

## Tech Stack

- **Python** - Core scripting language
- **yt-dlp** - YouTube downloader library
- **FFmpeg** - Audio processing and conversion
- **Git** - Version control

## Quick Start

### Prerequisites

This script requires the following tools to be installed on your system:

1. **yt-dlp**: YouTube downloader (Python package)
2. **ffmpeg**: Audio/video processing tool (system dependency)

### Installation

1. **Install Python Dependencies**:
   ```bash
   pip install yt-dlp
   ```

2. **Install System Dependencies**:

   **On macOS (using Homebrew)**:
   ```bash
   brew install ffmpeg
   ```

   **On Ubuntu/Debian**:
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

   **On Windows**:
   - Download ffmpeg from https://ffmpeg.org/download.html
   - Add it to your system PATH

3. **Configure Playlists**:
   - Open `urls.txt`
   - Add your YouTube playlist URLs (one per line)
   - Example: `https://www.youtube.com/playlist?list=PL4an4gce7LuPswK2mtocj8j55DKHra_QA`

4. **Run the Script**:
   ```bash
   python download_to_mp3.py
   ```

## How It Works

This script intelligently detects different types of YouTube URLs:
- **Regular Playlists**: Downloads all items in playlist order
- **Mix Playlists**: Limits to first 50 songs (YouTube Mix can be infinite)
- **Single Videos**: Downloads individual videos

All downloaded MP3 files will be saved in the `output/` directory, ready to transfer to your car's USB drive or music player.


## Note

This tool is for personal use only. Please respect copyright laws and only download content you have permission to use.

---

**🔗 Check it out**: https://github.com/naveen-krishna/youtube-mp3-downloader

*What's your go-to solution for offline music? Would love to hear your thoughts! 🎵*
