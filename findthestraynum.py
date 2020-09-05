def stray(arr):
    for j in arr:
        if arr.count(j) == 1:
            return j
