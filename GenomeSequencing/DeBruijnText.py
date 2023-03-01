﻿# Code to generate nodes and edges accoriding to DeBruijn Graph logic (Hamiltonian Approach) (finding a path visiting every node exactly once)
from collections import defaultdict


def DeBruijnText(k, seq):
    l = len(seq)
    debruijn_graph = defaultdict(list)
    for i in range(l-k+1):
        if seq[i:i+k-1] not in debruijn_graph:
            debruijn_graph[seq[i:i+k-1]] = []
        debruijn_graph[seq[i:i+k-1]].append(seq[i+1:i+k])
    
    for key, value in debruijn_graph.items():
        print(key+' -> '+','.join(value))



if __name__ == '__main__':
    DeBruijnText(12, 'GCTGCCGCGTCAATGACGAGGGCGCTCATTCAGAAAGACATGCATGTTCCGAAAATACCCTGCGATCCAGCTTGGCAATATAAAAGCCTATACGTTTTATCATTACCAATACTTAAGCGTGTAGGAATGGTCCCGGGTACGAGTCGGTTCGGCACCCGGGTCATTTCGGGAATCGGGTGTACGCATTACGTCCCGGGCTAGGCATCGTTGTTAGATCACAACGTCTTATGTCAGAATGGTACCATACACCCAGAAGTATAAGTTTAACGCGGCGCTCATGTTGAGTGCAGTCATAATAATTTTTGCCGGCGTCAACAGACGTTTACTCGTCCCAGTGGAAGCTGGAGTTGCTTTACTTCACAGGCCAAACATTGTGACCCTGTAGAATCCGCTTGGAGCCCCAAAACGAAACCTGAGAGTACCGGGCAACGAACAAATAAGGGTGATTTAGGATTCGCGTTATGTAATTGGTTTGGGTAGCCATACCATTGAAAAATCATTTTGGCGGTTGAATAAGACGGTAATCCGTCTGGGTCCTTCATTGATTTCCATTCGCATGCGAACCGGGGATAACAGGGAGTTGAATGGTCCACCCTGTGCTTCGGGCCACCCTACGTGTATTGAAAGCCAAATGCTGTCTCAGCGAGCACTTGGACATACTGTCAAGGAAAGCGTCGCTGCCTCAAAGGGGACTGGTGCAGGGAATGTCGCGTAGTCGGGTCTAACGGATTTGCTGCCGATGTGTTCATGCGTTATTGCATTCTCCTAAGGCAAGAGGGGCTATTTCAGTATTAGTCAAGCAGCTGCTGTTTGGACCATGTGACGATTAATGATTAATGAGCATGCTGTCGTCTTCGCTTGCCGGTGCCCAAGCCTATCCGTCAATGCTTGGCATGAGAACGATGTTACCACAGTGCACGATGAAGAACTCAACAGGCTAGAACGGATCTGGCTCTGCTTATCTAGCGTTGTGGTATGCACTAAGCCCTATCCTGCCAGGGGACTGGGTCGGTTCAGGAAATAGTCGACCGACTAGTACGTGCCTGCCGTGTCGAGATGAGGGCCTTGTACCTGGTCCCTTCGTCAACCGAACGACATCTACCGTTCAATCATCCGCTTTAAATATTGAAAAACGCATGGGTCATTTCGCATGTATCGTAACATCAATATAGTGCCTTCCCCCTAAACTCCTCCGGTAACCCGTGGCGGCCAACTGCTTACACTTAACAACTTCCTCGCACAAGTTTGGGAAGTTCCTCGAATGCTCATAGAGAAACAGCAATCTAGGGTATCTGCTTCTTGACCATGAGCGAACCAGTGACGCCAGCTTACGAGTGAAGACCGACCTCATTATCAGGGAGCCGTGGACGTAGTGGAAAACGCTTCGAGATGTAAGGGGTCTGGAGTGTCTATCCATGATACATCTGAGTCAAACGAGTTCATAGATACTTAGGGTTATCAAGCTCACCAGGTCAGTAGTGATAAGAATATAAGGCGTCTACAACCGGGCACTAACAGAAGTAATGTCCAAGAGGTCAACTCAGTAAGCCTTCGACAGTCTAAAGGACAAACGCTCCCTGTTCGGATACACCTGGAAATACGTGGGAGTATTCTGAAGCTTGACGAAATTTATGATGGCCGTACGTTAGAAAATGAGACTTGAGAGACAGCAGCCTGTTTAAGACGTCCTGTTTTCATTACTGTCGCGATGCGGGTATCCTGGGGTGTGACCGCCTTTCCTTCAATTGACGGTTTCCTAGTGGCGATTACGAGCTTGGCGACAGTTACCGCCTGGTCTGCCGGTTATCGCTGCGTGATACCTAACTAGCATGCCCCAGTGTTAGTGCTTCATCACATAAGAGGATCTCTGGAGTAATGGAACCGTACCGATCATTCCTGTTGCGACAGGAAGCCATAAGCTCGCTACATGCTGTTTGAATGTGCATTCTATGTTAAATCTTACGCGACAGTAGGGAGCCGGCGTCGGGAACGCTGTGATT')