choice = int(input('''chose one of them:
               1 for cm to ft converter
               2 for kms to miles converter
               3 for usd to inr converter
                4 to exit\n'''))
if choice == 1:
    cm = int(input("Enter the value in cm: "))
    ft = cm * 0.4
    print(f"{cm} cm is equal to {ft} ft")
elif choice == 2:
    km = int(input("Enter the value in kms: "))
    miles = km*0.6
    print(f"{km} km is equal to {miles} miles")
elif choice == 3:
    usd = int(input("Enter the value in usd here: "))
    inr = usd*85
    print(f"{usd} usd is equal to {inr} inr")
else:
    print("Thank You.")
