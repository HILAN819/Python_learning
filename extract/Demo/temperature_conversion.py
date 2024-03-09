# Formula : c/5 = f-32/9
temp = input('Temperature e.g 45C or 32F: ')
degree = int(temp[:-1])
unit = temp[-1]

if unit.upper() == 'F':
    tempe_conversion = int(round((degree - 32) * 5/9))
    o_convention = "Celsius"
elif unit.upper() == 'C':
    tempe_conversion = int(round((degree * 9/5) - 32))
    o_convention = "Farenheit"
else:
    print("Proper convention needed.")

print("The temperature in ", o_convention, "is", tempe_conversion, 'degrees')

# temp_farenheit = (temp * 9/5) + 32
# print("Temperature in Farenheit is: " + str(temp_farenheit))
