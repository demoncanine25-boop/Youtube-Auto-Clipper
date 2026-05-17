from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import os


def create_clips(video_path, highlights, segments):

    os.makedirs("clips", exist_ok=True)

    video = VideoFileClip(video_path)

    clip_number = 1

    for start, end in highlights:

        subclip = video.subclipped(start, end)

        subtitles = []

        for seg in segments:

            if seg["start"] >= start and seg["end"] <= end:

                txt = TextClip(
                    text=seg["text"],
                    font="C:/Windows/Fonts/arial.ttf",
                    font_size=40,
                    color="white",
                    stroke_color="black",
                    stroke_width=2,
                    method="caption",
                    size=subclip.size
                )

                txt = txt.with_start(seg["start"] - start)
                txt = txt.with_end(seg["end"] - start)
                txt = txt.with_position(("center", "bottom"))

                subtitles.append(txt)

        final = CompositeVideoClip([subclip] + subtitles)

        output = f"clips/clip_{clip_number}.mp4"

        final.write_videofile(
            output,
            codec="libx264",
            audio_codec="aac"
        )

        clip_number += 1

    video.close()