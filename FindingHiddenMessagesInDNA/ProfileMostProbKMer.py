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
    p = 1
    k = len(Pattern)
    for i in range(k):
        p = p * Profile[Pattern[i]][i]
    return p


Profile = {'A': 0, 'C': 0, 'G': 0, 'T': 0} 
keys = 'ACGT'
file = open('dataset_159_3.txt')
for i, line in enumerate(file):
	if i == 0:
		Dna = line.rstrip()
	elif i == 1:
		k = int(line.rstrip())
	else:
		temp = list(map(float, line.rstrip().split(' ')))
		Profile[keys[i - 2]] = temp


print(ProfileMostProbableKmer(Dna, k, Profile))