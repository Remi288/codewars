def increment_string(strng):
    #if string is just characters adds 1
    if strng.isalpha() == True:
        s_string = strng.split()
        print(s_string)
        s_string.append('1')
        char_string = "".join(s_string)
        return(char_string)
    #checks if string is just '' and returns 1
    elif strng == '':
        return '1'
    #checks if string contains digits and adds 1 number
    #NEED HELP
    else:
        # final_string = []
        num_string = []
        n_string = list(strng)
        for i in n_string:
            if i.isdigit() == True:
                new_num = int(i) + 1
                newnumstr = str(new_num)
                num_string.append(newnumstr)

# I will stud regular expression and get back to this 
print((increment_string("foo")))
