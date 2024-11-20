friends = {"Rachel":56, "monica":91, "mohit":5}
s = sorted(friends.items(), key = lambda x: x[1])
print(s)