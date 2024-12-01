# List- Collection of items (duplicates are allowed, multiple diff. data type are allowed)

my_list= [1, 2, 3]
my_list1= [1, 2, "xyz", True]

print(my_list)
print(len(my_list))
print(my_list1[0])
print(my_list1[2])

#We can Re-assign the value
my_list1[2]="zzz"
print(my_list1)