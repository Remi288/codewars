def sum_two_smallest_numbers(numbers):
    nn = min(numbers)
    numbers.remove(nn)
    nn2 = min(numbers)
    numbers.remove(nn2)
    sumnumber = nn + nn2
    return sumnumber
    

#    numbers.sort()
#    return numbers[0] + numbers[1]



print((sum_two_smallest_numbers([5, 8, 12, 18, 22])))
