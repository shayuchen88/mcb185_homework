import mcb185
import sys

def kd_value(aa):
    if aa == 'I': return 4.5
    if aa == 'V': return 4.2
    if aa == 'L': return 3.8
    if aa == 'F': return 2.8
    if aa == 'C': return 2.5
    if aa == 'M': return 1.9
    if aa == 'A': return 1.8
    if aa == 'G': return -0.4
    if aa == 'T': return -0.7
    if aa == 'S': return -0.8
    if aa == 'W': return -0.9
    if aa == 'Y': return -1.3
    if aa == 'P': return -1.6
    if aa == 'H': return -3.2
    if aa == 'E': return -3.5
    if aa == 'Q': return -3.5
    if aa == 'D': return -3.5
    if aa == 'N': return -3.5
    if aa == 'K': return -3.9
    if aa == 'R': return -4.5
    return 0

def kd_avgscore(seq):
    score = 0
    for aa in seq:
        score += kd_value(aa)
    return score/len(seq)

def proline(seq):
    return "P" in seq

def signal(seq):
    if len(seq) < 30:
        return False
    for i in range(0, 30 - 8 + 1):
        subseq = seq[i:i+8]
        if kd_avgscore(subseq) >= 2.5:
            return True
    return False

def trans(seq):
    if len(seq) <= 30:
        return False
    for i in range(30, len(seq) - 10):
        subseq = seq[i:i+11]
        if kd_avgscore(subseq) >= 2.0 and not proline(subseq):
            return True
    return False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if signal(seq) and trans(seq):
        print(defline)


