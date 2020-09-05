def reverse_words(text):
    new_reverse = []
    text_text = text.split(' ')
    print(text_text)
    for i in text_text:
        tt = i[::-1]
        new_reverse.append(tt)
    return ' '.join(new_reverse)

    # reversed_text = text[::-1]
    # return reversed_text
