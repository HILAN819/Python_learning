
# anonymous function that can be passed in other functions
items = [('apple', 20),
         ('mango', 34),
         ('orange', 45),
         ('banana', 13)]
# lambda parameter: expression
items.sort(key=lambda item: item[1])
print(items)
items.append(('pawpaw', 67))
print(items)

# list comprehension
price = [item[1] for item in items]
print(price)

# prices = list(map(lambda item: item[1], items))
# print(prices)

