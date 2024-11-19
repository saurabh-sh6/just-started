y = int(input("Enter the year here: "))
if(y%400==0):
    print(f"The year {y} is a leap year.")
elif(y%4==0)and(y%100!=0):
    print(f"The year {y} is a leap year.")
else:
    print(f"The year {y} is not a leap year.")