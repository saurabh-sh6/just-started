n = int(input("Enter the digit here: "))
for i in range (0,n):
    for j in range (i+1):
        print("*", end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()