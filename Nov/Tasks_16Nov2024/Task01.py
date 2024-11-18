# Write a program that prints numbers from 1 to 100. However,
# for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzBuzz."

#Logic building formula
#o/p - > str

#Rough logic :-
#for num in range(1, 101)
#if num % 3 == 0 -> "fizz"
#elif num % 5 == 0 -> "Buzz"
#elif num % 3 == 0 and num % 5 == 0 -> "FizzBuzz"

for num in range(1, 101):
    if num % 3 == 0: # check num is multiple of 3
        print("Fizz")
    elif num % 5 == 0: # check the num is multiple of 5
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0: # check the num is multiple of both 3 and 5
        print("FizzBuzz")
    else:
        print(num)