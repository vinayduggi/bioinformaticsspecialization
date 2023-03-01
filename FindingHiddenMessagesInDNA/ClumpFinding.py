def ClumpFinding(Genome, k, L, t):
    FrequentPatterns = []
    Clump = []
    for i in range(pow(4, k)):
        Clump[i] = 0
    for i in range(len(Genome)-L+1):
        Text = Genome[i:i+L]
        FrequencyArray = ComputingFrequencies(Text, k)
        for index in range(pow(4, k)):
            if FrequencyArray[index] >= t:
                Clump[index] = 1
    for i in range(pow(4, k)):
        if Clump[i] == 1:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns


def ComputingFrequencies(Text, k):
    FrequencyArray = []
    for i in range(pow(4, k)):
        FrequencyArray.append(0)
    for i in range(len(Text)-(k-1)):
            Pattern = Text[i:i+k]
            j = PatternToNumber(Pattern)
            FrequencyArray[j] += 1
    Result = ""
    for item in FrequencyArray:
        Result = Result + " " + str(item)
    return Result


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


E_Coli_Genome = open("E_coli.txt", "r")
Genome = E_Coli_Genome.read()
k = 9
L = 500
t = 3
print(ClumpFinding(Genome, k, L, t))

