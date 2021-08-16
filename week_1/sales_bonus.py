sales = float(input("Enter sales: $"))
while sales >= 0:
      if sales >= 1000:
        sales *= 0.15
        print(sales)
      elif sales <= 0:
        print('Enter valid input.')
      else:
         sales *= 0.1
         print(sales)
      sales = float(input("Enter sales: $"))



