first = int(input("Enter the first number here: "))
second = int(input("Enter the second number here: "))
if first>second:
    smaller = second
else:
    smaller = first

for i in range(1,smaller+1):
    if first%i==0 and second%i==0 :
        hcf=i
print(hcf)