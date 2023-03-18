
def concatenate_text(labels, text):

    clusters = {}

    for label, sentence in zip(labels, text):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(sentence)

    concatenated_text = {}

    for label in clusters:
        concatenated_text[label] = ' '.join(clusters[label])
    return concatenated_text
