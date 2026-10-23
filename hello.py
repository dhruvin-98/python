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





from numbers import Real

def preprocess(config, features):
    if not isinstance(config, dict):
        raise TypeError("config must be a dictionary")

    if not isinstance(features, list):
        raise TypeError("features must be a list")

    multiplier = config.get("multiplier", 1)

    if (
        isinstance(multiplier, bool)
        or not isinstance(multiplier, Real)
    ):
        raise TypeError("multiplier must be a real number")

    if any(
        isinstance(value, bool) or not isinstance(value, Real)
        for value in features
    ):
        raise TypeError("all features must be real numbers")

    processed_features = [
        value * multiplier for value in features
    ]

    effective_config = config.copy()

    return processed_features, effective_config


config = {"multiplier": 2}
features = [1, 2, 3]

processed, effective_config = preprocess(config, features)

print(processed)
print(effective_config)
print(features)
print(config)

#sss