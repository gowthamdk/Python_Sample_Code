def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
li = [0,1,2,3,4]
e = enumerate(li)
