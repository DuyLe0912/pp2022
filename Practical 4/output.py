from domain.Students import *
from domain.Courses import *
from domain.Marks import *
from domain.GPA import *
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

