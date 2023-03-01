import random
def GibbsSampler(Dna, k, t, N):
    l = len(Dna[0])
    m = [random.randint(0, l-k) for _ in range(t)]
    Motifs = [Dna[i][m[i]:m[i]+k] for i in range(t)]
    BestMotifs = Motifs
    BestScore = Score(BestMotifs)
    for j in range(N):
        i = random.randint(0, t-1)
        P = PseudoProfile(Dna[:i] + Dna[i+1:])
        Motif_i = ProfileRandomKmer(Dna[i], k, P)
        Motifs = Motifs[:i] + [Motif_i] + Motifs[i+1:]
        currScore = Score(Motifs)
        if currScore < BestScore:
            BestMotifs = Motifs
            BestScore = currScore
    return BestMotifs, BestScore

def RunGibbsSampler(Dna, k, t, N, _iter = 20):
    BestScore = float('inf')
    random.seed()
    for _ in range(_iter):
        currBestMotifs, currBestScore = GibbsSampler(Dna, k, t, N)
        if currBestScore < BestScore:
            BestMotifs, BestScore = (currBestMotifs, currBestScore)
    return BestMotifs


def BiasedRandom(bias_list):
    number = random.uniform(0, sum(bias_list))
    curr = 0
    for i, bias in enumerate(bias_list):
        curr += bias
        if number <= curr:
            return i

def ProfileRandomKmer(Seq, k, Profile):
    l = len(Seq)
    p = []
    for i in range(l-k+1):
        p.append(Pr(Seq[i:i+k], Profile))
    i = BiasedRandom(p)
    return Seq[i:i+k]


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


def Pr(Pattern, Profile):
    seq1 = 'ACGTacgt01230123'
    seq_dict = { seq1[i]:int(seq1[i+8]) for i in range(8) }
    p = 1
    k = len(Pattern)
    for i in range(k):
        p *= Profile[seq_dict[Pattern[i]]][i]
    return p


Dna = []
file = open('dataset_163_4.txt')
for i, line in enumerate(file):
	if i == 0:
		k, t, N = map(int, line.rstrip().split(' '))
	else:
		Dna.append(line.rstrip())

print(GibbsSampler(Dna,k,t, N))