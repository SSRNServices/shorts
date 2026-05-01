# 🎬 Shorts - Video Processing Toolkit

<div align="center">
  A powerful Python utility and Telegram Bot to effortlessly split and trim videos using FFmpeg.
</div>

---

## 🌟 Features

- **✂️ Split Videos**: Cut long videos into smaller segments of equal duration. Includes options for padding, colors, and adding "Part-XX" labels.
- **🕒 Trim Start**: Remove a specific number of seconds from the beginning of a video without re-encoding, making it blazingly fast.
- **🤖 Telegram Bot**: Process videos directly from Telegram by sending them with commands!
- **🐳 Docker Support**: Easily deploy the Telegram bot using the provided Dockerfile.

## 🛠️ Requirements

- **Python 3.11+**
- **FFmpeg & FFprobe** installed and available in your system's `PATH`.

---

## 🖥️ CLI Usage

### 1. Split Video (`split.py`)
Splits a video into smaller segments, adds padding, and overlays a text label.

```bash
python3 split.py
```
**Interactive Prompts:**
1. Full path to the video file.
2. Segment duration in seconds.
3. TOP and BOTTOM padding height in pixels.
4. Padding color in HEX format (e.g., `#000000`).
5. Font selection for the "Part-XX" text.

**Output:** Creates a folder `<video_name>_parts` containing the segmented files.

### 2. Trim Start of Video (`trim_start.py`)
Removes a specified number of seconds from the beginning of a video.

```bash
python3 trim_start.py
```
**Interactive Prompts:**
1. Full path to the video file.
2. Number of seconds to remove from the start.

**Output:** Creates a new file `<video_name>_trimmed<extension>`.

---

## 🤖 Telegram Bot Usage

You can deploy the Telegram bot to process videos remotely.

### Commands

- Send a video with the caption `/trim <seconds>` to remove the first X seconds.
- Send a video with the caption `/split <seconds>` to split the video into multiple segments of X seconds.

### Local Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Export your bot token:
   ```bash
   export BOT_TOKEN="your_telegram_bot_token"
   ```
3. Run the bot:
   ```bash
   python bot.py
   ```

### 🐳 Docker Deployment

The easiest way to run the bot is via Docker!

1. Build the image:
   ```bash
   docker build -t shorts-bot .
   ```
2. Run the container:
   ```bash
   docker run -d -e BOT_TOKEN="your_telegram_bot_token" shorts-bot
   ```

---

## 📝 Notes

- The output files will keep the original video extension.
- Make sure you have enough storage space when splitting large videos!
