# Write a program  to sum of three number from the user input,
# if user doest n't enter any number, user default as 100, 200, 300

#Logic building formula:-
#i/p -> int, o/p -> int

num1= int(input("Enter the num1\n"))
num2= int(input("Enter the num2\n"))
num3= int(input("Enter the num3\n"))

def sun_of_3_num(num1=100, num2=200, num3=300):
    return num1+num2+num3

result= sun_of_3_num(num1, num2, num3)
print("Sum of 3 num ",result)

result= sun_of_3_num(10,20)
print("Sum of 3 num ",result)

result= sun_of_3_num()
print("Sum of 3 num using default values ",result)

