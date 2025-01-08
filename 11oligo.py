def tm(a, c, g, t):
    if (a + c + g + t) <= 13:
        Tm = ((a + t) * 2)+((g + c) * 4)
    else: 
        Tm = 64.9 + ((41 * (g + c - 16.4)) / (a + t + g + c)) 
    return Tm

print(tm(5, 7, 3, 4))