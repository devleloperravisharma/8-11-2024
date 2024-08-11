#making a set

eset = {1, 2, 2, 3, 3}

print(eset)

#adding

eset.add(4)

print(eset)

#removing

eset.remove(2)

print(eset)

#discarding

eset.discard(3)

#printing all elements

for element in eset:
    print(element)

#telling if number is in set

if 2 in eset:
    print("2 is in the set")

print(eset)

#making new sets

set1 = {2, 4, 3}
set2 = {5, 4, 2, 3, 9, 8}

#union way 1

print(set1.union(set2))

#intersection way 1

print(set1.intersection(set2))

#difference way 1

print(set2.difference(set1))

#symmetric difference way 1

print(set1.symmetric_difference(set2))

#other ways to write these functions

#union way 2

print(set1 | set2)

#intersection way 2

print(set1&set2)

#difference way 2

print(set2-set1)

#symmetric difference way 2

print(set1^set2)

#seeing what happens if you find the difference of the same set

print(set1.difference(set1))

#                ^
#it's empty!!!!! |