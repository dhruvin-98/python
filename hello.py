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





training_data = [10, 20, 30]

def normalize(data):
    data[0] = 0
    return data

normalized_data = normalize(training_data)

print(training_data)
print(normalized_data)
print(training_data is normalized_data)

