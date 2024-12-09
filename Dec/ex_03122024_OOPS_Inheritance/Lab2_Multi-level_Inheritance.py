# Multi-Level Inheritance
# GF -> F -> S

class GrandFather:
    gold= "2 kg"

    def bhk1(self):
        print("bhk1")

class Father(GrandFather):
     _car= "3 Cars"

     def bhk2(self):
         print("2bhk")

class Son(Father):
    cycle= "2 cycle"

    def bhk3(self):
        print("3 bhk")

obj_GF= GrandFather()
obj_GF.bhk1()
print(obj_GF.gold)

obj_F= Father()
obj_F.bhk1()
print(obj_F._car)

obj_s= Son()
obj_s.bhk2()
print(obj_s._car)
obj_s.bhk3()
obj_s.bhk1()