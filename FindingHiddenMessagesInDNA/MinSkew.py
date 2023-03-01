def Skew(Genome):
    skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'G':
            skew.append(skew[i]+1)
        elif Genome[i] == 'C':
            skew.append(skew[i]-1)
        else:
            skew.append(skew[i])
    return skew


E_Coli_Genome = open("E_coli.txt", "r")
Genome = E_Coli_Genome.read()

def MinSkew(Genome):
    sk = Skew(Genome)
    m = min(sk)
    return [i for i, val in enumerate(sk) if val == m]


data = MinSkew(Genome)
print(*data, sep = ' ')


