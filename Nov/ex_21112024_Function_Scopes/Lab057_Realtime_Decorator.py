import time


def time_decorator(func):
    def wrapper():
        start_time=time.time()
        print(start_time)
        func()
        end_time=time.time()
        print(end_time)
        print("Total time take by the func ",end_time-start_time)

    return wrapper()


@time_decorator #executes 1st

def  test_ui_1():
    print("Add a function, time take by this function 1")
    time.sleep(2)



@time_decorator
def  test_ui_2():
    print("Add a function, time take by this function 2")
    time.sleep(5) #use to make interpreter wait for 5 sec
