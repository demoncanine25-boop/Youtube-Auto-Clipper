import sys
from downloader import download_video
from transcriber import transcribe
from highlight_detector import find_highlights
from video_editor import create_clips


def main():

    url = input("Enter YouTube video URL: ")

    print("\nDownloading video...")
    video_path = download_video(url)

    print("\nTranscribing video...")
    segments = transcribe(video_path)

    print("\nDetecting highlights...")
    highlights = find_highlights(segments)

    print(f"\nFound {len(highlights)} highlight clips")

    print("\nGenerating clips with subtitles...")
    create_clips(video_path, highlights, segments)

    print("\nDone! Clips saved in /clips folder")


if __name__ == "__main__":
    main()