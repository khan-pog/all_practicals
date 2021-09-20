""" Test guitar
Creator: Khan Thompson
Date: 06/09/2021
"""

from practical_6.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
gibson.get_age()
print(gibson.get_age())  # Done.
print(gibson.is_vintage())  # Done.

print("My guitars!")
name = input("Name: ")
guitars = []
# Done.
while name != '':
    year = input('Year: ')
    cost = input('Cost: ')
    guitars.append(Guitar(name, int(year), float(cost)))
    print('{} ({}) : ${} added.'.format(name, int(year), float(cost)))
    name = input("Name: ")
print("These are my guitars:")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
for i, guitar in enumerate(guitars, 1):
    # Done.
    print(
        f"Guitar {i}: {guitar.name:{len(guitar.name)}} ({guitar.year}), worth"
        f" ${guitar.cost:{len(str(guitar.cost))},.2f}{' (vintage)' if guitar.is_vintage() else ''}")
