#remove duplicate numbers from dictionary

my_dict = {"a": 10, "b": 20, "c": 10}

unique_dict = {}
seen_values = []

for key in my_dict:
    value = my_dict[key]
    if value not in seen_values:
        unique_dict[key] = value
        seen_values.append(value)

print("Dictionary after removing duplicates:", unique_dict)
