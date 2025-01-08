import random

def deathsaves():
    success_count = 0
    failure_count = 0
    while success_count < 3 and failure_count < 3:
        dice = random.randint(1, 20)
        if dice == 1:
            failure_count += 2
        elif dice == 20:
            return 'revived'
        elif dice < 10:
            failure_count += 1
        elif dice >= 10:
            success_count += 1
    if success_count == 3:
        return 'stable'
    if failure_count == 3:
        return 'die'

number_revived = 0
number_stable = 0
number_die = 0

for i in range(10000):
    if deathsaves() == 'revived':
        number_revived += 1
    if deathsaves() == 'stable':
        number_stable += 1
    if deathsaves() == 'die':
        number_die += 1

print('prob of revived is', number_revived/10000)
print('prob of stable is', number_stable/10000)
print('prob of die is', number_die/10000)
