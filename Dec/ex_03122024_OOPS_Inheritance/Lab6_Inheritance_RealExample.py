

class BaseTestcase:

    def open_browser(self):
        print("Open brower ")

    def read_from_excell(self):
        print("Read from exell")

    def close_browser(self):
        print("close browser")

class Testcase1(BaseTestcase):

    def positive_testcase(self):
        self.open_browser()
        print("Test case P1 Executed ")
        self.close_browser()

    def negative_testcase(self):
        self.open_browser()
        print("Test case N1 Executed ")
        self.close_browser()

class Testcase2(BaseTestcase):

    def Testcase_2(self):
        self.open_browser()
        print("Testcase2  Executed ")
        self.close_browser()

obj_test2= Testcase2()
obj_test2.read_from_excell()