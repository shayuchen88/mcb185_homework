import sys
import mcb185
import math

winsize = int(sys.argv[2])
th = float(sys.argv[3])

def entropy(prob_list):
    h = 0
    for p in prob_list:
        if p > 0:
            h -= p * math.log2(p) 
    return h

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline)
    seq = list(seq)

    for i in range(0, len(seq) - winsize + 1):
        subseq = seq[i:i+winsize]
        
        num_A = subseq.count("A")
        num_T = subseq.count("T")
        num_G = subseq.count("G")
        num_C = subseq.count("C")
        
        prob_A = num_A / winsize
        prob_T = num_T / winsize
        prob_G = num_G / winsize
        prob_C = num_C / winsize
        
        prob_list = [prob_A, prob_T, prob_G, prob_C]
        h = entropy(prob_list)

        if h < th:
            seq[i:i+winsize] = ["N"] * winsize

    print("".join(seq))