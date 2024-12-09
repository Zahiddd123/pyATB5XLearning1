#Class, object, constructor

class Dog:
    #Attibute
    name= None
    breed= None

    def __init__(self,name,breed): # "__init__" act as a construtor here to inetialize
                                   # the value in object, it called when object is created.
         print("PC")
         self.name=name
         self.breed=breed

    #Behaviour
    def bark(self):
        print("Who is barking ->"+self.name)

    def eat(self):
        print("Who is Eating ->"+self.name)

    #Object ref

tyson_ref= Dog("tyson","bully")
print("My dog name is -> "+tyson_ref.name)
tyson_ref.bark()
    #Dog() -> Object
    #Tyson -> Ref
bow_ref= Dog("bow","husky")
print(bow_ref.name)
print("My dog breed name is -> "+bow_ref.breed)
bow_ref.eat()
