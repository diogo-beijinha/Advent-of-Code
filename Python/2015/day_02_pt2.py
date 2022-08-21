file = open("Python/2015/input_files/day_02.txt", "r")

ribbon = 0
present_wrap = 0
bow = 0
while 1:
    present_wrap = 0
    bow = 0
    # get and divide size values
    line = file.readline()

    if not line:
        break

    l, w, h = line.split('x')
    l = int(l)
    w = int(w)
    h = int(h)

    present_wrap = 2 * min(l+w, w+h, h+l)
    bow = l * w * h
    ribbon += present_wrap + bow

print(ribbon)
