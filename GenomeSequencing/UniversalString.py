from itertools import product

def universal_string(k):
    kmers = [''.join(item) for item in product('01', repeat=k)]
    return kmers

from collections import defaultdict


def DeBruijnPatterns(Kmers):
    k = len(Kmers[0])
    debruijn_patterns = defaultdict(list)
    for edge in Kmers:
        if edge[:k-1] not in debruijn_patterns:
            debruijn_patterns[edge[:k-1]] = []
        debruijn_patterns[edge[:k-1]].append(edge[1:])
    return debruijn_patterns


from random import randint

def EulerianCycle(Graph, k):
    maxEdge = maxEdges(Graph)
    GraphNodes = list(Graph.keys())
    StrtNode = GraphNodes[0]
    CurrNode = GraphNodes[0]
    Stack = []
    Cycle = []
    while len(Cycle) != maxEdge:
        if Graph[CurrNode] != []:
            Stack.append(CurrNode)
            NexNode = randint(0,len(Graph[CurrNode])-1)
            PrevNode = CurrNode
            CurrNode = Graph[CurrNode][NexNode]
            Graph[PrevNode].remove(CurrNode)
        else:
            Cycle.append(CurrNode)
            CurrNode = Stack[len(Stack)-1]
            Stack.pop()
    
    EulerCycle = []
    EulerCycle.insert(0, StrtNode)
    for Node in Cycle[::-1]:
        EulerCycle.append(Node)
    
    return EulerCycle[:-(k-1)]


def PathToGenome(EuPath):
    GenomePath = EuPath[0]
    for i in range(len(EuPath)-1):
        if EuPath[i][1:] == EuPath[i+1][:-1]:
            GenomePath += EuPath[i+1][-1]
    print(GenomePath)
    
    


def maxEdges(Graph):
    maxEdges = sum([len(x) for x in Graph.values()])
    return maxEdges

if __name__ == '__main__':
    PathToGenome(EulerianCycle(DeBruijnPatterns(universal_string(26)),26))