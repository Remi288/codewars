# def accum(s):
#  output = ""
#  for i in range(len(s)):
#   output += (s[i] * (i + 1)) + "-"
#  output += (s[i]*(i+1))+"-"
#  return output.title()[:-1]


# print(accum("zpghgh"))

# def accum(s):
#     index = 0
#     char = ''
#     #my new string
#     newstr = ''
#     #loop through the given string
#     i = 0
#     while i < len(s):
#         #acess your index and character
#         index = i
#         char = s[i]
#         #add your uppercase of your character to new string
#         newstr = newstr + char.upper()
#         #add lowercase of your character the number of times the index is
#         for _ in range(index):
#             newstr = newstr + char.lower()
#             #add dash to the string
#         newstr = newstr + '-'
#         i = i + 1
#         #slice the last char and return string
#     return newstr[:-1]


