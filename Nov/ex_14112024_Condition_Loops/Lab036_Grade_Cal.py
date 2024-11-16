# Grade calculator Program:
# Write a program that calculates  and displays the letter grade
# for a given  numerical  score (e.g.,A, B, C..)
# based on the following grading scale.

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# E: 50-59
# F: 0-59

#Logic building formula
#1. User Inputs -> score or marks -> int
#2. o/p letter grade(A, B, C) -> str

score= int(input("Enter the score\n"))

# Score >=90 and Score <=100 ->A

if score >=90 and score <=100:
    print("Your grade is ","A")
elif score >=80 and score<=89:
    print("Your grade is ","B")
elif score >= 70 and score <= 79:
    print("Your grade is ", "C")
elif score >= 60 and score <= 69:
    print("Your grade is ", "D")
elif  score >= 100: #and score <= -1:
    print("You are top of the world")
else:
    print("Your grade is ","F")