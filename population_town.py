flag = 0
a = int(input("What is the population of the town now: "))
p = int(input("How much reduction is there: "))
print(f"Yearly reduction in the population by {p} % for the next 10 years: ")
print(a)
while True:
    b = a*((100-p)/100)
    a = b 
    print(int(b))
    flag+=1
    if flag == 9:
        break