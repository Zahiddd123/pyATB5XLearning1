# Hybrid Inheritance

# multiple type of inheritance :-
# Single inheritance
# multiple and multi-level inheritance

class Father1: # One parent multiple child

        def bb1(self):
         print("bb1")

class Son(Father1):

     def bhk12(self):
         print("12 bhk")

class Son2(Father1):

    def no_flat1(self):
        print("nO FLAT ")

class Son3(Son, Son2):

     def son3_inf(self):
        print("son3")
        self.bb1()


obj_s3= Son3()
obj_s3.son3_inf()