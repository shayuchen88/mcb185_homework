def skew(seq, w):
    tempseq = seq[0:w]
    print(tempseq)
    for i in range(len(seq) -w):
        newseq = tempseq[1:] + seq[i+w]
        tempseq = newseq
        print(tempseq)

skew('ACGTACGTGGGGGACGTACGTCCCCC', 3)



