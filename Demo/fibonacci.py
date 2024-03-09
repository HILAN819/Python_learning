# x, y = 0, 1
# while y < 50:
#     print(y)
#     x, y = y, x+y

for i in range(1, 16):
    if not i % 3 and not i % 5:
        print("fizzbuzz")
    elif not i % 3:
        print("buzz")
    elif not i % 5:
        print("fizz") 
    else:
        print(i)