# Hierarchical Inheritance

class Father: # One parent multiple child

    def bhk1(self):
        print("1 bhk")

class Son(Father):

     def bhk2(self):
         print(" 2 bhk")

class Son2(Father):

    def no_flat(self):
        print("nO FLAT ")

obj_s= Son()
obj_s.bhk1()

obj_s2= Son2()
obj_s2.bhk1()
obj_s2.no_flat()