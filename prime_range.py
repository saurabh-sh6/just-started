lower = int(input("Enter the lower limit here: "))
upper = int(input("Enter the upper limit here: "))
for i in range(lower, upper+1):
    if i>0:
        for j in range(2,i):
            if i%j==0:

                break
        else:
            print(i,end=" ")