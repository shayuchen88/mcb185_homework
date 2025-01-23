import sequence

print(sequence.transcribe("ACGT"))
print(sequence.revcomp("AAAACGT"))
print(sequence.translate("ATGCCCTAA"))

s = "ACGTGGGGGGCATATG"
print(sequence.gc_comp(s))
print(sequence.gc_skew(s), sequence.gc_skew(sequence.revcomp(s)))

seq = "ACGTACGTGGGGGACGTACGTCCCCC"
w = 10
for i in range(len(seq) -w +1):
    sq = seq[i::i+w]
    print(i, sequence.gc_comp(sq), sequence.gc_skew(sq))