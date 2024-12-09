# Static method- A static method is a method that belongs to a class
#                rather than an instance of the class.



# A static method/ func can be call without making an object as
# compare to tbe normal method/ func

# Identify static method- If we are abl to use the func/ method
#                         using class name then it is a SM.

class O:

    @staticmethod
    def sum(a,b):
        return (a+b)

    def sub(self, a, b):
        return (a-b)

    print("sum ",sum(3, 4)) # Using static method without obj

obj_o= O()
result=obj_o.sub(3,1)
print("Sub ",result) # Non static method



