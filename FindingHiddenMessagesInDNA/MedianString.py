def MedianString(Dna, k):
    dist = float('inf')
    for i in range(pow(4, k)):
        Pattern = NumberToPattern(i, k)
        distanc = DistanceBetweenPatternAndStrings(Pattern, Dna)
        if dist > distanc:
            dist = distanc
            Median = Pattern
    return Median


def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for Text in Dna:
        l = len(Text)
        hamdist = float('inf')
        for i in range(l-k+1):
            hamdistc = HammingDistance(Pattern, Text[i:i+k])
            if hamdist > hamdistc:
                hamdist = hamdistc
        distance += hamdist
    return distance


def HammingDistance(p, q):
    HamDist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            HamDist += 1
    return HamDist


def NumberToPattern(Index, k):
    num_base = {0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T'}
    Pattern = ''
    for i in range(k):
        Pattern += num_base[Index % 4]
        Index = Index // 4
    return Pattern[::-1]


k = 7
#dna = open("dataset_158_9.txt", "r")
#strings = dna.read()
#Dna = strings.split(' ')
Dna = ["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC", "GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC", "GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"]
print(MedianString(Dna, k))