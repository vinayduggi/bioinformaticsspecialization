import random
def OneRandomizedMotifSearch(Dna, k, t):
    Motifs = []
    l = len(Dna[0])
    n = [random.randint(0, l-k) for _ in range(t)]
    Motifs = [Dna[i][n[i]:n[i]+k] for i in range(t)]
    BestMotifs = Motifs
    BestScore = Score(BestMotifs)
    while True:
        Profile = PseudoProfile(Motifs)
        Motifs = MotifsSearch(Dna, k, Profile)
        CurrScore = Score(Motifs)
        if CurrScore < BestScore:
            BestMotifs = Motifs
            BestScore = CurrScore
        else:
            return BestMotifs, BestScore


def RandomizedMotifSearch(Dna, k, t, _iter = 1):
    BestScore = float('inf')
    random.seed()
    for _ in range(_iter):
        currBestMotifs, currBestScore = OneRandomizedMotifSearch(Dna, k, t)
        if currBestScore < BestScore:
            BestMotifs, BestScore = (currBestMotifs, currBestScore)
    return BestMotifs


def MotifsSearch(Dna, k, Profile):
    Motifs = []
    for Seq in Dna:
        Motifs.append(ProfileMostProbableKmer(Seq, k, Profile))
    return Motifs


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


def PseudoProfile(Motifs):
    k = len(Motifs[0])
    n = len(Motifs)
    s = 1 / (n+4)
    seq1 = 'ACGTacgt01230123'
    seq_dict = { seq1[i]:int(seq1[i+8]) for i in range(8) }
    P = [[s for _ in range(k)] for __ in range(4)]
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
file = open('dataset_161_5.txt')
for i, line in enumerate(file):
	if i == 0:
		k, t = map(int, line.rstrip().split(' '))
	else:
		Dna.append(line.rstrip())


BestMotifs = RandomizedMotifSearch(Dna, k, t)
for Motif in BestMotifs:
    print(Motif)