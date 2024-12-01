# Decorators in Python:-

# 1. We can add a annotation to the functions(to perform the extra task)

# 2.    e.g-> before running the function we want to do something (decorators)

# 3. Decorators are very powerful and flexible tool that allow us to modify the
# behaviour of the function or methods without changing the actual code.

# 4. Decorators are essentially functions that take another function  as an argument
#  and extend or alters its behaviour.

def add_extra_security(func):
    def wrapper():
        print("1. Before the function is called ")
        print("2. Add gloves, license")
        func()
        print("3. After the function is called ")
        print("4. Safe driving, leave all the items ")

    return wrapper()


@add_extra_security
def driving_scooty():
    print("Normal function")
    print("I am driving scooty")
