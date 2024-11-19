# n = int(input("Enter the number here: "))
# if n == 0:
#     print(n)

# else:
#     s=0
#     for i in range(1,n+1):
#         s += i
#     print(f"The sum of {n} natural numbers is",s)
def sum(a):
    if a == 0:
        return a
    else:
        return a + sum(a-1)
    
n = int (input("Enter the number here: "))
if n<0:
    print("Enter a positive number here.")
else:
    print(f"The sum of {n} natural numbers is ",sum(n))