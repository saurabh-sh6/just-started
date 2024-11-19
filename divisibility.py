lower = int(input("Enter the lower limit here: "))
upper = int(input("Enter the upper limit here: "))
n = int(input("You want to check the divisibility of: "))
print(f"Numbers that are divisible by {n} are: ")
for i in range (lower, upper+1):
    
    if i % n ==0:
        # print(i)
        print(i)