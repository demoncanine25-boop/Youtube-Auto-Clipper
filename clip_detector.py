def detect_clips(segments):

    clips = []

    for seg in segments:

        text = seg["text"]

        if len(text.split()) > 8:   # interesting sentence

            clips.append({
                "start": seg["start"],
                "end": seg["end"],
                "text": text
            })

    return clips