import math

for a in range(1, 101):
    for b in range(a + 1, 101):
        if math.sqrt(a**2 + b**2) % 1 == 0:
            print(a, b, math.floor(math.sqrt(a**2 + b**2)))