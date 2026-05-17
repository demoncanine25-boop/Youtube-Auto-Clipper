def generate_subtitles(segments, start, end):

    subs = []

    for seg in segments:

        if seg["start"] >= start and seg["end"] <= end:

            subs.append({
                "start": seg["start"] - start,
                "end": seg["end"] - start,
                "text": seg["text"]
            })

    return subs