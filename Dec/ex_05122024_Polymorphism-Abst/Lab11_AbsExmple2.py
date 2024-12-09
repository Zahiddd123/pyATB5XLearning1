from abc import ABC, abstractmethod


class GearBox(ABC):

    @abstractmethod
    def set_gearbox(self):
        pass

class Engine(GearBox):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine):

    def start(self):
        super().start()
        print("Start the car")

    def stop(self):
        print("Stop the car")

    def set_gearbox(self):
        print("GearBox is ready ")

    def drive(self):
        
        self.start()
        self.stop()
        self.set_gearbox()

obj_C= Car()
obj_C.drive()

