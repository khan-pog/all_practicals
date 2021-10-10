temps_input = open('temps_input.txt', 'r')
name_file = open('temps_output.txt', 'w')
i = 0
for line_str in temps_input:
    celsius = 5 / 9 * (int(line_str) - 32)
    print(int(celsius), file=name_file)
    print(int(line_str))
    print(celsius)
    # makes temps_output.txt file with






