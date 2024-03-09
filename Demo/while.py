number = int(input("Number: "))
counter = 0
while number != 0:
    number = number // 10
# floor division to get an integer
    counter = counter + 1

print("Total digits are", counter)
