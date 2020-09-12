def increment_string(strng):
    if not strng:
        return "1"
    lastchar = strng[-1]
    if lastchar.isalpha():
        return strng + '1'
    else:
        num = ''
        for i in strng[::-1]:
            if i.isnumeric():
                num = num + i
                print(num)
            else:
                break
        reverse_num = num[::-1]
        reverse_num_int = int(reverse_num) + 1
        reverse_num_int_str = str(reverse_num_int)
        # length_strng = len(strng)
        length_reverse = len(reverse_num_int_str)
        length_num = len(reverse_num)
        newstr = strng[:-length_num]

        if length_num > length_reverse:
            diff = length_num - length_reverse
            leading_zero = ('0' * diff) + reverse_num_int_str
            return newstr + leading_zero
        return newstr + str(reverse_num_int)
        


                

print((increment_string("foo001")))
