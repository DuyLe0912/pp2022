GPA = []

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