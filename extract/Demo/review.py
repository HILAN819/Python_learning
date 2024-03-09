# fruit = 10 % 3
# print(fruit)
# print(bool("false"))

Temparature = input("The Temparature is: ")
temparature = int(Temparature)
if 30 <= temparature < 50:
    print("Situation Critical")

elif 0 <= temparature < 30:
    print("Conditions conducive")

elif  -20 <= temparature < 0:
    print("Warm clothing recommended!")

else:
    print("lets drink champagne coz we are DEAD!!")
