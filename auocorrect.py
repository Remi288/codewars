import re


def autocorrect(input):
    new = re.sub(r'\b[u]|you+\b', 'your sister', input, flags=re.I)
    return new
