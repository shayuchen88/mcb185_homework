def transcribe(dna):
    return dna.replace('T', 'U')

def revcomp(dna):
    rc = []
    for nt in dna[::-1]:
        if nt == 'A': rc.append('T')
        elif nt == 'C': rc.append('G')
        elif nt == 'G': rc.append('C')
        elif nt == 'T': rc.append('A')
        else: rc.append('N')
    return ''.join(rc)

def translate(dna):
    ass = []
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if codon == "ATG": ass.append("M")
        elif codon == "TAA": ass.append("*")
        elif codon == "TAG": ass.append("*")
        elif codon == "TGA": ass.append("*")
        else: ass.append("X")
    return " ".join(ass)