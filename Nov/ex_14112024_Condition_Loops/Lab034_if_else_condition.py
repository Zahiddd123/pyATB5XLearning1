#Problem to find max between 2 numbers.

#Logic building formula
#STEP-1
# 1. user input -> 2 integer
# 2. o/p -> int 1 which ever is greater max number  it will return.
# 31.4 -> float

num1=float(input("Enter the number\n"))
num2=float(input("Enter the number\n"))

if num1 >=  num2:
    print("MAX is",num1)
else:
    print("MAX is",num2)

#Edge cases:-
#1.If num1 == num2-- Handled
#String- ABC, ten. -> Handle by try and catch(In future)
#-ve values
