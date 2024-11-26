s = int(input("Enter your annual salary here: "))
if s>=500000 and s<=1000000:
    tax = 0.10*(s)
elif s >=1100000 and s<=2000000:
    tax = 0.20*(s)
else:
    tax = 0.30*(s)
in_hand = s - tax -(0.10*s) - (0.05*s)-(0.03*s)
monthly = in_hand/12
print("Your In hand monthly salary is: ", monthly)