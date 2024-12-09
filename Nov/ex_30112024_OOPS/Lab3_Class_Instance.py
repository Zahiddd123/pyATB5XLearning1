class Person:
    def __init__(self, name):
        # print(
        #     "I am called ")
        self.name=name

    def walk(self):
        return self.name

Akif= Person("Akif")
print(Akif.name)
print("WHO IS WALKING -> ",Akif.walk())

Zoro= Person("Zoro")
print(Zoro.name)
print("WHO IS WALKING -> ",Zoro.walk())