# Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.

#Logic building formula
#i/p -> year(int)
#o/p -> str

year=int(input("Enter the year\n"))

#Rough logic
#if year % 4 == 0 and year != 100 or year % 400 == 0 -> "Is a leap year".
if year % 4 == 0 and year != 100 or year % 400 == 0:
    print(year,"is the leap year")
else:
    print("Not the leap year")