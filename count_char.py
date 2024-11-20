word = input("Enter the string: ")
char_count = { }
for char in word:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char] = 1
for char, count in char_count.items():
    print(f"{char} : {count}")