n = int(input("Enter any number: "))
if n==1:
    print("1 is not a prime number.")
if n>1:
    for i in range (2,int(n**0.5)+1):
        if n%i == 0:
            print(f"The number {n} is not a prime number.")
            break
    else:
        print(f"The number {n} is a prime number.")