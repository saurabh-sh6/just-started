a = int(input("Enter first number here: "))
b = int(input("Enter second number here: "))
MaxNum = max(a,b)
while(True):
    if (MaxNum%a==0 and MaxNum%b==0):
        break
    MaxNum+=1
print(f"The LCM of {a} and {b} is {MaxNum}")