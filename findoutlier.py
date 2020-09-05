
def find_outlier(integers):
    newarry = [i for i in integers if i % 2 == 0]
    if len(newarry) == 1:
      return newarry[0]
    else:
      for i in integers:
        if i not in newarry:
          return i
