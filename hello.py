# #hello python
# # Print "Hello World!"
# print("Hello world!")
# # Print "Have a good day."
# print("Have a good day. ")
# # Print "Learning Python is fun!"
# print("Learning Python is fun!")

# print("line 1 ", end="")
# print("line 2 ")

# # Print "I am" and the number 25
# print("I am", 25)


# """
# Comment
# """


# x=1
# print(x)
# print(type(x))


#unpacking

# fruits = ["apple","banana","mango"]

# x,y,z = fruits
# print(x)
# print(y)
# print(z)


#global keyword

# x = "global"

# def myfun():
#     x = "local"
#     print(x)

# myfun();
# print(x)

# # Create variable x with value 5
# x =5
# # Create variable y with value "John"
# y = "John"
# # Print the type of x
# print(type(x))


#interview 

# x = 100
# y = x

# x = 200

# print(x)
# print(y)
# print(x is y)


# data = ([1, 2], 10)
# alias = data

# data[0].append(3)

# print(data)
# print(alias)

# data[0] = [7, 8]





# training_data = [10, 20, 30]

# def normalize(data):
#     data[0] = 0
#     return data

# normalized_data = normalize(training_data)

# print(training_data)
# print(normalized_data)
# print(training_data is normalized_data)

# [0, 20, 30]
# [0, 20, 30]
# True

#both refers to same object so it basically change the original object also



# #shallow copy 
# def normalize(data):
#     result = data.copy()
#     result[0] = 0
#     return result

# training_data = [10, 20, 30]
# normalized_data = normalize(training_data)

# print(training_data)      # [10, 20, 30]
# print(normalized_data)    # [0, 20, 30]
# print(training_data is normalized_data)  # False




# base_config = {
#     "learning_rate": 0.01,
#     "epochs": 10
# }

# experiment_a = base_config
# experiment_b = base_config

# experiment_a["learning_rate"] = 0.1

# print(experiment_b["learning_rate"])

# 0.1




# base_config = {
#     "learning_rate": 0.01,
#     "epochs": 10
# }

# experiment_a = base_config
# experiment_b = base_config

# experiment_a["learning_rate"] = 0.1

# print(experiment_b["learning_rate"])

#solution = create deep copy /not shallow copy 





# predictions = [
#     {"class": "cat", "score": 0.92},
#     {"class": "dog", "score": 0.81}
# ]

# predictions_backup = predictions.copy()

# predictions_backup[0]["score"] = 0.1

# print(predictions)
# print(predictions_backup)

# [{'class': 'cat', 'score': 0.1}, {'class': 'dog', 'score': 0.81}]
# [{'class': 'cat', 'score': 0.1}, {'class': 'dog', 'score': 0.81}]

# #.copy creates outer list , inner one still remain shared .


# solution = deepcopy

# import copy

# predictions_backup = copy.deepcopy(predictions)
# predictions_backup[0]["score"] = 0.1

# print(predictions[0]["score"])         # 0.92
# print(predictions_backup[0]["score"])  # 0.1





# from numbers import Real

# def preprocess(config, features):
#     if not isinstance(config, dict):
#         raise TypeError("config must be a dictionary")

#     if not isinstance(features, list):
#         raise TypeError("features must be a list")

#     multiplier = config.get("multiplier", 1)

#     if (
#         isinstance(multiplier, bool)
#         or not isinstance(multiplier, Real)
#     ):
#         raise TypeError("multiplier must be a real number")

#     if any(
#         isinstance(value, bool) or not isinstance(value, Real)
#         for value in features
#     ):
#         raise TypeError("all features must be real numbers")

#     processed_features = [
#         value * multiplier for value in features
#     ]

#     effective_config = config.copy()

#     return processed_features, effective_config


# config = {"multiplier": 2}
# features = [1, 2, 3]

# processed, effective_config = preprocess(config, features)

# print(processed)
# print(effective_config)
# print(features)
# print(config)

#sss



# x = 1    # int
# y = 2.8e1  # float
# z = 1j # complex  j is imaginary value

# print(type(x))
# print(type(y))
# print(type(z))

# a=float(x)
# print(a) # type conversion 


# import random 
# print(random.randrange(1,10))

# # dir(random)

# # dir : for getting all the methods of anything

# # Create an integer
# x=5
# # Create a float
# y=3.14
# # Create a complex number
# z=2+3j
# # Print the types
# print(type(x))
# print(type(y))
# print(type(z))



# #casting 

# # Create an integer
# x=1
# # Convert to float
# a=float(x)
# # Convert to string
# b=str(x)
# # Print values
# print(x)
# print(a)
# print(b)




# a = "Hello, World!"
# print(a[1])

# for x in "banana":
#   print(x)

# a = "Hello, World!"
# print(len(a))


# #in
# # To check if a certain phrase or character is present in a string, we can use the keyword in

# print("Hello" in a)

# #if
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

#   #if NOT
#   txt = "The best things in life are free!"
# print("expensive" not in txt)


# a = "hello everyone !"

# # x=print(a[2:4])
# # y=print(a[-6:-2])
# # z=print(a[:5])

# # print(a.upper())
# # print(a.lower())

# # print(a.strip()) # removes white space from start or end
# # print(a.replace("H", "J"))

