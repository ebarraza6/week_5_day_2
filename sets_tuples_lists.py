# # collection = single "variable" used to store multiple values
# # list = [] ordered and changable. Duplicates OK
# # set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# #tuple = () ordered and unchangable. Duplicates OK. FASTER

# fruits= ["apple", "orange", "banana", "coconut", "pineapple", "mango", "watermelon"]


# print(fruits[::-1])
# #::2 gives every 2 element
# #::-1 makes it backwards
# for fruit in fruits:
#     print(fruit)
# # this iterates over list
# # for every fruit in fruits
# print(dir(fruits))
# # attributes for a list
# print(help(fruits))
# # help gives you help about documentation
# print(len(fruits))
# # gives you length of list
# print("apple" in fruits)
# # tells you if an element is in the list
# fruits[0]="kiwi"
# # replaces 0 with an element
# fruits.append("blueberry")
# # adds an elements to the end of a list
# fruits.remove("apple")
# # removes an element from the list
# fruits.insert(0, "strawberry")
# # inserts an element and pushes everything over
# fruits.sort()
# # puts everything in order
# fruits.reverse()
# # reverses based on the order we placed them
# fruits.clear()
# # clears everything
# print(fruits.index("apple"))
# # finds the index of the element

################sets##############
# sets are unordered and unindexed
# they are defined using curly brackets
# they do not allow duplicates
# fruits = {"apple", "banana", "mango", "cherry", "watermelon"}
# print(fruits)
# print(dir(fruits)) # attributes that can be used with sets
# # print(help(fruits))# documentation/methods that can be used with sets
# print(len(fruits)) # number of elements in the set
# # print("volvo" in fruits ) # checks if an element is in the set
# # add an element to the set
# print(fruits.add("orange"))
# print(fruits)
# print(fruits.add("kiwi"))
# print(fruits)
# # add multiple elements to the set
# print(fruits.update(["orange", "kiwi", "pineapple"]))
# print(fruits)
# # remove an element from the set
# print(fruits.remove("banana"))
# print(fruits)
# print(fruits.pop()) # removes the last element in the set
# print(fruits)
# print(fruits.clear()) # clears the set
# print(fruits)

# social_security_numbers = {123456789, 987654321, 123456789}
# print(social_security_numbers.pop)
# print(social_security_numbers)
# print(social_security_numbers.add(457689213))
# print(social_security_numbers)

# ######tuples######
# # tupels are immutable and are defined using parentheses
# # create a tuple called my_tuple with the following values:
example_tuple = (1,2,3,4,5,6,7,8,9,10)
print(example_tuple)
print(example_tuple.count(2)) # count the number of tiems
# the value 2 appears in the tuple
print(dir(example_tuple)) # attributes that can be used with tuples
# print(help(example_tuple))# documentation/methods that can be used with tuples
print(len(example_tuple)) # number of elements in the tuple
print(2 in example_tuple) # check if an element is in the tuple
# # when are they useful?
# # Tuples are useful when you want to store a
# # collection of items that should not be changed
# # , such as days of the week, months of the year, etc.
# # if you want to find the index of a value in a tuple
print(example_tuple.index(2))
# lymeric = "peter pipe picked a pack of pickled peppers"
# # convert the string to a tuple
# # split it first
# lymeric_tuple = tuple(lymeric.split())
# print(lymeric_tuple)
# # find how many times the letter "p" appears in the tuple
# print(lymeric_tuple.count("p"))

# loops with tuples
for item in example_tuple:
    print(item)

######dictionary##############
#dictionarys are unordered, changeable and indexed
#they are defined using curly brackets
#they have keys and values
# a collection of (key:value) pairs, no duplicates
#keys are unique
# values can be of any data type
capitals= { "Kenya":"Nairobi",
           "Uganda":"Kampala",
           "tanzania":"Dodoma",
           "Rwanda": "Kigali",
           "China":"Beijing",
           "USA":"Washington DC"}
print(capitals)
print(dir(capitals))#attributes that can be used with dictionaries
# print(help(capitals))#documentation/methods that can be
#used with dictionaries
print(len(capitals))#number of items in the dictionary
#if you want to check the value of a key in the dictionary
print(capitals["Kenya"])
print(capitals.get("Kenya"))
#add an item to the dictionary
capitals["South Africa"] = "Pretoria"
print(capitals)
capitals.update({"Nigeria":"Abuja"})
capitals.update({"Mexico":"Mexico City"})
capitals.update({"Argentina":"Buenos Aires"})
capitals.update({"Peru":"Lima"})
# add three more countries and their capitals to the dictionary

capitals.pop("China")#remove an item from the dictionary
print(capitals)
#clear the dictionary
# capitals.clear() # do not run this
# loop through the dictionary
for key in capitals:
    print(f"these are the {key}")

for value in capitals.values():
    print(value)
    
# print the key value pairs in the dictionary
    items_all = capitals.items() #key value pairs
    for key, value in items_all:
        print(f"{key} is the capital of {value}")