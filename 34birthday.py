import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def same():
    cal = []
    for i in range(days):
        cal.append(0)
    for i in range(people):
        bd = random.randint(0, days - 1)
        if cal[bd] != 0:
            return True
        else: cal[bd] += 1
    return False

def counting(times):
    counting = 0
    for i in range(times):
        if same():
            counting += 1
    return counting

print(counting(trials)/trials)


