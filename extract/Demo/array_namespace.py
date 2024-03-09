import array
array_func = []
count = 0
for name in array.__dict__:
    array_func.append(name)
    count += 1

print("Namespaces in array: /n", sorted(array_func))
print(count)
