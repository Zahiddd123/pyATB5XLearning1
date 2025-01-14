# Encapsulation:-
# Binding the data variable within the method (Def function within the class).

class Car:
    def __init__(self, c_name, c_color, c_model):
        self.name= c_name
        self.color= c_color
        self.model= c_model

    def car_start(self):
        print("Starting the car with name  -> " +self.name)
        print("Starting the car with color  -> "+self.color)
        print("Starting the car with model  -> "+self.model)

Audi= Car("Audi","Blue","2024")
Audi.car_start()

Mersadeez= Car("Mersadeez", "Blue", "2023")
Mersadeez.car_start()

