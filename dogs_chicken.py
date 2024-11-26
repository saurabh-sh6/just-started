#Number of dogs and chicken are there when the user provides 
# the value of total heads and legs.
heads = int(input("Total number of heads are: "))
legs = int(input("Total number of legs are: "))
remaining_legs = legs - (heads*2)
dogs = remaining_legs/2
chicken = heads - dogs
print(f'''Acoording to the data given, 
      Number of dogs are {dogs} 
      Number of chickens are {chicken}''')