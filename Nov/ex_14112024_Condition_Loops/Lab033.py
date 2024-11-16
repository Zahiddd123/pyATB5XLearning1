#Write a  program  to make a user  age  and let him know if he can go  the club. 21

#Logic building formula

#STEP 1
#User input i/p-> data type -> int
#o/p -> String -> User if he can go club or not.

#STEP 2 Rough logic
# age > 21 -> print -"can go to club"
# age < 21 -> print -"cannot go to club"

#STEP 3 Write the logic
age=input("Enter the age\n")
age=int(input("Enter the age\n"))

if age > 21:
    print("can go to club")
else:
    print("cannot go to club")


#STEP 4 Check for the edge cases. (Where the code can break)
#We should consider the edge cases such as:
#Negative ages or extremely high values. -> Program will break
#Non-numeric input-ABC
#Age which is valid. > 130


#STEP 5  Optimize the code
#Handle all the edge cases



