#BI11-069 Le Tran Khuong Duy
#Practical work 3
import numpy as np
class student:
    def __init__(self,id,name,dob):
        self.__id=id
        self.__name=name
        self.__dob=dob
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def __str__(self):
        return f"Student ID: {self.__id}\nStudent Name: {self.__name}\nStudent DOB:{self.__dob}"

class course:
    def __init__(self,id,name,credit):
        self.__id=id
        self.__name=name
        self.__credit=credit
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credit(self):
        return self.__credit
    def __str__(self):
        return f"Course ID: {self.__id}\nCourse Name: {self.__name}\nCourse Credit: {self.__credit}"

class mark:
    def __init__(self,std_id,crs_id,grade):
        self.__std_id=std_id
        self.__crs_id=crs_id
        self.__grade=grade
    def get_std_id(self):
        return self.__std_id
    def get_crs_id(self):
        return self.__crs_id
    def get_grade(self):
        return self.__grade

class gpa:
    def __init__(self,std_id,gpa_val):
        self.__std_id=std_id
        self.gpa_val=gpa_val
    def get_std_id(self):
        return self.__std_id
    def get_gpa(self):
        return self.gpa_val
    def __str__(self):
        return (f"Student ID: {self.__std_id} / GPA: {self.gpa_val}")


#Lists
students = []
courses = []
marks = []
GPA = []

#Input functions
def studentsNum():
    stdnum = int(input("Enter number of students in class: "))
    return stdnum

def studentInfoInput(student_order):
    id = input(f"Enter student #{student_order} id: ")
    name = input(f"Enter student #{student_order} name: ")
    dob = input(f"Enter student #{student_order} date of birth: ")
    stdInfo = student(id,name,dob)
    students.append(stdInfo)

def coursesNum():
    crsnum = int(input("Enter number of courses: "))
    return crsnum

def courseInfoInput(course_order):
    id = input(f"Enter course #{course_order} id: ")
    name = input(f"Enter course #{course_order} name: ")
    credit = int(input(f"Enter course #{course_order} credit: "))
    crsInfo = course(id,name,credit)
    courses.append(crsInfo)

def marking_process():
    print("------Marking------")
    for i in courses:
        while 1:
            crsId = input("Enter course id: ")
            crsIDList = [crs_Id.get_id() for crs_Id in courses]
            if crsId in crsIDList:
                for j in students:
                    while 1:
                        stdID = input("Enter student id: ")
                        stdIDList = [std_Id.get_id() for std_Id in students]
                        if stdID in stdIDList:
                            grade = float(input("Enter mark: "))
                            grade = round(grade,1)
                            mrk = mark(stdID,crsId,grade)
                            marks.append(mrk)
                            break
                        else:
                            print("No matches! Try again.")
                break
            else:
                print("No matches! Try again.")

def calculate_GPA():
    grade=np.array(marks)
    cred=np.array(courses)
    for i in students:
        total_mark = 0
        total_credit = 0
        for j in grade:
            if j.get_std_id() == i.get_id():
                total_mark = total_mark + j.get_grade()
                for k in cred:
                    if j.get_crs_id() == k.get_id():
                        total_credit = total_credit + k.get_credit()
        id = i.get_id()
        gpa_val = total_mark/total_credit
        std_gpa = gpa(id,gpa_val)
        GPA.append(std_gpa)



#Ouput funstions
def displayStudents():
    print("---------------- Students List -----------------")
    student_order = 1
    for i in students:
        print(f"{student_order}.")
        print(i)
        print("******")
        student_order+=1

def displayCourses():
    print("---------------- Courses List ------------------")
    course_order = 1
    for i in courses:
        print(f"{course_order}.")
        print(i)
        print("******")
        course_order+=1

def displayMarks():
    print("---------------- Mark List --------------------")
    for i in courses:
        print(f"\tCourse ID: {i.get_id()}")
        for k in range(0,len(marks)):
            if(marks[k].get_crs_id() == i.get_id()):
                print(f"Student ID: {marks[k].get_std_id()}  /  Mark: {marks[k].get_grade()}")

def displayGPA():
    print("---------------- GPA List ---------------------")
    for i in GPA:
        print(i)


#main
print("--------- Student Mark Management --------\n")
stdnum = int(studentsNum())
for i in range(0,stdnum):
    studentInfoInput(i+1)
crsnum = int(coursesNum())
for i in range(0,crsnum):
    courseInfoInput(i+1)
marking_process()

while 1:
    print("--------- Class Info Display --------")
    print("1.Display all students")
    print("2.Display all courses")
    print("3.Display marks")
    print("4.Display GPA in descending order")
    print("5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        displayStudents()
    elif choice == 2:
        displayCourses()
    elif choice == 3:
        displayMarks()
    elif choice == 4:
        calculate_GPA()
        GPA.sort(key=lambda x: x.gpa_val, reverse=True)
        displayGPA()
    elif choice == 5:
        exit_choice = input("Do you want to exit? [Y/N]: ")
        if exit_choice.upper() == "Y" or exit_choice.upper() == "YES":
            break
        else:
            pass
    else:
        print("Invalid input! Try again. \n")




