# Task 1 for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

# 1> Take 2 input from the user
num1= int(input("Enter the num1\n"))
num2= int(input("Enter the num2\n"))

# 2> Quotient is obtained by using true division (//) operator
# 3> Remainder is obtained using modulus (%) operator when num1 is divide by num2
Quotient= num1 // num2
remainder= num1 % num2
print("Quotient of num1 and num2 is  ",Quotient)
print("remainder of num1 and num2 is  ",remainder)
