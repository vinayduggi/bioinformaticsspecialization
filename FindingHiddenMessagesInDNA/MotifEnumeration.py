def MotifEnumeration(Dna, k, d):
    Patterns = set()
    neighbor = set()
    text = Dna[0]
    for i in range(len(text)-k+1):
        n = Neighbors(text[i:i+k], d)
        neighbor = neighbor.union(n)
        for n in neighbor:
            ValidPattern = True
            for i in range(1, len(Dna)):
                if not DoesPatternAppear(n, Dna[i], d):
                    ValidPattern = False
                    break
            if ValidPattern:
                Patterns.add(n)
    return Patterns


def DoesPatternAppear(Pattern, Text, d):
    k = len(Pattern)
    l = len(Text)
    for i in range(l-k+1):
        if HammingDistance(Pattern, Text[i:i+k]) <= d:
            return True
    return False 


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


Dna = "ACAAAGTCCTCCAATCGTGTGGACA", "GTGTGCTAATGGGGGCGTTCCCGGA", "TGGTAATTGCCTCAGCTAATCCCTA", "TCTCTCATTACAAATTATCCTAGGC", "TGAGTTTTAATGATCCTGCTCTAAT", "AATGACTAATTCCAAGGATAATTTA"
k = 5
d = 1
m = MotifEnumeration(Dna, k, d)
print(' '.join(m))