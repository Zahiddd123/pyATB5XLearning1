class Person:
    def __init__(self, name):
        # print(
        #     "I am called ")
        self.name=name

    def walk(self):
        return self.name

Obj1= Person("Akif")
print(Obj1.name)
print("WHO IS WALKING -> ",Obj1.walk())

Obj2= Person("Zoro")
print(Obj2.name)
print("WHO IS WALKING -> ",Obj2.walk())