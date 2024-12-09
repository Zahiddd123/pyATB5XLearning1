a = 10 # Global variable

class Person:
    b= 11 # Instance variable:- Belong to class

    def print_info(self):
        c= 10 # local variable
        print(c) # we dont need self keyword for local variables
        print(self.b)
        # a="hello" # Local variable get more preference than global variable
        # print(a)
        global a # To access the global variable within the function
                    # we have to use "global" key word.
        print(a)


objec_ref= Person()
objec_ref.print_info()
objec_ref.print1()