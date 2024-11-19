n=int(input("Enter the number here: "))
result = list(map(lambda x :2**x,range(n+1)))
for i in range (n+1):
    print(result[i])