import os
import subprocess
from pathlib import Path
import shutil
import platform

def get_ffmpeg():
    ffmpeg = shutil.which("ffmpeg")
    ffprobe = shutil.which("ffprobe")

    if not ffmpeg or not ffprobe:
        print("❌ FFmpeg not found in PATH.")
        return None, None

    return ffmpeg, ffprobe


def choose_font():
    system = platform.system()

    if system == "Windows":
        fonts = {
            "1": ("Arial", "C:/Windows/Fonts/arial.ttf"),
            "2": ("Arial Bold", "C:/Windows/Fonts/arialbd.ttf"),
            "3": ("Calibri", "C:/Windows/Fonts/calibri.ttf"),
            "4": ("Times New Roman", "C:/Windows/Fonts/times.ttf"),
        }

    elif system == "Linux":
        fonts = {
            "1": ("DejaVu Sans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
            "2": ("DejaVu Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
            "3": ("Liberation Sans", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"),
            "4": ("FreeSerif", "/usr/share/fonts/truetype/freefont/FreeSerif.ttf"),
        }

    elif system == "Darwin":
        fonts = {
            "1": ("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"),
            "2": ("Arial Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
            "3": ("Helvetica", "/System/Library/Fonts/Helvetica.ttc"),
        }

    else:
        fonts = {}

    print("\n🎨 Choose Font:")
    for key, (name, _) in fonts.items():
        print(f"{key}. {name}")
    print("9. Custom font path")

    choice = input("Enter choice: ").strip()

    if choice in fonts:
        path = fonts[choice][1]
        if os.path.exists(path):
            return path
        else:
            print("⚠️ Font not found. Falling back to default.")

    elif choice == "9":
        custom = input("Enter full font path (.ttf/.otf): ").strip()
        if os.path.exists(custom):
            return custom
        else:
            print("❌ Invalid path. Using default.")

    # fallback
    if system == "Windows":
        return "C:/Windows/Fonts/arial.ttf"
    elif system == "Linux":
        return "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    else:
        return "/System/Library/Fonts/Supplemental/Arial.ttf"


def split_video():
    ffmpeg, ffprobe = get_ffmpeg()
    if not ffmpeg:
        return

    video_path = input("Enter video path: ").strip().strip('"')
    video = Path(video_path)

    if not video.exists():
        print("❌ File not found")
        return

    try:
        duration = int(input("Enter segment duration (seconds): "))
        top_pad = int(input("Enter TOP padding height (px, e.g. 80): "))
        bottom_pad = int(input("Enter BOTTOM padding height (px, e.g. 40): "))
    except:
        print("❌ Invalid numeric input")
        return

    color = input("Enter padding color (HEX like #000000): ").strip()

    font_path = choose_font()

    output_dir = video.parent / f"{video.stem}_parts"
    output_dir.mkdir(exist_ok=True)

    # Get total duration
    probe_cmd = [
        ffprobe,
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(video)
    ]

    total_duration = float(subprocess.check_output(probe_cmd).decode().strip())

    part = 1
    start = 0

    while start < total_duration:
        output_file = output_dir / f"Video-{part:03d}{video.suffix}"
        text = f"Part-{part:02d}"

        vf = (
            f"pad=iw:ih+{top_pad + bottom_pad}:0:{top_pad}:color={color},"
            f"drawtext=fontfile='{font_path}':"
            f"text='{text}':fontcolor=white:fontsize=36:"
            f"x=(w-text_w)/2:y={top_pad//3}"
        )

        command = [
            ffmpeg,
            "-ss", str(start),
            "-t", str(duration),
            "-i", str(video),
            "-vf", vf,
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "23",
            "-c:a", "aac",
            "-y",
            str(output_file)
        ]

        print(f"⏳ Processing Part {part}...")

        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError:
            print(f"❌ Failed at Part {part}")
            return

        start += duration
        part += 1

    print(f"\n✅ Done! Files saved in: {output_dir}")


if __name__ == "__main__":
    split_video()