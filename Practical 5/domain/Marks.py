marks = []

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