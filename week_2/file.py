
number_sumation = 0

number_to_add = 0



number_file = open('number.txt', 'r')

for line_str in number_file:
    number_sumation += int(line_str)

    print(line_str)
print(number_sumation)

number_file.close()

name_file = open('name.txt', 'w')
print("Your name is Bob", file=name_file)
number_file = open('number.txt', 'r')
first_number_to_add = int(number_file.readline())


second_number_to_add = int(number_file.readline())

print(first_number_to_add + second_number_to_add)

number_file.close()
