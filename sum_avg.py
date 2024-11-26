add = 0
count = 0

while True:
    num = int(input("Enter your number (0 to stop): "))
    if num != 0:
        add += num
        count += 1
    else:
        print("Thank you!")
        break

if count > 0:
    avg = add / count
    print("Your sum:", add)
    print("Your average is:", avg)
else:
    print("No numbers were entered, so no sum or average to display.")