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

# def my_function(*numbers):
#   total = 0
#   for num in numbers:
#     total += num
#   return total

# print(my_function(1, 2, 3))
# print(my_function(10, 20, 30, 40))
# print(my_function(5))


# #  **Kwargs

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")



# #unpacking list 

# def my_function(a, b, c):
#   return a + b + c

# numbers = [1, 2, 3]
# result = my_function(*numbers) # Same as: my_function(1, 2, 3)
# print(result)

# #unpacking Dictionary

# def my_function(fname, lname):
#   print("Hello", fname, lname)

# person = {"fname": "Emil", "lname": "Refsnes"}
# my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

# x = "global"

# def outer():
#   x = "enclosing"
#   def inner():
#     x = "local"
#     print("Inner:", x)
#   inner()
#   print("Outer:", x)

# outer()
# print("Global:", x)


#decorator function

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# @changecase
# def otherfunction():
#   return "I am speed!"

# print(myfunction())
# print(otherfunction())

 # lambda function 

# x = lambda a : a + 10
# print(x(1))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))

# #map
# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x:x*2,numbers))
# print(doubled)

# #filter 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = list(filter(lambda x:x % 2 !=0 , numbers))
# print(odd_numbers)

#sorted
# students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
# sorted_student = sorted(students,key= lambda x:x[1])
# print(sorted_student)

#sort by str length
# words = ["apple", "pie", "banana", "cherry"]
# sorted_words = sorted(words, key=lambda x: len(x))
# print(sorted_words)


#recursion

# def countdown(x):
#     if x<=0:
#         print("Done")
#     else:
#         print(x)
#         countdown(x-1)

# countdown(4)

# def factorial(n):
#   # Base case
#   if n == 0 or n == 1:
#     return 1
#   # Recursive case
#   else:
#     return n * factorial(n - 1)

# print(factorial(5))


#fibonacci 0,1,1,2,3,5,8,13

# def fibonacci11(x):
#    if x<=1:
#     return x  
#    else:
#       return fibonacci11(x-1)+fibonacci11(x-2)


# print(fibonacci11(7))


# #recursion with list

# my_list=[1,2,3,4,5]

# def sum_list(n):
#   if len(n)==0:
#     return 0
#   else:
#     return 


#genertor

#fibonacci using generator

# def fibonacci():
#       a,b = 0,1
#       while True:
#             yield a
#             a,b = b,a+b

# #get first 100 numbers 

# gen = fibonacci()

# for i in range(10):
#       print(next(gen))




# def echo_generator():
#   while True:
#     received = yield
#     print("Received:", received)

# gen = echo_generator()
# next(gen) # Prime the generator
# gen.send("Hello")
# gen.send("World")


# def my_gen():
#   try:
#     yield 1
#     yield 2
#     yield 3
#   finally:
#     print("Generator closed")

# gen = my_gen()
# print(next(gen))
# gen.close()


# for i in range(10):
#   print(i)

# print(list(range(5)))
# print(list(range(1, 6)))
# print(list(range(5, 20, 3)))

# r = range(10)
# print(r[2])
# print(r[:3])

# # Print 0 through 5
# for i in range(6):
# 	print(i)

# # Print 2 through 5
# for i in range(2,6):
# 	print(i)

# # Create a list
# cars=["Ford","Volvo","BMW"]
# # Print the first item
# print(cars[0])
# # Change the second item to "Toyota"
# cars[1] = "Toyota"
# # Print the list
# print(cars)




#iterator 
# Create a tuple
# mytuple = ("apple","banana","cheery")
# # Create an iterator
# myit = iter(mytuple)
# # Print the first item
# print(next(myit))

# print(next(iter(mytuple)))



# # Import the platform module
# import platform
# # Print the system platform
# print(platform.system())

# import mymodule as mm

# print(mm.hellofun())


# import datetime 

# print(datetime.datetime.now())


# Import the datetime module
# import datetime
# # Store the current date and time in x
# x = datetime.datetime.now()
# # Print the year
# print(x.year)

# import math

# print(dir(math))

# # Print the lowest value
# print(min(5,10))
# # Print the highest value
# print(max(5,10))
# # Print the absolute value
# print(abs(-7.25))
# # Print 4 to the power of 3
# print(pow(4,3))


#json to python dictionary

# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])



# #dic to JSON

# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x,indent=4,separators=(" ","="),sort_keys=True))

# # Import json
# import json

# # Create a JSON string
# x = '{"name": "Emil", "age": 30}'

# # Parse the JSON string
# y = json.loads(x)

# # Print the age
# print(y["age"])



# import re

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

# import re

# txt = "The rain in Spain"
# x = re.findall("Portugal", txt)
# print(x)

# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start())

# import re

# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)

# import re

# #Split the string at every white-space character:

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)


import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


# Import re
import re
# Create a string
txt = "The rain in Spain"
# Search for "Spain"
x = re.search("Spain",txt)
# Print the span
print(x.span())
