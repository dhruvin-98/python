# Write a Python program where the user chooses how many lists to enter.

# For each list, ask how many numbers it contains, then ask for the numbers.

# Create a function analyze(*lists) that:
# - With one list, prints that list.
# - With two lists, joins them and prints the largest and smallest numbers.
# - With three lists, joins them and prints the sum of all the numbers.
# - With any number of lists, uses a single-line list comprehension to join them, then uses lambda to:
#   - create and print a list of each number doubled
#   - create and print a list of the even numbers



number_of_lists = int(input("How many list you want to enter ? : "))

lists=[]

for i in range(number_of_lists):
        count = int(input(f"How many numbers for list {i+1} : "))
        values=[]

        for j in range(count):
                value=int(input(f"Enter element {j+1} for list {i+1} :"))
                values.append(value)

        lists.append(values)


def analyze(*lists):

        combined = [item for ls in lists for item in ls]
        print("Combined list is :",combined)
        
        if len(lists) == 1:
                print(lists[0])

        elif len(lists) == 2:
                print("Largest number is :",max(combined))
                print("Smallest number is :",min(combined))

        elif len(lists) == 3:
                print("Sum of alll the numbers is :",sum(combined))

        #lambda function
        doubled = list(map(lambda x : x**2,combined))
        even_numbers = list(filter(lambda x : x % 2 == 0,combined))

        print("List of doubled numbers  is :",doubled)
        print("List of even numbers is :",even_numbers)


analyze(*lists)