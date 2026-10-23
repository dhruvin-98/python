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



x = 10
y = 25

print(x/y) #returns float
print(x//y) #returns integer