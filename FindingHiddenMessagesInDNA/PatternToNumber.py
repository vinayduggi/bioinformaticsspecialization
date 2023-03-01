def PatternToNumber(Pattern):
    base_num = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    total = 0
    for i, val in enumerate(Pattern[::-1]):
        total += base_num[val] * pow(4, i)
    return total


Pattern = 'AAGCAAAGGTGGG'
print(PatternToNumber(Pattern))