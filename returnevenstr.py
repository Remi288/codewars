def even_chars(st):
    '''
    This will check and return a new list of even char in a given string
    loop through the length of the string starting from index one
    check if i is even number
    append string[index] to new array
    '''
    # create a new arrary
    newarry = []

    str_length = len(st)
    if str_length < 2 or str_length > 100:
        return 'invalid string'
    else:
        for i in range(1, str_length): # or (1, str_length, 2) and 
            if i % 2 == 1: # remove this
                newarry.append(st[i])
        return (newarry)


print(even_chars("aBc_e9g*i-k$m"))
