a = input ("Enter your word here: ")
w = a.split()
w = [i.lower() for i in w]
# for i in range (len(w)):
#     w[i] = w[i].lower()
w.sort()
for i in w:
    print(i)