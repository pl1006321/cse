from person import *

class Student(Person):
    def __init__(self,fname,lname,age,id):
        super().__init__(fname,lname,age)
        self.__id = id
        # if inheriting, super must come first before initializing extra attributes

    def get_id(self):
        return self.__id

    def set_id(self,id):
        self.__id = id

    def __str__(self):
        return f"Student: {self.fname} {self._lname} Age: {self.get_age()} ID: {self.__id}"