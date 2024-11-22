# * args -> used for unlimited arguments

def print_mult_arguments(*args):
    for i in args:
        print(i)

    print_mult_arguments("x")
    print_mult_arguments("x", "y", 3, 4)