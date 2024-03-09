
for number in range(6):
    print("Attempt", number + 1)
Scored = False
for x in range(0, 10, 2):
    print("Score: ", x)
    if Scored:
        print("Wonderful!")
        break
else:
    print("Try again")