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


Pattern = 'GGATA'
dna = open("dataset_5164_1.txt", "r")
strings = dna.read()
Dna = strings.split(' ')
print(Dna)
print(DistanceBetweenPatternAndStrings(Pattern, Dna))


