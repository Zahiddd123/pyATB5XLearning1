#Inner function can access/ use the variable of the outer function.

def outer_func():
    var1=30 #local # this variable is acting as global for the below 2 functions.

    def inner_func1():
        print(var1)
        var2= 90

    def inner_func2():
        print(var1)

    inner_func1()
    inner_func2()
    #print(var2) # we cannot access the inner func var2 outside the func.

outer_func()