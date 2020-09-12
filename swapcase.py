def swap(s, n):
        # if n == 0:
        #     return s
        # if s == '':
        #     return s
        newstr = ''
        i = 0
        b = "{:b}".format(n)
        b = str(b)
        len_b = len(b)
        for letter in s:
            if n[i] == '1':
                letter = letter.upper() if letter.islower() else letter.lower()
            if letter.isalpha():
                newstr += letter
            return newstr

    # Stuck here, please Help
