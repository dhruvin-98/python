
import pprint

count = int(input("Enter number of student : "))

student={}

for i in range(count):
    key = f"s{i+1}"
    rollno = int(input("Roll number :"))
    name = input("Name :")
    marks = int(input("Marks :"))
    grade = None


    student[key] = {

        "rollno":rollno,
        "name":name,
        "marks":marks,
        "grade":grade

    }

for i in student.values():
    marks = i["marks"]

    if marks >=90 and marks <=100:
        i["grade"] = "A"
    elif marks >=80:
        i["grade"] = "B"
    elif marks >=60:
        i["grade"] = "C"
    elif marks >=40:
        i["grade"] = "D"
    else:
        i["grade"] = "Fail"


pprint.pprint(student)
