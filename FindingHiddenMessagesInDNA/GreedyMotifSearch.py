def GreedyMotifSearch(Dna, k, t):
    BestMotifs = [Dna[i][0:k] for i in range(t)]
    BestScore = float('inf')
    Dna1 = Dna[0]
    l = len(Dna1)
    for i in range(l-k+1):
        Motifs = []
        Motifs.append(Dna1[i:i+k])
        for i in range(1, t):
            P = Profile(Motifs)
            Motifs.append(ProfileMostProbableKmer(Dna[i], k, P))
        currScore = Score(Motifs)
        if currScore < BestScore:
            BestMotifs = Motifs
            BestScore = currScore
    return BestMotifs


def ProfileMostProbableKmer(Dna, k, Profile):
    l = len(Dna)
    pmax = -1
    imax = -1
    for i in range(l-k+1):
        p = Pr(Dna[i:i+k], Profile)
        if p > pmax:
            pmax = p
            imax = i
    return Dna[imax:imax+k]


def Pr(Pattern, Profile):
    seq1 = 'ACGTacgt01230123'
    seq_dict = { seq1[i]:int(seq1[i+8]) for i in range(8) }
    p = 1
    k = len(Pattern)
    for i in range(k):
        p *= Profile[seq_dict[Pattern[i]]][i]
    return p


def Profile(Motifs):
    k = len(Motifs[0])
    n = len(Motifs)
    s = 1 / n
    seq1 = 'ACGTacgt01230123'
    seq_dict = { seq1[i]:int(seq1[i+8]) for i in range(8) }
    P = [[0 for _ in range(k)] for __ in range(4)]
    for Motif in Motifs:
        for i in range(k):
            P[seq_dict[Motif[i]]][i] += s
    return P


def Score(Motifs):
    k = len(Motifs[0])
    n = len(Motifs)
    seq1 = 'ACGTacgt01230123'
    seq_dict = { seq1[i]:int(seq1[i+8]) for i in range(8) }
    P = [[0 for _ in range(4)] for __ in range(k)]
    for Motif in Motifs:
        for i in range(k):
            P[i][seq_dict[Motif[i]]] += 1
    Sm = 0
    for i in range(k):
        Sm += max(P[i])
    return n * k - Sm


Dna = []
file = open('dataset_159_5.txt')
for i, line in enumerate(file):
	if i == 0:
		k, t = map(int, line.rstrip().split(' '))
	else:
		Dna.append(line.rstrip())


data = GreedyMotifSearch(Dna, k, t)
print(*data, sep = ' ')