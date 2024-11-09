# 1. Write a program to  take the 2 user input
# 2. then sum the numbers
# 3. mul -> *
# 4. div -> /

# Logic building rule;-
#STEP-1
# Understand everything what user want don't assume anything(DAA)
# 1. I/P -> num1, num2 -> int
# 2. O/P -> sum -> int, mul -> int, div -> float

"""
num1 = input("Enter the num 1")
num2 = input("Enter the num 2") #the variable type here is str  we have to convert it to int
"""

# we can convert the str type to integer by 2 ways:-
# 1. num1 = int(num1)
# 2. num1= int(input(""))

num1 = int(input("Enter th num1 "))
num2 = int(input("Enter th num2 "))


#STEP-2 / Rough logic
# sum +, -, *, /

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("Sum is ",sum)
print("Sub is ",sub)
print("Mul is ",mul)
print("div is ",div)
