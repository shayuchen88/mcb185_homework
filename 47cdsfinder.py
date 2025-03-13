import sys
import mcb185

length = int(sys.argv[2])

def translate(codon):
    aa = ""
    if codon in ['ATA', 'ATC', 'ATT']:
        aa = 'I'
    elif codon == 'ATG':
        aa = 'M'
    elif codon in ['ACA', 'ACC', 'ACG', 'ACT']:
        aa = 'T'
    elif codon in ['AAC', 'AAT']:
        aa = 'N'
    elif codon in ['AAA', 'AAG']:
        aa = 'K'
    elif codon in ['AGC', 'AGT']:
        aa = 'S'
    elif codon in ['AGA', 'AGG']:
        aa = 'R'
    elif codon in ['CTA', 'CTC', 'CTG', 'CTT']:
        aa = 'L'
    elif codon in ['CCA', 'CCC', 'CCG', 'CCT']:
        aa = 'P'
    elif codon in ['CAC', 'CAT']:
        aa = 'H'
    elif codon in ['CAA', 'CAG']:
        aa = 'Q'
    elif codon in ['CGA', 'CGC', 'CGG', 'CGT']:
        aa = 'R'
    elif codon in ['GTA', 'GTC', 'GTG', 'GTT']:
        aa = 'V'
    elif codon in ['GCA', 'GCC', 'GCG', 'GCT']:
        aa = 'A'
    elif codon in ['GAC', 'GAT']:
        aa = 'D'
    elif codon in ['GAA', 'GAG']:
        aa = 'E'
    elif codon in ['GGA', 'GGC', 'GGG', 'GGT']:
        aa = 'G'
    elif codon in ['TCA', 'TCC', 'TCG', 'TCT']:
        aa = 'S'
    elif codon in ['TTC', 'TTT']:
        aa = 'F'
    elif codon in ['TTA', 'TTG']:
        aa = 'L'
    elif codon in ['TAC', 'TAT']:
        aa = 'Y'
    elif codon in ['TAA', 'TAG', 'TGA']:
        aa = '*'
    else:
        aa = 'X'  
    return aa

def revcomp(dna_sequence):
    rc = []
    for nt in dna_sequence[::-1]:
        if   nt == 'A': rc.append('T')
        elif nt == 'C': rc.append('G')
        elif nt == 'G': rc.append('C')
        elif nt == 'T': rc.append('A')
        else:           rc.append('N')
    return ''.join(rc)

def translation(seq):
    protein = []
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        protein.append(translate(codon))
    return ''.join(protein)

def orf(proteinseq):
    orfs = []
    i = 0
    while i < len(proteinseq):
        if proteinseq[i] == 'M':
            for j in range(i, len(proteinseq)):
                if proteinseq[j] == '*':
                    if (j - i + 1) >= length:
                        orfs.append(proteinseq[i:j+1])
                    i = j
                    break
        i += 1
    return orfs

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    protein = translation(seq)
    orf_ = orf(protein)
    for i in range(len(orf_)):
        if len(orf_[i]) >= 100:
            print(">NC_000913.3-prot-"+str(i))
            print(orf_[i][:20])


