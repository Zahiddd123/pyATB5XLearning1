# my_dic= {
#     "name" : "xyz",
#     "age": 30,
#      "exp" : "4"}
#
# print(my_dic)
# print(my_dic["age"])
#
# my_dic["name"]= "abc"
# print(my_dic)
#
# del my_dic["age"]
# print(my_dic)
#
# for key,value in my_dic.items():
#     print(key,value)
#
# print("name" in my_dic)

# Check if two dictionaries are equal

# dic1= {"a": 1, "b": 2, "c":3}
# dic2= {"b": 2, "a": 1, "c":3}
#
# print(dic1 == dic2)

# Write a program to remove the duplicate value from the dic.

# my_dict= {"a": 1, "b": 2, "c":1, "d": 6}
#
# unique_value= set()
#
# result = {}
#
# for key, value in my_dict.items():
#     if value not in unique_value:
#         result[key]= value
#         unique_value.add(value)
#
# print(unique_value)

# Write a program to print number of vowels a string contains.

input_string= "hello world"

vowels= "aeiou"
vowels_count= 0
char_name="Vowel char ->"

for char in input_string:
    if char in vowels:
        vowels_count= vowels_count+1
        print("The vowel chars -> ",char)
print(vowels_count)

