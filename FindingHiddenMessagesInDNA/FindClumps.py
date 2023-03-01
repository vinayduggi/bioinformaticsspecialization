def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for j in range(n-k+1):
            if Pattern == Text[j:j+k]:
                freq[Pattern] += 1
    return freq

def FindClumps(Genome, k, L, t):
    Patterns = []
    n = len(Genome)
    for i in range(n-L):
        Window = Genome[i:i+L]
        freqMap = FrequencyMap(Window, k)
        for key in freqMap:
            if freqMap[key] >= t:
                Pattern = key
                Patterns.append(Pattern)
                Patterns = list(set(Patterns))
    return Patterns


E_Coli_Genome = open("E_coli.txt", "r")
Genome = E_Coli_Genome.read()
k = 9
L = 500
t = 3
print(FindClumps(Genome, k, L, t))