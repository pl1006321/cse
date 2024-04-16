class Person:
    def __init__(self,fname,lname,age):
        # 3 types of varialbes u can create in init
        # by good programming conventions, all attributes should be private
        self.fname = fname # public variable!
        self._lname = lname # this makes it a protected variable
        self.__age = age # this makes it a private variable
        # priv variable -> never able to access from main method
        # public -> always able to access it directly from main
        # protected -> public, but if someone's reading your program, it'll tell you to use the private conventions to access it

    # accessor methods / getters
    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self._lname

    def get_age(self):
        return self.__age

     # mutator methods / setters
    def set_fname(self,fname):
        self.fname = fname

    def set_lname(self,lname):
        self._lname = lname

    def set_age(self,age):
        self.__age = age

    def greeting(self):
        return "hi i am a person!"

    def __str__(self):
        return f"First Name: {self.fname} {self._lname} Age: {self.__age}"

