#Write a python program to get the max and min values of a dictionary

my_dict = {"a": 10, "b": 25, "c": 5}

first_key = next(iter(my_dict))
min_val = my_dict[first_key]
max_val = my_dict[first_key]


for key in my_dict:
    value = my_dict[key]
    if value < min_val:
        min_val = value
    if value > max_val:
        max_val = value

print("Minimum Value:", min_val)
print("Maximum Value:", max_val)