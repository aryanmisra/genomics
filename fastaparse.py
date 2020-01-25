#parses fasta formatted files into dict objects

import re

file = "test.fasta"
seqs = {}
with open(file) as f:
    for row in f:
        row = row.rstrip()
        row_header = re.search(r'^>\w+', row) #using regex to search for > which indicates the start of a header
        if row_header:
            seqs[row_header.group(0)] = [] #create new key in dictionary if row is a header
            hold = row_header.group(0) #putting current working key into memory
        else:
            # seqs[hold] = row
            if row is not None: seqs[hold].append(row) #appending DNA seq to current working key

for key in seqs:
    seqs[key] = ''.join(map(str, seqs[key])) #converting list to string

print(seqs)