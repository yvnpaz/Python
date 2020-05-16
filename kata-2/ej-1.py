"""
Una panadería vende barras de pan a 3.49€ ...
"""

price = 3.49
discount = 1 - 0.6
discount_price = price * discount

number_bread = int(input('Introduce the number of bread: '))

print("Number of bread: ", number_bread)
print("Price habitual: " +  str(price))
print("Price with discount: " + str(discount_price))
print("Cost total: " + str(number_bread * discount_price))
