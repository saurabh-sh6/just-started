letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
import random
# pas = " "
# for i in range (0,nr_letters):
#     pas +=random.choice(letters)
# for i in range (0, nr_symbols):
#     pas += random.choice(symbols)
# for i in range (0, nr_numbers):
#     pas += random.choice(numbers)
# print(pas)
pas_l = [ ]
for i in range (0,nr_letters):
    pas_l +=random.choice(letters)
for i in range (0, nr_symbols):
    pas_l += random.choice(symbols)
for i in range (0, nr_numbers):
    pas_l += random.choice(numbers)

random.shuffle(pas_l)
for i in pas_l:
    print(i,end="")
