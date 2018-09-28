# VOLUME OF A CYLINDER
# volume = area of base * height
# area = pi r**2

area = 0
height = 0
volume = 0


def volume(r, h):
    global area
    global height
    global volume
    area = 3.14*(r**2)
    height = h
    volume = area*height
    return volume

print(volume(3, 5))