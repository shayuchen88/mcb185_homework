import sys
import math

nt = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

def ma(nt1, nt2):
    if nt1 == nt2:
        return match
    return mismatch

for nts in nt:
    print(f'{nts:>3}', end="")
print()
for i in range(0, len(nt)):
    print(nt[i], end="")
    for j in range(0, len(nt)):
        print(f'{(ma(nt[i], nt[j])):>3}', end="")
    print()