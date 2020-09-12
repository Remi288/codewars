def is_isogram(s):

    if len(s) == len(set(s.lower())):
        return True
    else:
        return False


print(is_isogram('abba'))


'''
  # def is_isogram(s):
    # return len(s) == len(set(s.lower()))

'''


# def is_isogram(string):
#     lower_str = string.lower()
#     newarry = []
#     for char in lower_str:
#         if char not in newarry:
#             newarry.append(char)
#         else:
#             return False
#     return True
