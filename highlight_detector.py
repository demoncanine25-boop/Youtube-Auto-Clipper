def find_highlights(segments):

    keywords = [
        "insane",
        "crazy",
        "unbelievable",
        "no way",
        "what",
        "wow",
        "amazing",
        "look at this"
    ]

    highlights = []

    for seg in segments:
        text = seg["text"].lower()

        if any(k in text for k in keywords):

            start = max(seg["start"] - 5, 0)
            end = seg["end"] + 10

            if end - start >= 10:
                highlights.append((start, end))

    return highlights