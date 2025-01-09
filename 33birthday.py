import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def same_birthday():
    birthday = []
    for i in range(people):
        bd = random.randint(1, days)
        if bd in birthday:
            return True
        else: birthday.append(bd)
    return False

def counting(times):
    count = 0
    for i in range(times):
        if same_birthday():
            count += 1
    return count

print(counting(trials)/trials)