sample_data = input("Input: ")
letters = 0
numbers = 0
for i in sample_data:
    if i.isalpha():
        letters += 1

    elif i.isdigit():
        numbers += 1
    else:
        pass

print("Letters: ", letters)
print("Numbers: ", numbers)
