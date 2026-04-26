import os
import subprocess
import shutil
from pathlib import Path

def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("❌ FFmpeg not found.")
        print("👉 Install it and make sure it's in PATH.")
        print("Windows: https://ffmpeg.org/download.html")
        print("Ubuntu: sudo apt install ffmpeg")
        return False
    return True

def split_video():
    if not check_ffmpeg():
        return

    video_path = input("Enter full path of video file: ").strip().strip('"')

    video = Path(video_path)

    if not video.exists():
        print("❌ File does not exist.")
        return

    try:
        duration = int(input("Enter segment duration (seconds): ").strip())
        if duration <= 0:
            raise ValueError
    except ValueError:
        print("❌ Invalid duration.")
        return

    output_dir = video.parent / f"{video.stem}_parts"
    output_dir.mkdir(exist_ok=True)

    output_pattern = str(output_dir / f"Video-%03d{video.suffix}")

    command = [
        "ffmpeg",
        "-i", str(video),
        "-c", "copy",
        "-map", "0",
        "-f", "segment",
        "-segment_time", str(duration),
        "-reset_timestamps", "1",
        output_pattern
    ]

    print("\n⏳ Splitting video...")

    try:
        subprocess.run(command, check=True)
        print(f"\n✅ Done! Files saved in: {output_dir}")
    except subprocess.CalledProcessError as e:
        print("❌ FFmpeg failed.")
        print(e)

if __name__ == "__main__":
    split_video()