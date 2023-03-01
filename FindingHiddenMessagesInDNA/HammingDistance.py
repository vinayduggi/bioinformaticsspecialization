def HammingDistance(p, q):
    HamDist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            HamDist += 1
    return HamDist


p = 'CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG'
q = 'ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT'

print(HammingDistance(p, q))