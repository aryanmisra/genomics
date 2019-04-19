seq = input("Input Data: ")
counts = {"A":0,"C":0,"G":0,"T":0}
for i in range(0,len(seq)):
    counts[seq[i]] += 1
print("{a} {c} {g} {t}".format(a=counts["A"],c=counts["C"],g=counts["G"],t=counts["T"]))
