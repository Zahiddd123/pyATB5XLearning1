class Car:

    def __init__(self):
        self.password= "password" # public instance variable
        self.__password_secure= "password12" # private instance variable

    def change_password(self):
        self.__password_secure="pass123"

obj= Car()
print(obj.password)
#print(obj.__password_secure)  # cannot access the private instance variable outside the class