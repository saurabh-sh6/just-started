punc = """!@#$%&*()_+-[]{},?/`~'"""
s = input("Enter the string here: ")
empty_s = " "
for i in s:
    if i not in punc:
        empty_s += i

print(empty_s)