import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

color = [R, G, B]

colorname = []
colorcode = []

fp = open(colorfile)
for line in fp:
    colorname.append(line.split()[0])
    colorcode.append(line.split()[2])
fp.close()

def dtc(P, Q):
    d = 0
    for p, q in zip(P, Q):
        d += abs(p - q)
    return d

def colornumber(code):
    return [int(code.split(",")[0]), int(code.split(",")[1]), int(code.split(",")[2])]

def main():
    mindiff = 255
    idx = 0
    for i in range(0, len(colorcode)):
        if dtc(color, colornumber(colorcode[i])) < mindiff:
            mindiff = dtc(color, colornumber(colorcode[i]))
            idx = i
    return (colorname[idx])

print(main())

