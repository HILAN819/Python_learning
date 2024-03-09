x = int(input("X: "))
y = int(input("Y: "))

message = "X is greater than Y." if x > y else "Y is greater than X." if y > x else "X is equal to Y."
print(message)