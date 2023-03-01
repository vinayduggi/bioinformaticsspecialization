#finding a path visiting every edge exactly once (eulerian path)
from collections import defaultdict


def DeBruijnPatterns(Kmers):
    k = len(Kmers[0])
    debruijn_patterns = defaultdict(list)
    for edge in Kmers:
        if edge[:k-1] not in debruijn_patterns:
            debruijn_patterns[edge[:k-1]] = []
        debruijn_patterns[edge[:k-1]].append(edge[1:])

    
    for key, value in debruijn_patterns.items():
        print(key+' -> '+','.join(value))





Kmers_in = open('sample.txt','r')
Kmers = Kmers_in.read().split()


if __name__ == '__main__':
    DeBruijnPatterns(Kmers)