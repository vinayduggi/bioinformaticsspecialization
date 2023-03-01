def ApproximatePatternCount(Genome, Pattern, d):
    count = 0
    for i in range(len(Genome)-len(Pattern)+1):
        mismatch = Genome[i:i+len(Pattern)]
        if HammingDistance(Pattern, mismatch) <= d:
                count += 1
    return(count)


def HammingDistance(p, q):
    HamDist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            HamDist += 1
    return HamDist


Vibrio_Cholorae= open("Vibrio_Cholorae_Genome.txt", "r")
Genome = Vibrio_Cholorae.read()
Pattern = 'ATGATCAAG'
d = 4
print(ApproximatePatternCount(Genome, Pattern, d))