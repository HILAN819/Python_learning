point = {"x": 2, "y": 3, "z": 5}
print("point: ", point)
# option 2 to write a dictionary
values = dict(a=4, b=7, c=9)
print("values: ", values)

# iteration
new_values = []
for key in values:
    # print(key, values[key])
    new_values.append(values[key]*2)

print("New values: ", new_values)
new_values = set(new_values)
print("set_new_values", new_values)

# Dictionary Comprehension
numbers = {x: x * 3 for x in range(10)}
print(numbers)
