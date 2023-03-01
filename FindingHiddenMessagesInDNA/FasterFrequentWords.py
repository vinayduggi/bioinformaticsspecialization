def FasterFrequentWords(Genome, k):
    FrequentPatterns = []
    FrequencyArray = ComputingFrequencies(Genome, k)
    maxCount = max(FrequencyArray)
    for i in range(pow(4, k)):
        if FrequencyArray[i] == maxCount:
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
    return FrequencyArray


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

Genome = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
data = FasterFrequentWords(Genome, k)
print(*data)


