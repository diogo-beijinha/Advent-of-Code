file = open("Python/2015/input_files/day_02.txt", "r")

# surface area of the box = 2*l*w + 2*w*h + 2*h*l
'''
For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
'''

paper = 0
smallest = 0


while 1:
    # get and divide size values
    line = file.readline()

    if not line:
        break

    l, w, h = line.split('x')
    l = int(l)
    w = int(w)
    h = int(h)

    # get smallest area
    smallest = l * w
    if w * h < smallest:
        smallest = w * h
    if h * l < smallest:
        smallest = h * l

    # calculate surface areas for present
    paper += 2*l*w + 2*w*h + 2*h*l
    paper += smallest


print("Total square feet of wrapping paper to order:", paper)
