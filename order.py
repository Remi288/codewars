import re

def order_please(sentence):

    if sentence == '':
        return ''

    split_up = sentence.split(' ')
    numbers = re.findall('\d+', sentence)

    print(numbers)
    print(split_up)

    dict_sentence = dict(zip(numbers, split_up))

    print(dict_sentence)

    sorted_dict = sorted(dict_sentence.items())
    print(sorted_dict)

    result = [i[1] for i in sorted_dict]
    print(result)

    return " ".join(result)
