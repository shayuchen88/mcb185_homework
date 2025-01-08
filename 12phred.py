import math

def char_to_prob(char):
    q = ord(char) - 33
    prob = 10 ** (-q / 10)
    return prob

def prob_to_char(prob):
    if prob <= 1 and prob > 0:
        q = -10 * math.log10(prob)
        char = chr(round(q) + 33)
        return char
    else:
        return None


print(char_to_prob('A'))
print(prob_to_char(0.001))