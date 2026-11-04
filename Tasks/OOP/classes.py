class Main:
 
        
    class StudentInfo:
        def __init__(self,student_rollno,student_name):
            self.student_rollno = student_rollno
            self.student_name = student_name


    class StudentMarks:
        def __init__(self,student_rollno,student_marks_one,student_marks_two,student_marks_three):
            self.student_marks_one = student_marks_one
            self.student_marks_two =student_marks_two
            self.student_marks_three = student_marks_three
            self.student_rollno = student_rollno

    def grade_fun(self,avg_marks):
        if avg_marks > 100:
            return "Invalid marks"
        elif avg_marks >= 90:
            return "A Grade"
        elif avg_marks >= 80:
            return "B Grade"
        elif avg_marks >= 60:
            return "C Grade"
        elif avg_marks >= 40:
            return "D Grade"
        else:
            return "Fail"

    def run(self):
            num = int(input("Enter Number of students : "))
    
            for n in range(num):   
                
                student_rollno = int(input("Roll no: "))
                student_name = input("Name :")
                student_marks_one = int(input("Subject 1 Marks :"))
                student_marks_two = int(input("Subject 2 Marks :"))
                student_marks_three = int(input("Subject 3 Marks :"))
    
                info = self.StudentInfo(student_rollno,student_name)
                marks = self.StudentMarks(student_rollno,student_marks_one,student_marks_two,student_marks_three)

                avg_marks = (student_marks_one+student_marks_two+student_marks_three)/3
                grade =self.grade_fun(avg_marks)

                print(f"Name: {info.student_name}")
                print(f"Roll no: {info.student_rollno}")
                print(f"Average: {avg_marks:.2f}")
                print(f"Grade: {grade}")
            
Main().run()
    
    

