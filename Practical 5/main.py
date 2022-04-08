import os
from zipfile import ZipFile

from input import *
from output import *
#main
if os.path.isfile('students.dat'):
    zip_file = ZipFile('students.dat', 'r')
    zip_file.extractall()
    if os.path.isfile('Students.txt'):
        f = open('Students.txt', 'r')
        print(f.read())
        f.close()
    if os.path.isfile('Courses.txt'):
        f = open('Courses.txt', 'r')
        print(f.read())
        f.close()
    if os.path.isfile('Marks.txt'):
        f = open('Marks.txt', 'r')
        print(f.read())
        f.close()
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
            file_list = ['Students.txt', 'Courses.txt', 'Marks.txt']
            with ZipFile('students.dat', 'w') as new_zip:
                for file_Name in file_list:
                    new_zip.write(file_Name)
                for file_Name in file_list:
                    os.remove(file_Name)
            break
        else:
            pass
    else:
        print("Invalid input! Try again. \n")