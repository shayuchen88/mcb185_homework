import sys
import math

pro = []
for p in sys.argv[1:]:
    temp = float(p)
    if temp >= 1 or temp <= 0:
        sys.exit("wrong probabilities! probabilities can's larger than 1 or lower than 0")
    pro.append(temp)

total = 0
for p in pro:
    total += p
if math.isclose(total, 1.0) == False:
    sys.exit('wrong probabilities! sum of probabilities is larger than 1')

entropy = 0
for p in pro:
    entropy -= p * math.log2(p)

print(f'{entropy:.4f}')
        