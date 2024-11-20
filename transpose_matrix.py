a = [[1,3,5],[2,3,6]]
b = [[0,0],[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i]=a[i][j]
for i in b:
    print(i)

# b = [ [a[j][i] for j in range (len(a))] for i in range (len(a[0]))]
# for i in b:
#     print(i)