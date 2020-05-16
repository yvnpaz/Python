"""
...
"""

age = int(input("Introduce your age, please: "))

if age < 4:
    print("The price of the ticket is zero.")
elif age >= 4 and age <= 18:
    print("The price of the ticket is fifth euros.")
else:
    print("The price of the ticket is ten euros.")