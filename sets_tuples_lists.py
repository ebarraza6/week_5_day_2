# collection = single "variable" used to store multiple values
# list = [] ordered and changable. Duplicates OK
# set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#tuple = () ordered and unchangable. Duplicates OK. FASTER

fruits= ["apple", "orange", "banana", "coconut", "pineapple", "mango", "watermelon"]

print(fruits[::-1])
#::2 gives every 2 element
#::-1 makes it backwards
for fruit in fruits:
    print(fruit)
# this iterates over list
# for every fruit in fruits
print(dir(fruits))
# attributes for a list
print(help(fruits))
# help gives you help about documentation
print(len(fruits))
# gives you length of list
print("apple" in fruits)
# tells you if an element is in the list
fruits[0]="kiwi"
# replaces 0 with an element
fruits.append("blueberry")
# adds an elements to the end of a list
fruits.remove("apple")
# removes an element from the list
fruits.insert(0, "strawberry")
# inserts an element and pushes everything over
fruits.sort()
# puts everything in order
fruits.reverse()
# reverses based on the order we placed them
fruits.clear()
# clears everything
print(fruits.index("apple"))
# finds the index of the element
