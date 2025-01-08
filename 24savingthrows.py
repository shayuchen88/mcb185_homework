
import random

def savingthrows(dcs, event):
    if event == 'No':
        dice = random.randint(1, 20)
        if dice >= dcs:
            return 'You succeed'
        if dice < dcs:
            return 'You fail'
    if event == 'Advantage':
        dice1 = random.randint(1, 20)
        dice2 = random.randint(1, 20)
        if dice1 > dice2:
            dice  = dice1
        else: dice = dice2
        if dice >= dcs:
            return 'You succeed'
        if dice < dcs:
            return 'You fail'
    if event == 'Disadvantage':
        dice1 = random.randint(1, 20)
        dice2 = random.randint(1, 20)
        if dice1 > dice2:
            dice  = dice2
        else: dice = dice1
        if dice >= dcs:
            return 'You succeed'
        if dice < dcs:
            return 'You fail'

print(savingthrows(5, 'No'))
print(savingthrows(10, 'No'))
print(savingthrows(15, 'No'))