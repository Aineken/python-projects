from six.moves import reduce

def persistence(n):
    res = 0
    data = n
    arr = []
    while data > 9:
        for i in str(data):
            arr.append(int(i))
        data = reduce(lambda x, y: x*y, arr)
        arr = []

        res +=1

    return res


print(persistence(17))
