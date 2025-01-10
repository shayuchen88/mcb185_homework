import sys
import math

nt = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

for i in range(0, len(nt)):
    for j in range(0, len(nt)):
        if nt[i] == nt[j]:
            print(nt[i], match)
        else: print(nt[j], mismatch)
    