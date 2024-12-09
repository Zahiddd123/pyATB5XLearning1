# Polymorphism:- Allows objects of different classes to be treated as object
#                of a common superclass
# A object can have many forms

# We have 2 different type of ploy.:-

# Method overloading- We can have multiple functions with same name but diff arguments.
#                      By default python doesn't support direct method over loading concept.

# Python does not support method overloading in traditionally sense

class calc: # Not supported traditionally in python without the default parameter

    def sum(self, a, b):
        return a*b

    def sum(self, a, b, c=1):
        return a+b+c

obj= calc()
r=obj.sum(1,2)
print(r)
# **Important**

# Method overloading is only supported with default parameters

# Method overriding- We can override the methods of parents