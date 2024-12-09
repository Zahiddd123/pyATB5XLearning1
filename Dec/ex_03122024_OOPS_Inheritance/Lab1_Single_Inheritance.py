# Single Inheritance- 85% of the time we will use SI in API, web automation

# Inheritance- Is a basic fundamental of OOPS concept according to which
#           child class can access/ Inherit the attributes, methods, func. of the parent class.


class Father():
    key= "2bhk"

    def car(self):
        print("My father have Alto car")
        print(self.key)

class Son(Father):
    key2 = "1 bhk"

    def son_car(self):
        print("Son have SUV car")


Obj_f= Father()
Obj_f.car()

Obj_s= Son()
Obj_s.car() # Here we are accessing the father class method
            # in son class using single inheritance.