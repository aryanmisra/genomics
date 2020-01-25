#finds reverse complement of DNA sequences

seq = input("input: ")
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
bases = list(seq)
bases = [complement[base] for base in bases]
word = ''.join(bases)
print(word[::-1])
