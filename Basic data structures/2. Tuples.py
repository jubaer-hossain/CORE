tp = tuple() # Empty tuple
tp = (1, 2, 3)
tpTwo = (1)

# Ranged tuples
r = range(0, 20, 2)
print(10 in r)
print(r) # range(0, 20, 2)

for items in r:
    print(items) # 0, 2, 4, 6, 10.... 18 every number in one seperate line

print(r.index(10)) # 5. Cause it is in the 5th in a 0 based index
