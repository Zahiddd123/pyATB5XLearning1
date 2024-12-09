# Abstraction: Hide the details and show what is required.

# Eg:- Car - Keys-> Private, tyres-> Public

from abc import ABC, abstractmethod


class Father:

    def __init__(self, name ):
        self.name= name

    @abstractmethod
    def loan(self):
        pass

class Son(Father):
    def loan(self):
        print("1L loan given -> ",self.name)

obj_s= Son("Z")
obj_s.loan()