file = open("input_files/day_01.txt", "r")
floor = 0

while 1:
    char = file.read(1)
    if not char:
        break

    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    else:
        pass

print(floor)
