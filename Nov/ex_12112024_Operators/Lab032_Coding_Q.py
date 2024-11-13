#Write a program to calculate the area of te circle given
#its radius using the formula ----area= pir*r**2---(Take pie as 3.14).

#logic building formula

# STEP- 1
#figure out the input and output
#input -> r -> datatype -> float
#pie= 3.14
#power -> pow or ** -> any
# o/p -> float - area, print area

#STEP 2
#Rough logic = 3.14 * pow(r**2)

radius= float(input("Enter the radius of the circle\n"))
print(radius)
Area= 3.14 * (radius**2)
print("Area of the circle ->",Area)
print(f"Area of the circle: {Area:.2f}") #f used to print the number after the decimal "."