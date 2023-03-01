def Pr(Pattern, Profile):
    seq1 = 'ACGTacgt01230123'
    seq_dict = { seq1[i]:int(seq1[i+8]) for i in range(8) }
    p = 1
    k = len(Pattern)
    for i in range(k):
        p *= Profile[seq_dict[Pattern[i]]][i]
    return p


Pattern = 'CAGTGA'
Profile = {
    'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
    'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
    'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
    'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
}


print(Pr(Pattern, Profile))