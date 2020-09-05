def binary_array_to_number(arr):
    arr_str = ''
    for i in arr:
        arr_str += str(i)

    return int(arr_str, 2)


print((binary_array_to_number([0, 0, 0, 1])))
