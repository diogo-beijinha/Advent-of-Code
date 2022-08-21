file = open("input_files/day_01.txt", "r")
floor = 0
pos = 0

while 1:
    char = file.read(1)
    if not char:
        break

    if char == "(":
        floor += 1
        pos += 1
        if floor == -1:
            break
    elif char == ")":
        floor -= 1
        pos += 1
        if floor == -1:
            break
    else:
        pass

print("Santa has arrived to the basement in position {0}".format(pos))
