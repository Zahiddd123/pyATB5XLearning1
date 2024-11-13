#Program - if age > 18 - allowed to vote
# else - not allowed to vote

user_age= int(input("Enter the age\n"))

# if user_age > 18:
#     print("Allowed to vote")
# else:
#     print("Not allowed to vote")


print("Allowed to vote" if user_age > 18 else "Not allowed to vote") #Using ternary operator here