try:
    num1= int(input("Enter the num 1\n ")) # if try block is ok interpreter
                                           # go to else block or go to except block
    num2= int(input("Enter the num 2\n "))
    result= num1/ num2
except ValueError as e: # If you know the exception good practice that you
                        # should add that instead of using "Exception"
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("Output is ",result)

finally: #This code will always executed
    print("This code will always executed ")


# try:
#     num1= int(input("Enter the num 1\n "))
#     num2= int(input("Enter the num 2\n "))
#     result= num1/ num2
# except Exception as e:
#     print(e)



