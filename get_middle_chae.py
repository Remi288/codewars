def get_middle(str):
  word_length = len(str)
  middle_char = word_length/2
  if word_length % 2 == 0:
    return str[middle_char - 1: middle_char + 1]
  else:
    return str[middle_char: middle_char + 1]
