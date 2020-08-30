def two_sum(numbers, target):
    #Loop through the array
    for i in range(0, len(numbers)):
        # print(i)
        for j in range(i +1, len(numbers)):
            print(j)
            # compare if the number in array is equal is target
            if numbers[i] + numbers[j] == target:
                return ([i, j])
