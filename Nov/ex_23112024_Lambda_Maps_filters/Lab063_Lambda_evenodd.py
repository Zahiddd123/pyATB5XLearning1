# Write a program to calculate even and odd

#Type- 1

# def find_even_odd(num):
#     if num % 2 == 0:
#         print(num,"<= Num is even ")
#     else:
#         print(num,"<= Num is odd")
#
# find_even_odd(26)

chek_even_odd = lambda num: "Even" if num%2 == 0 else "Odd"
print(chek_even_odd(2))
