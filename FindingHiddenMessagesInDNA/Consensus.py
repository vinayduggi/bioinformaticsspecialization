import numpy as np
def Consensus(Motifs):
    P = PseudoProfile(Motifs)
    k = len(P[0])
    Pt = [[row[i] for row in P] for i in range(k)]
    seq_dict = ['A', 'C', 'G', 'T']
    return ''.join([seq_dict[np.argmax(Pt[i])] for i in range(k)])


def PseudoProfile(Motifs):
    k = len(Motifs[0])
    n = len(Motifs)
    s = 1 / (n+4)
    seq1 = 'ACGTacgt01230123'
    seq_dict = { seq1[i]:int(seq1[i+8]) for i in range(8) }
    P = [[1 for _ in range(k)] for __ in range(4)]
    for Motif in Motifs:
        for i in range(k):
            P[seq_dict[Motif[i]]][i] += s
    return P


Motifs = ['TTTGGGACGCTC', 'TATGGGCCTCTC', 'TTTGAGGCACTC', 'TGTGCGACCCTC', 'TATGAGTCTCTC', 'TCTGTGCCACTC', 'TCTGAGACCCTC', 'TGTGCGTCTCTC', 'TTTGTGGCCCTC', 'TATGAGACCCTC', 'TGTGGGACTCTC', 'TATGGGTCCCTC', 'TTTGCGACTCTC', 'TTTGTGTCACTC', 'TCTGTGTCTCTC', 'TTTGGGTCACTC', 'TTTGTGTCGCTC', 'TATGTGCCCCTC', 'TGTGTGACTCTC', 'TCTGAGACGCTC', 'TTTGGGACGCTC', 'TTTGCGTCGCTC', 'TATGGGGCGCTC', 'TCTGGGGCACTC', 'TCTGAGACGCTC']


print(Consensus(Motifs))