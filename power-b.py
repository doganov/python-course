L = [1, 2, 4, 8, 16, 32, 64]
X = 5

for n in L:
    if 2 ** X == n:
        print 'at index', L.index(n)
        break
else:
    print X, 'not found'
