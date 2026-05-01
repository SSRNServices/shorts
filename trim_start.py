import subprocess
import shutil
from pathlib import Path

def get_ffmpeg():
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        print("❌ FFmpeg not found in PATH.")
        return None
    return ffmpeg


def trim_video():
    ffmpeg = get_ffmpeg()
    if not ffmpeg:
        return

    video_path = input("Enter video path: ").strip().strip('"')
    video = Path(video_path)

    if not video.exists():
        print("❌ File not found")
        return

    try:
        cut_seconds = float(input("Enter seconds to REMOVE from start: "))
        if cut_seconds < 0:
            raise ValueError
    except:
        print("❌ Invalid input")
        return

    output_file = video.parent / f"{video.stem}_trimmed{video.suffix}"

    command = [
        ffmpeg,
        "-ss", str(cut_seconds),   # start after X seconds
        "-i", str(video),
        "-c", "copy",              # fast (no re-encode)
        "-avoid_negative_ts", "make_zero",
        "-y",
        str(output_file)
    ]

    print("\n⏳ Trimming video...")

    try:
        subprocess.run(command, check=True)
        print(f"\n✅ Done! Output saved as: {output_file}")
    except subprocess.CalledProcessError:
        print("❌ Failed to trim video")


if __name__ == "__main__":
    trim_video()