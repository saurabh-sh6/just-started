a = [[1,5,9],[1,5,8],[3,3,9]]
b = [[4,5,6],[3,5,9],[2,3,8]]
c = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j]+b[i][j]
for i in c :
    print(i)