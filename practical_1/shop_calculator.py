cost_matrix = 0
while 1 == 1:
    number_of_items = int(input("Number of items: "))
    if number_of_items > 0:
        for q in range(0, number_of_items, 1):
            cost_of_items = int(input("Price of item: "))
            cost_matrix += cost_of_items
        break
    else:
        print("Enter valid input")


print("Total price for", end=" ")
print(number_of_items, end=" ")
print("items is", end=" ")
print(cost_matrix)
