def Neighbors(Pattern, d):
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        return{'A', 'C', 'G', 'T'}
    Neighborhood = set()
    Suffix = Pattern[1:]
    FirstSymbol = Pattern[0]
    SuffixNeighbors = Neighbors(Suffix, d)
    Nucleotides = ['A', 'C', 'T', 'G']
    for Text in SuffixNeighbors:
        if HammingDistance(Text, Suffix) < d:
            for x in Nucleotides:
                Neighborhood.add(x+Text)
        elif HammingDistance(Text, Suffix) ==d:
            Neighborhood.add(FirstSymbol+Text)
    return Neighborhood


def HammingDistance(p, q):
    HamDist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            HamDist += 1
    return HamDist
            

Pattern = 'ACGT'
d = 3
data = Neighbors(Pattern, d)
print(*data)
