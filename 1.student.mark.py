#BI11-069 Le Tran Khuong Duy
#Practical work 1

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
    stdInfo = {'id':id,'name':name,'DOB':dob}
    students.append(stdInfo)

def coursesNum():
    crsnum = int(input("Enter number of courses: "))
    return crsnum

def courseInfoInput(course_order):
    id = input(f"Enter course #{course_order} id: ")
    name = input(f"Enter course #{course_order} name: ")
    crsInfo = {'id':id,'name':name}
    courses.append(crsInfo)

def marking_process():
    print("------Marking------")
    for i in courses:
        while 1:
            crsId = input("Enter course id: ")
            crsIDList = [crs_Id["id"] for crs_Id in courses]
            if crsId in crsIDList:
                for j in students:
                    while 1:
                        stdID = input("Enter student id: ")
                        stdIDList = [std_Id["id"] for std_Id in students]
                        if stdID in stdIDList:
                            mark = float(input("Enter mark: "))
                            mrk = {'Student ID':stdID,'Course ID':crsId,'Mark':mark}
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
        print("******")
        print(f"{student_order}.")
        print(f"Student ID: {i.get('id')}\nStudent name: {i.get('name')}\nDate of birth: {i.get('DOB')}")
        print("******")
        student_order+=1

def displayCourses():
    print("---------------- Courses List ------------------")
    course_order = 1
    for i in courses:
        print("******")
        print(f"{course_order}.")
        print(f"Course ID: {i.get('id')}\nCourse name: {i.get('name')}")
        print("******")
        course_order+=1

def displayMarks():
    for i in marks:
        print("******")
        print(f"Student ID: {i.get('Student ID')}\nCourse ID: {i.get('Course ID')}\nMark: {i.get('Mark')}")
        print("******")

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




