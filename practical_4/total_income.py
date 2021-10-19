"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of number_of_months."""
    incomes = []
    # DONE : Refactor the months variable to number_of_months
    number_of_months = int(input("How many number_of_months? "))

    for month in range(1, number_of_months + 1):
        # DONE : Change the line that gets the income input so that it uses the string format() method instead of string concatenation (+).
        income = float(input("Enter income for month {}: ".format(str(month))))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()