# #split
# print(a.split(",")) # returns ['Hello', ' World!']

# b = "2"
# print(a+" "+b)

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)


# #questions

# # Create the variable
# txt = "Hello, World!"
# # Print characters from index 2 to 5
# print(txt[2:5])
# # Print in upper case
# print(txt.upper())
# # Create the name variable
# name = "Python"
# # Print using an f-string
# print(f"I love {name}")


#string methods

# txt = "hello, and welcome to my world."
# x = txt.capitalize()
# print (x)

# txt = "Hello, And Welcome To My World!"
# x = txt.casefold()
# print(x)

# txt = "Hello, welcome to my world."
# x = txt.index("welcome")
# print(x)


# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))

# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")



# x = 10
# y = 25

# print(x/y) #returns float
# print(x//y) #returns integer




# # The Walrus operator  :=

# numbers = [1, 2, 3, 4, 5]

# if (count := len(numbers)) > 3:
#     print(f"List has {count} elements")

num = 6

# x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

# print(x)

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)
# print(x is y)
# print(x == y)

# x = [1, 2, 3]
# y = [1, 2, 3]

# print(x == y)
# print(x is y)

# fruits = ["apple", "banana", "cherry"]

# print("banana" in fruits)





# # Create variables
# a=15
# b=4
# # Print modulus
# print(a%b)
# # Print floor division
# print(a//b)
# # Print power
# print(a**b)
# # Add 10 to a
# a+=10





# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[2:])
# print(thislist[-4:-1])
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")


# #changing value
# thislist[1] = "blackcurrant"
# thislist[1:3] = ["blackcurrant", "watermelon"]


# #insert method
# thislist.insert(2, "watermelon")
# print(thislist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# # newlist = []
# # for x in fruits:
# #     if "a" in x:
# #         newlist.append(x)
# # print(newlist)

# #new comprehension method
# newlist = [x for x in fruits if "a" in x]
# print(newlist)


# list1 = [10,44,86,11,1,234]
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)


#how to change tuple 
#convert it to list , change in list , convert again into tuple
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# #can add tuple to tuple

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)


# #unpacking tuple (normally vs using Asterisk)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)


# # Create the tuple
# fruits=("apple","banana","cherry")
# # Print the second item
# print(fruits[1])
# # Print the number of items
# print(len(fruits))
# # Unpack the tuple
# (a,b,c) = fruits
# # Print b
# print(b)

#frozen set

# x = frozenset({"apple", "banana", "cherry"})

# #display x:
# print(x)

# #display the data type of x:
# print(type(x)) 


# # Create the set
# colors = {"red", "green", "blue"}

# # Print the set
# print(colors)

# # Add "yellow"
# colors.add("yellow")

# # Remove "green"
# colors.discard("green")

# # Print the number of items
# print(len(colors))

#dictionary

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()
# y = car.values()
# z = car.items()

# print(x) #before the change
# print(y)
# print(z)
# car["color"] = "white"

# print(x) #after the change
# print(y)
# print(z)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)



# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }


# print(myfamily["child2"]["name"])

# # Create the dictionary
# car= {
# 	"brand":"Ford",
# 	"model":"Mustang",
# 	"year":2024
# }
# # Print the model
# print(car["model"])
# # Add a color key
# car["color"]="red"
# # Remove the brand key
# car.pop("brand")
# # Print the dictionary
# print(car)



# a = 2
# b = 330
# print("A") if a > b else print("B")

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# x = 15
# y = 20
# max_value = x if x > y else y
# print("Maximum value:", max_value)


# temperature = 25
# is_raining = False
# is_weekend = True

# if (temperature > 20 and not is_raining) or is_weekend:
#   print("Great day for outdoor activities!")

# #nested 

# username = "Emil"
# password = "python123"
# is_active = True

# if username:
#   if password:
#     if is_active:
#       print("Login successful")
#     else:
#       print("Account is not active")
#   else:
#     print("Password required")
# else:
#   print("Username required")


# # Create age variable
# age = 20;
# # Write if/elif/else
# if age<13:
# 	print("Child")
# elif age<18:
# 	print("Teenager")
# else:
# 	print("Adult")


# #match in python

# # Create variable day
# day=3;
# # Use match statement

# match day:
# 	case 3:
# 		print("Wednesday")
# 	case _:
# 		print("Other day")


# Create the i variable
# i=0;
# # While loop: print 1-5, skip 3 with continue
# while i<6:
# 	i+=1;
# 	if i == 3:
# 		continue
# 	print(i)

# # Create the fruits list
# fruits = ["apple","banana","cheery"]
# # Loop through fruits, break at "banana"
# for x in fruits:
# 	print(x)
# 	if x=="banana":
# 		break



#function



#keyword argument

# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(animal = "dog", name = "Buddy")


# #positional argument

# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function("Buddy", "dog")


# #mixing

# def my_function(animal, name, age):
#   print("I have a", age, "year old", animal, "named", name)

# my_function("dog", name = "Buddy", age = 5)


# #combining

# def my_function(a, b, /, *, c, d):
#   return a + b + c + d

# result = my_function(5, 10, c = 15, d = 20)
# print(result)

# *args

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


#  **Kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



#unpacking list 

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

#unpacking Dictionary

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)
