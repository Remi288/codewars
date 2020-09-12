

def solve(s):
    if s == s[::-1]:
        return 'OK'
    elif s != s[::-1]:
        s = s[:-1]
        return 'remove one'
    else:
        return 'not possible'
    #did not pass all cases
