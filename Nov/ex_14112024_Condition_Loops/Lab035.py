#Program to find max between 3 numbers.

#Logic building formula
# 1. user input -> 3 integer
# 2. o/p -> int 1 which ever is greater max number  it will return or string with number.

#Rough logic

#SYNTAX of if-else condition:-
# if condition1:
#     print("do 1")
#     elif condition2:
#     print("do 2")
#     elif condition2:
#     print("do 3")
# else:
#     print("do for else")

num1= int(input("Enter the number\n")) #5
num2= int(input("Enter the number\n")) #3
num3= int(input("Enter the number\n")) #2

# condition 1: 5> 3 and 5> 2 -> 5
# num1> num2 and num1 > num3 -> num1
#
# condition 2: 3> 5 and 3> 2 -> 3
# num2> num1 and num2 > num3 -> num2
#
# condition 3: 2> 5 and 2> 3 -> 2
# num3> num1 and num3 > num2 -> num2

if num1 > num2 and num1> num3:
    print("MAX is ",num1)
elif num2 > num1 and num2 > num3:
    print("MAX is ",num2)
else:
    print("MAX is ",num3)
