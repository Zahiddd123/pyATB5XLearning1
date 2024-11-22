# User defined functions:-

# 1.They can't have return/ -> non return
# 2.They can return something
# 3.They have parameter
# 4.They don't parameter/ non-parameter

# 1.They can't return (No return type and no parameter):-

def greet():
    print("Hello")

greet()

#2. No return type with argument/ Para.

def greet_by_name(name):
    print("Hello",  name.upper())

greet_by_name("Zahid")

#3. No return type with default(positional argument) parameter(argument)

def say_hello_def_para(name="ZAHID"): #default value
        print("Hello,", name)

say_hello_def_para("Rahul")
say_hello_def_para()

#Multiple argument
def multiple_arg(name1="A", name2="B"):
    print("Mul,",name1, name2)

multiple_arg()
multiple_arg("z","x")
multiple_arg(name1="c")
multiple_arg(name2="d")

#4. Argument + return type:

def sum_of_two(a, b):
    return a+b
result= sum_of_two(4, 6)
print(result)

# Sum of 2 no. with default value:-
def sum_of_2_num(a= 100, b= 200):
    return a+b
result= sum_of_2_num(30, 40)
print(result)
result= sum_of_2_num()
print(result)
