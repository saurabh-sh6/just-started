a = input("Enter your string here: ")
rev = a[ : : -1]
if rev == a:
    print(f"String {a} is a palindrome.")
else:
    print(f"String {a} is not a palindrome.")