#reverse a string

def reverse_string(name) :
    return name[::-1]

name = input("ENter your String :")
print(reverse_string(name))   


#character interchange

str1= "abcd"

print(str1.replace("a","d"))



# Interchange every two adjacent characters

def swap_pairs(text):
    result = ""

    for i in range(0, len(text) - 1, 2):
        result += text[i + 1] + text[i]

    if len(text) % 2 != 0:
        result += text[-1]

    return result


text = input("Enter your string: ")
print(swap_pairs(text))