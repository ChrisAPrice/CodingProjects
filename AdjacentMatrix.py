import numpy as np

matrixtest = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])

A = np.empty([25,25], dtype=int)

for r in matrixtest:
    print(r)

# tuple (base, adj,adj,adj)
tup1 = (1,2,6)
tup2 = (2,1,3,7)
tup3 = (3,2,4,8)
tup4 = (4,3,5,9)
tup5 = (5,4,10)
tup6 = (6,1,7,11)
tup7 = (7,2,6,8,12)
tup8 = (8,3,7,9,13)
tup9 = (9,4,8,10,14)
tup10 = (10,5,9,15)
tup11 = (11,6,12,16)
tup12 = (12,7,11,13,17)
tup13 = (13,8,12,14,18)
tup14 = (14,9,13,15,19)
tup15 = (15,10,19,25)
tup16 = (16,11,17,21)
tup17 = (17,12,16,18,22)
tup18 = (18,13,17,19,23)
tup19 = (19,14,18,20,24)
tup20 = (20,15,19,25)
tup21 = (21,16,22)
tup22 = (22,17,21,23)
tup23 = (23,18,22,24)
tup24 = (24,19,23,25)
tup25 = (25,20,24)

list = [tup1,tup2,tup3,tup4,tup5,
        tup6,tup7,tup8,tup9,tup10,
        tup11,tup12,tup13,tup14,tup15,
        tup16,tup17,tup18,tup19,tup20,
        tup21,tup22,tup23,tup24,tup25]

for i in list:
    for x in i[0:len(i)]:
        A[i[0]-1][x-1] = 1

for a in A:
    print(a)