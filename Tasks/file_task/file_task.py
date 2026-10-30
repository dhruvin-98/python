num_of_student = int(input("Enter number of students: "))

def write_data(num_of_student):  

    students=[]
    marks=[]
    avg=[]
    for i in range(num_of_student):
        roll_no=int(input(f"Enter roll number of student {i+1} :"))
        name=input(f"Enter name of student {i+1} :")
        students.append((roll_no,name))

        subject1=int(input("mark of subject 1 :"))
        subject2=int(input("mark of subject 2 :"))
        subject3=int(input("mark of subject 3 :"))
        average=int(subject1+subject2+subject3)/3
        marks.append((roll_no,subject1,subject2,subject3))
        avg.append((roll_no,name,average))

    with open("studentInfo.txt","w") as file:
        for roll_no,name in students:
            file.write(f"{roll_no}-{name}\n")  

    with open("studentMarks.txt","w") as file:
            for roll_no,subject1,subject2,subject3 in marks:
                file.write(f"{roll_no}-{subject1}-{subject2}-{subject3}\n")

    #grade calculate

    for roll_no,name,average in avg:
        if 80<=average<=100:
              with open("Agrade.txt","a") as file:
                file.write(f"{roll_no}-{name}-{average}\n")
        elif 60<=average<80:
              with open("Bgrade.txt","a") as file:
                file.write(f"{roll_no}-{name}-{average}\n")
        elif 40<=average<60:
              with open("Cgrade.txt","a") as file:
                file.write(f"{roll_no}-{name}-{average}\n")
        else:
            pass

write_data(num_of_student)
        


