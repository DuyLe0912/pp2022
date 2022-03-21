#BI11-069 Le Tran Khuong Duy
#Practical work 2
class student:
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob
    def __str__(self):
        return f"Student ID: {self.id}\nStudent Name: {self.name}\nStudent DOB:{self.dob}"

class course:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __str__(self):
        return f"Course ID: {self.id}\nCourse Name: {self.name}"

class mark:
    def __init__(self,std_id,crs_id,grade):
        self.std_id=std_id
        self.crs_id=crs_id
        self.grade=grade

#Lists of dictionaries
students = []
courses = []
marks = []

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
    crsInfo = course(id,name)
    courses.append(crsInfo)

def marking_process():
    print("------Marking------")
    for i in courses:
        while 1:
            crsId = input("Enter course id: ")
            crsIDList = [crs_Id.id for crs_Id in courses]
            if crsId in crsIDList:
                for j in students:
                    while 1:
                        stdID = input("Enter student id: ")
                        stdIDList = [std_Id.id for std_Id in students]
                        if stdID in stdIDList:
                            grade = float(input("Enter mark: "))
                            mrk = mark(stdID,crsId,grade)
                            marks.append(mrk)
                            break
                        else:
                            print("No matches! Try again.")
                break
            else:
                print("No matches! Try again.")


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
        print(f"\tCourse ID: {i.id}")
        for k in range(0,len(marks)):
            if(marks[k].crs_id == i.id):
                print(f"Student ID: {marks[k].std_id}  /  Mark: {marks[k].grade}")

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
    print("4.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        displayStudents()
    elif choice == 2:
        displayCourses()
    elif choice == 3:
        displayMarks()
    elif choice == 4:
        exit_choice = input("Do you want to exit? [Y/N]: ")
        if exit_choice.upper() == "Y" or exit_choice.upper() == "YES":
            break
        else:
            pass
    else:
        print("Invalid input! Try again. \n")




