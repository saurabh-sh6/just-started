cp = int(input("Enter the cost price of the article: "))
sp = int(input("Enter the selling price of the article: "))
if sp >cp:
    p= sp-cp
    print(f"you have a profit of {p}")
else:
    l= cp-sp
    print(f"You have a loss of {l}")