import sequence

seq = "ACGTACGTGGGGGACGTACGTCCCCC"
w = 10
for i in range(len(seq) -w +1):
    sq = seq[i:i+w]
    print(i, sq, sequence.gc_comp(sq), sequence.gc_skew(sq))