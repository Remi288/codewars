def solution(s):
    #loop through if any char start with cap replace it with space
    ss = ''
    for i in s:
        if i.upper() == i:
            ss = ss + ' ' + i
        else:
            ss = ss + i
    return ss




print((solution("helloWorld")))