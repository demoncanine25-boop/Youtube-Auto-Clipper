from downloader import download_video
from transcriber import transcribe_video
from clip_detector import detect_clips
from video_editor import create_clips


def main():

    url = input("Enter YouTube URL: ")

    print("\nDownloading video...")
    video_path = download_video(url)

    print("\nTranscribing video...")
    segments = transcribe_video(video_path)

    print("\nDetecting highlight clips...")
    clips = detect_clips(segments)

    print(f"\nFound {len(clips)} clips")

    print("\nGenerating clips...")
    create_clips(video_path, clips)

    print("\nDone! Clips saved in 'clips' folder.")


if __name__ == "__main__":
    main()