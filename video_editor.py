from moviepy import VideoFileClip
import os

CLIP_FOLDER = "clips"

def create_clips(video_path, clips):

    video = VideoFileClip(video_path)

    for i, clip in enumerate(clips):

        start = clip["start"]
        end = clip["end"]

        subclip = video.subclipped(start, end)

        output = os.path.join(CLIP_FOLDER, f"clip_{i+1}.mp4")

        subclip.write_videofile(output)

    video.close()