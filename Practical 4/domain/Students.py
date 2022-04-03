students = []

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