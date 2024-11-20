a = [[1,2,3],[3,4,5],[6,7,8]]
b = [[3,4,5,1],[6,7,8,3],[4,7,8,6]]
c = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range (len(a)): #for rows of matrix a
    for j in range (len(b[0])): #for columns of matrix b
        for k in range (len(b)): #for the common element, it can be rows of b or coluns of a
            c [i][j]+=a[i][k]*b[k][j]
for i in c:
    print(i)
