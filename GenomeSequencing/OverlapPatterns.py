# Code for overlap patterns using a set of kmers using nodes and edges

from collections import defaultdict


def OverlapPatterns(Kmers):
    AdjList = defaultdict(list)
    for node in Kmers:
        AdjList[node[:-1]].append(node)
    for node in Kmers:
        Suffix = AdjList[node[1:]]
        if Suffix:
            print(node+' -> '+','.join(Suffix))




Kmers_in = open('dataset_198_10.txt','r')
Kmers = Kmers_in.read().split()


if __name__ == '__main__':
    OverlapPatterns(Kmers)