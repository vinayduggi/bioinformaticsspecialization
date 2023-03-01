def FrequentWordsMismatch(Genome, k, d):
    FrequentPatterns = []
    FrekuencyArray = ComputingFrequenciesWithMismatches(Genome, k, d)
    maxCount = max(FrekuencyArray)
    for i in range(len(FrekuencyArray)):
        if FrekuencyArray[i] == maxCount:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns


def ComputingFrequenciesWithMismatches(Text, k, d):
    FrequencyArray = []
    for i in range(pow(4, k)):
        FrequencyArray.append(0)
    for i in range(len(Text)-(k-1)):
            Pattern = Text[i:i+k]
            Neighbourhood = Neighbors(Pattern, d)
            for ApproximatePattern in Neighbourhood:
                j = PatternToNumber(ApproximatePattern)
                FrequencyArray[j] += 1
    return FrequencyArray


def PatternToNumber(Pattern):
    base_num = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    total = 0
    for i, val in enumerate(Pattern[::-1]):
        total += base_num[val] * pow(4, i)
    return total

def NumberToPattern(Index, k):
    num_base = {0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T'}
    Pattern = ''
    for i in range(k):
        Pattern += num_base[Index % 4]
        Index = Index // 4
    return Pattern[::-1]


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

Genome = 'GGGAAAAAAAAGGGAGCTACATACAAAAAAGCAGCAAAAAAAATACAGGGGGGTACATAATAATACAGGGGGGTACAAGCGGGTAAAAAAGGGAAAAAAAAAGCGGGTACAGGGTAATACAGGGGGGAAAATAATAAAGCTACAAGCGGGAAAAGGGTACAGGGAAAAGGGTACATACAGGGAAAATAAAAAATAAAGCTACAAAAAAGCAGCAAAATACAGGGAGCTACAAAAAAAAATAAGGGGGGGGGTACATAATACAAAAAAAAATACAAGCTACATACAAGCTACATAAGGGAAAAAAAAAAAAAAAAAAAAAGC'
k = 6
d = 2
data = FrequentWordsMismatch(Genome, k, d)
print(*data)


