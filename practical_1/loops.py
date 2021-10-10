for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
stars = int(input("Number of stars: "))

for q in range(0, stars, 1):

    for i in range(0, q, 1):
        print('*', end=" ")
        q += 1
    print('  ')
