import re


def clean_string(s):
    while '#' in s:
        s = re.sub('.?#', '', s, 1)
    return s


print(clean_string(('abc#d##c')))
