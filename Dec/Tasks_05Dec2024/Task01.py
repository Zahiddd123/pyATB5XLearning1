from abc import ABC,abstractmethod


class PC:
    def __init__(self):
        print("PC ready to GO--")


class MotherBoard(ABC):

    @abstractmethod
    def start_Motherboard(self):
      pass  # print("starting motherboard")

class RAM(ABC):

     @abstractmethod
     def start_ram(self):
         pass

class Processor(ABC):

    @abstractmethod
    def start_processor(self):
        pass

class Storage(ABC):

    @abstractmethod
    def storage_data(self):
        pass

    @staticmethod
    def loadOS():
        print("Operating System loaded")
        
    def startMouse(self):
        print("Mouse started")

    def useHeadPhone(self):
        print("Headphones connected")

class CommandPC(ABC):

    def start_Motherboard(self):
        print("MotherBoard started")

    def start_ram(self):
        print("RAM started")

    def start_processor(self):
        print("RAM started")

    def storage_data(self):
        print("Total storage data of PC is 500 GB ")

    def command_pc(self):
        self.start_Motherboard()
        self.start_ram()
        self.start_processor()
        self.storage_data()
        Storage.loadOS()  # Called static method using class name
        print("Command your pc as per requirement now--->")

obj_C= CommandPC()
obj_C.command_pc()


