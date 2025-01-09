import math

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

print(f'{math.pi}')
print(f'{math.pi:.3f}')
print(f'{1e6 * math.pi:e}')
print(f'{"hello world":>20}')
print(f'{"hello world":.>20}')
print(f'{20:<10} {10}')

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq:
    print(nt, end='')
print()

for nt in seq:
    print(nt)
print()

s = 'ABCDEFGHIJ'
print(s[0:5])

print(s[0:8:2])

print(s, s[::], s[::1], s[::-1])


nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])

for i, nt in enumerate(nts):
    print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])

for nt, name in zip(nts, names):
    print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

text = 'good day          to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

import sys
print(sys.argv)