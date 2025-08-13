# YouTube Playlist to MP3 Downloader

## Use Case

Finding good quality MP3 downloads for music can be challenging, especially for offline listening. This script solves that problem by allowing you to download your favorite YouTube playlists directly as MP3 files.

Perfect for:
- **Car Travel**: Keep downloaded playlists in your car for offline listening during long drives
- **Offline Listening**: No internet connection needed once downloaded
- **Personal Music Library**: Build your own MP3 collection from YouTube playlists

## How It Works

This script downloads all videos from YouTube playlists and converts them to MP3 format, making them perfect for offline listening in your car or anywhere else.

## Setup

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
   - Example: `https://www.youtube.com/playlist?list=PL7A9n1TybRSkWE9pgw04QRRH2hKuD3YIy`

3. **Run the Script**:
   ```bash
   python download_to_mp3.py
   ```

## Features

- ✅ Downloads entire playlists automatically
- ✅ Converts to high-quality MP3 format
- ✅ Organizes files in `output/` directory
- ✅ Fresh downloads (no duplicates)
- ✅ Perfect for car audio systems

## Output

All downloaded MP3 files will be saved in the `output/` directory, ready to transfer to your car's USB drive or music player.

## Note

This tool is for personal use only. Please respect copyright laws and only download content you have permission to use.
