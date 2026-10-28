
def calculate(*lists):
    #combine all list 

    combined = [element for ls in lists for element in ls]

    print("\n combined list :",combined)


    #for 1 list
    if len(lists) == 1:
        print("List is :",lists[0])

    #for 2 lists
    elif len(lists) == 2:
        print("Maximum element is ",max(combined))
        print("Minimum element is ",min(combined))

    #for 3 lists
    elif len(lists) == 3:
        print("Aum of all element is :",sum(combined))



    #calculate square using lambda 
    square = lambda x: x ** 2
    squares = [square(x) for x in combined]
    print("Squares :",squares)

    #odd number
    odd_number = [x for x in combined if x%2 != 0]
    print("odd numbers are :",odd_number)



#input 

n = int(input("Enter number of list :"))

all_lists = []

for i in range(n):

    size = int(input(f"Enter the number of element for list {i+1}: "))

    ls=[]
    for j in range(size):
        element= int(input(f"element {j+1} is : "))
        ls.append(element)

    all_lists.append(ls)


#final call
calculate(*all_lists)