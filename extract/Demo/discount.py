quantity = int(input("Units Bought: "))
total_cost = quantity * 100
if total_cost >= 1000:
    discounted_price = total_cost - (total_cost * 10/100)
    print("Your discounted price is: ", discounted_price)
else:
    print("Your price is: ", total_cost)