import math


def calculation(radius, height):
    return 2 * math.pi * radius * (radius + height)


sets = 11

print('radius\theight\tsurface_area')

for i in range(1, sets):
    print(f"{i}\t{i*2}\t{calculation(i, i*2):.2f}")






