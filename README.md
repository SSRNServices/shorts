# Shorts

Python utilities to process videos using FFmpeg.

## Requirements

- Python 3
- FFmpeg and FFprobe installed and available in your `PATH`

## Scripts

### 1. Split Video (`script.py`)
Splits a video into smaller segments, adds padding, and overlays a "Part-XX" text label.

**Usage:**
```bash
python3 script.py
```
1. Enter the full path to the video file when prompted.
2. Enter the desired segment duration in seconds.
3. Enter the TOP and BOTTOM padding height in pixels.
4. Enter the padding color in HEX format (e.g., `#000000`).
5. Choose a font for the "Part-XX" text from the given menu, or provide a custom font path.

**Output:**  
Creates a folder next to the input file named `<video_name>_parts` containing the split segments.

### 2. Trim Start of Video (`trim_start.py`)
Removes a specified number of seconds from the beginning of a video without re-encoding (fast).

**Usage:**
```bash
python3 trim_start.py
```
1. Enter the full path to the video file when prompted.
2. Enter the number of seconds to remove from the start.

**Output:**  
Creates a new file next to the input file named `<video_name>_trimmed<extension>`.

## Notes

- The output files keep the original video extension.
- If the file path is invalid or numeric inputs are incorrect, the scripts exit with an error message.
