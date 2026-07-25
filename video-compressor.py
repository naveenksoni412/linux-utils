
import os
import subprocess
import sys
import datetime
import shutil
from pathlib import Path


def compress_video(input_file, folder_path):
    input_path = Path(input_file)
    #output_file = input_path.with_name(f"{input_path.stem}-compressed{input_path.suffix}")
    script_dir = Path(__file__).resolve().parent
    output_file = script_dir / f"{input_path.stem}-compressed{input_path.suffix}"

    # Use ffmpeg to compress the video
    cmd = [
        "ffmpeg",
        "-i", str(input_path),
        "-vcodec", "libx264",
        "-crf", "26",
        "-threads", "0",
        "-preset", "medium",
        "-acodec", "aac",
        "-b:a", "128k",
        "-movflags", "+faststart",
        str(output_file)
    ]
    print(f"Compressing: {input_file}")
    subprocess.run(cmd, check=True)

    # Copy timestamps from input to output
    stat_info = input_path.stat()
    os.utime(output_file, (stat_info.st_atime, stat_info.st_mtime))
    #shutil.move(output_file, folder_path)
    subprocess.run(["gio", "move", output_file, folder_path], check=True)

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for name in files:
            if name.lower().endswith(('.mp4', '.mov', '.mkv', '.avi')):
                full_path = os.path.join(root, name)
                try:
                    compress_video(full_path, folder_path)
                except Exception as e:
                    print(f"Failed to compress {full_path}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compress_videos.py <input_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    if not os.path.isdir(input_folder):
        print("Input path is not a directory.")
        sys.exit(1)

    process_folder(input_folder)
