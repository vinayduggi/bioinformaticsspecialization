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
oriC= open("oriC_Vibrio_Cholerae.txt", "r")
Text = oriC.read()
k = 9
print(FrequencyMap(Text, k))


def FrequencyWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            Pattern = key
            words.append(Pattern)
    return words
print(FrequencyWords(Text, k))
