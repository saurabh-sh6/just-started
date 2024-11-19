# def fact(a):
#     if a == 0:
#         return 1
#     else:
#         return a * fact(a-1)
# n = int(input("Enter the number here: "))
# if n<0:
#     print("Please enter a positive number.")
# if n>=0:
#     print(f"Factorial of {n} is {fact(n)}")
n = int(input("Enter the number here: "))
fact=1
if n<0:
    print("Please enter a positive number.")
if n==0:
    print("The factorial is 1.")
if n>0:
    for i in range (1,n+1):
        fact = fact*i
    print(f"The factorial of {n} is {fact}")