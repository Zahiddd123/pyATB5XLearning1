# Sort a dictionary by its values in :-

# 1> Ascending order
# my_dict = {"a": 3, "b": 1, "c": 2}

# 2> Descending order
# my_dict = {"a": 3, "b": 1, "c": 2}

# 1> Ascending order:-

my_dict = {"a": 3, "b": 1, "c": 2}

sort_dic= dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Sorted dic -> ",sort_dic)

# 2> Descending order

my_dict1 = {"a": 3, "b": 1, "c": 2}

sort_dic1= dict(sorted(my_dict1.items(), key=lambda item: item[1], reverse= True))

print("Sorted dic -> ",sort_dic1)
