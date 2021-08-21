"""
numbers[0]  # DONE : has value 3
numbers[-1]  # DONE : has value 2
numbers[3]  # DONE : has value 1
numbers[:-1]  # DONE : has value [3, 1, 4, 1, 5, 9]
numbers[3:4]  # DONE : has value 1
5 in numbers  # DONE : has value True
(7 in numbers  # DONE : has value False
("3" in numbers  # DONE : has value False
numbers + [6, 5, 3]  # DONE : has value [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

"""

numbers = [3, 1, 4, 1, 5, 9, 2]
# i expect 3 nill 1 2 1 0 0 [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers[0] = "ten" # DONE : CHANGE FIRST VALUE TO 'TEN'
numbers[6] = 1 # DONE : CHANGE LAST VALUE TO 1
numbers[2:] # DONE : GOT ALL NUMBERS BUT FIRST 2
9 in numbers # DONE : CHECK IF 9 IN AN ELEMENT ON NUMBERS
