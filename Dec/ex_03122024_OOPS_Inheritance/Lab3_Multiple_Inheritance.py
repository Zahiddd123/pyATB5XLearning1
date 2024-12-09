from Dec.ex_03122024_OOPS_Inheritance.Lab1_Single_Inheritance import Obj_s


class Father():

    def father_money(self):
        return 10

    def home(self):
        print("Father home")

class Mummy():

    def mommy_money(self):
        return 5

    def home(self):
        print("Mummy's home")

class Son(Father, Mummy): # Multiple Inheritance

     def son_inf(self):
         print("Son")

obj_son= Son()
print(obj_son.mommy_money() + obj_son.father_money())
obj_son.home()