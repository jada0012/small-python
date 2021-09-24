odds = set([i for i in range(1, 10, 2)])
evens  = set([i for i in range(0, 10, 2)])

u = odds.union(evens) #finds union of 2 sets
i = odds.intersection(evens) #finds intersection

setA = {2, 3, 4, 6, 9, 12}
setB = {1, 2, 3, 5, 9}

setA.update(setB) #adds the two sets
print(setA)
setA.intersection_update(setB) #updates set with only items in intersection
print(setA)
setA.difference_update(setB) #updates set with only items not in intersection
print(setA)
