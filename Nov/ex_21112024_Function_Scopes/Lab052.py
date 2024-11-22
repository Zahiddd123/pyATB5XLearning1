# Global variable

pb_global_b= 20

def my_function():
    pb_a= 10 # Local variable within the function
    print(pb_a)
    print(pb_global_b)

# print(pb_a) #cann't use local variable outside the function as name "pb_a" is not defined
print(pb_global_b) # can use global variable
my_function()