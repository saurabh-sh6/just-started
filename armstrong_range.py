lower = int(input("Enter the lower limit here:" ))
upper = int(input("Enter the upper limit here:"))
for i in range (lower, upper+1):
    temp=i
    order= len(str(i))
    s=0
    while temp>0:
        r = temp%10
        s +=r**order
        temp //= 10
    if (s==i):
        print(i)


