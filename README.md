# Shorts

A simple Python utility to split a video into smaller segments using FFmpeg.

## Requirements

- Python 3
- FFmpeg installed and available in your `PATH`

## Usage

1. Run the script:

```bash
python3 script.py
```

2. Enter the full path to the video file when prompted.
3. Enter the desired segment duration in seconds.
4. Enter the TOP and BOTTOM padding height in pixels.
5. Enter the padding color in HEX format (e.g., `#000000`).
6. Choose a font for the "Part-XX" text from the given menu, or provide a custom font path.
7. The script creates a folder next to the input file named `<video_name>_parts` and saves the split segments there.

## Notes

- FFmpeg and FFprobe are required to be installed and available in your `PATH`.
- The script adds top and bottom padding to each segment and overlays a "Part-XX" text label on the top padding.
- The output files keep the original video extension.
- If the file path is invalid or numeric inputs are incorrect, the script exits with an error message.

## Example

If you split `movie.mp4` with duration `10`, output files will be saved as:

```
movie_parts/Video-001.mp4
movie_parts/Video-002.mp4
```
