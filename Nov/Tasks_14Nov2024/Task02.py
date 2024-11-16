#Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

#Logic builder formula
# i/p-> 3(s1, s2, s3) -> datatype-> int
#o/p-> str.

s1=int(input("Enter the length of the s1\n"))
s2=int(input("Enter the length of the s2\n"))
s3=int(input("Enter the length of the s3\n"))

#Rough logic
# if s1 == s2 == s3 -> Equilateral
# elif s1 == s2 or s1 == s3 or s2 ==s3 -> Isosceles
#else -> Scalene

if s1 == s2 == s3:
    print("The triangle is","Equilateral")
elif s1 == s2 or s1 == s3 or s2 ==s3:
    print("The triangle is", "Isosceles")
else:
    print("The triangle is", "Scalene")