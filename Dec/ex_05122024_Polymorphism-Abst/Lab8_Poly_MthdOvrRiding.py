# Method OverRiding- Over riding the parent funct./ Method.

class Father:

    def home(self):
        print("2bhk")

class Son(Father):

    def town(self):
        print("10  bhk")

    def home(self): # Overrides the father method
        print("3 bhk")

obj= Son()
obj.home()