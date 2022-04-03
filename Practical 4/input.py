import numpy as np
from domain.Students import *
from domain.Courses import *
from domain.Marks import *
from domain.GPA import *
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