import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
    for lines in fp:
        if lines[0] != "#":
            words = lines.split()
            if words[2] == "CDS":
                beg = int(words[3])
                end = int(words[4])
                print(end - beg + 1)