import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

DOWNLOAD_PATH = "input.mp4"
OUTPUT_PATH = "output.mp4"

# ---------------- TRIM ----------------
async def trim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send a video with /trim <seconds>")

# ---------------- SPLIT ----------------
async def split(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send a video with /split <seconds>")

# ---------------- HANDLE VIDEO ----------------
async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    command = message.caption

    if not command:
        await message.reply_text("❌ Send command with video (e.g. /trim 10)")
        return

    try:
        cmd, value = command.split()
        value = int(value)
    except:
        await message.reply_text("❌ Format: /trim 10 or /split 30")
        return

    file = await message.video.get_file()
    await file.download_to_drive(DOWNLOAD_PATH)

    if cmd == "/trim":
        command_ffmpeg = [
            "ffmpeg",
            "-ss", str(value),
            "-i", DOWNLOAD_PATH,
            "-c", "copy",
            "-y",
            OUTPUT_PATH
        ]

    elif cmd == "/split":
        command_ffmpeg = [
            "ffmpeg",
            "-i", DOWNLOAD_PATH,
            "-c", "copy",
            "-map", "0",
            "-f", "segment",
            "-segment_time", str(value),
            "-reset_timestamps", "1",
            "part_%03d.mp4"
        ]
    else:
        await message.reply_text("❌ Unknown command")
        return

    await message.reply_text("⏳ Processing...")

    subprocess.run(command_ffmpeg)

    if cmd == "/trim":
        await message.reply_video(video=open(OUTPUT_PATH, "rb"))

    elif cmd == "/split":
        for file in sorted([f for f in os.listdir() if f.startswith("part_")]):
            await message.reply_video(video=open(file, "rb"))

    await message.reply_text("✅ Done")

# ---------------- MAIN ----------------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("trim", trim))
app.add_handler(CommandHandler("split", split))
app.add_handler(MessageHandler(filters.VIDEO, handle_video))

app.run_polling()
