s = input("Enter your sentence: ")
v = "aeiou"
s = s.lower()
count = { char:0 for char in v } #creating an empty dictionary 
for char in s :
    if char in count:
        count[char]+=1
print(count)