scratch = ["eye animation","mio mau", "game project", "microsoft paint"]

sampleset = set(scratch)

print(sampleset)

#printing a singular item

# sets are a pain and aren't indexable >:( print(sampleset[2])

#making an empty set because apperently we need this

meowtitymeowmeowset = set([])

#printing it because the output which gives "set()" is supposed to be meaningful to code.

print(meowtitymeowmeowset)

#if you want to add new items to a set (see why we have empty sets.)

meowtitymeowmeowset.add("meowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeowmeowtitymeowmeow")

#printing a very meanigful essay

print(meowtitymeowmeowset)

#adding more stuff because i need a bigger essay

meowtitymeowmeowset.add("maybe I should stop saying meowtitymeowmeowmeow. But thats a- okay")

meowtitymeowmeowset.add("Although my original essay was extrememly important for my given assignment, I cannot move further in the assignment without defining the meaning of meowtitymeowmeowmeow")

meowtitymeowmeowset.add("to define this very abstract word, it is do describe a cat of which feels the need to express itself in a new way of speech. meowtity is a new word in the cat dictionary, but in cattok, the popular social media platform among cats, decided to make a new work, involving this meowtity word, a revolutionary for meowons and meowons. To add to current 'lingo' as some call it, meow is a basic word of speech and by concatinating the two words, we get the revolutionary word: meowtitymeowmeowmeow")

meowtitymeowmeowset.add("mEoWWWoiehfdoefih")

meowtitymeowmeowset.add("no no meow meow")

#printing the very important essay

print(meowtitymeowmeowset)

#removing the 'accidental' mistakes

#using remove functions because it was important to have 2 diffferent ways to remove

meowtitymeowmeowset.remove("no no meow meow")

#printing to see if this stupid function works >:(

print(meowtitymeowmeowset)

#meowtitymeowmeowset.remove("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

#key error - you cannot remove something that isn't there (quite obvious) using remove

#somehow the discard doesnt give an error because it doesn't care

meowtitymeowmeowset.discard("kkkkkkkkkkkkkkkkkkk")

print(meowtitymeowmeowset)

#set operations -- union, interception, difference, symmetric difference

a = {5, 2, 6, 3, 9}

b = {1, 6, 3, 8, 5}

#using union because we need it (?)

print("union operation")

print(a.union(b))

#more ways?!

print(a|b)

#intersection along meow st and meow dr

print("intersection operation")

print(a.intersection(b))

#another :0

print(a&b)

#the difference between us

print("difference of sets operation")

print("difference from set a to b")

print(a.difference(b))

print("difference from set b to a")

print(b-a)

#symmetric difference (i gave up on being mad im too tired)

print(a.symmetric_difference(b))

print("symmetric difference the other way around, set b to a")

print(b^a)