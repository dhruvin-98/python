val = input("Enter your input :")
str_list = []
int_list=[]


sep_val = val.split(",")

for i in sep_val:
    try:
        one=int(i.strip())
        int_list.append(one)
    except:
        str_list.append(i.strip())

reversed_list = str_list[::-1]
print(reversed_list)

print(min(int_list))
print(max(int_list))

    
