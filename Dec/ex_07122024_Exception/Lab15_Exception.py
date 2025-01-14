# Exception in python are events that occur during the execution of  program that disrupt the
# normal flow of program
print("---Start the program")

try:
   a= int(input("Enter the num1 "))
   b= int(input("Enter the num2 "))
   c= a/ b

   print("Result ", c)

except Exception as e:
    print(e)

print("--End of the program")

# if we enter num1 = string then we will get "valueError exception"

# if enter num1 = 10 and num2= 0 then we will get "ZeroDivisionError"