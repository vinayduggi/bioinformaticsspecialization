from DeBruijnText import DeBruijnText
from collections import defaultdict, Counter
from itertools import chain
from random import randint

def StringReconstruction(Kmers):
    DeBruijn = DeBruijnPatterns(Kmers)
    EulerPath = EulerianPath(DeBruijn)
    String = PathToGenome(EulerPath)
    print(String)


def DeBruijnPatterns(Kmers):
    k = len(Kmers[0])
    debruijn_patterns = defaultdict(list)
    for edge in Kmers:
        if edge[:k-1] not in debruijn_patterns:
            debruijn_patterns[edge[:k-1]] = []
        debruijn_patterns[edge[:k-1]].append(edge[1:])
    
    return debruijn_patterns


def EulerianPath(Graph):
    return EulerianCycle(Graph)



def EulerianCycle(Graph):
    maxEdge = maxEdges(Graph)
    StrtNode, EndNode = StrtEndNode(Graph)
    CurrNode = StrtNode
    Stack = []
    Cycle = []
    while len(Cycle) != maxEdge:
        if CurrNode != EndNode and Graph[CurrNode] != []:
            Stack.append(CurrNode)
            NexNode = randint(0,len(Graph[CurrNode])-1)
            PrevNode = CurrNode
            CurrNode = Graph[PrevNode][NexNode]
            Graph[PrevNode].remove(CurrNode)
        else:
            Cycle.append(CurrNode)
            CurrNode = Stack[len(Stack)-1]
            Stack.pop()
    
    EulerCycle = []
    EulerCycle.insert(0, StrtNode)
    for Node in Cycle[::-1]:
        EulerCycle.append(Node)
    
    return EulerCycle


def StrtEndNode(Graph):
    TotalInDegrees = Counter(chain(*Graph.values()))
    TotalOutDegrees = {k:len(v) for k, v in Graph.items()}
    if len(TotalInDegrees) > len(TotalOutDegrees):
        IndegreesLst = list(TotalInDegrees.keys())
        for Node in IndegreesLst:
            if Node in TotalOutDegrees:
                if TotalOutDegrees[Node] > TotalInDegrees[Node]:
                    StrtNode = Node
            else:
                EndNode = Node
    elif len(TotalInDegrees) < len(TotalOutDegrees):
        IndegreesLst = list(TotalOutDegrees.keys())
        for Node in IndegreesLst:
            if Node in TotalInDegrees:
                if TotalInDegrees[Node] > TotalOutDegrees[Node]:
                    EndNode = Node
            else:
                StrtNode = Node
    else:
        IndegreesLst = list(TotalInDegrees.keys())
        OutdegreesLst = list(TotalOutDegrees.keys())
        for Node in OutdegreesLst:
            if Node in TotalInDegrees:
                if TotalOutDegrees[Node] > TotalInDegrees[Node]:
                    StrtNode = Node
            else:
                StrtNode = Node
        for Node in IndegreesLst:
            if Node in TotalOutDegrees:
                if TotalInDegrees[Node] > TotalOutDegrees[Node]:
                    EndNode = Node
            else:
                EndNode = Node
    
    return StrtNode, EndNode

def maxEdges(Graph):
    maxEdges = sum([len(x) for x in Graph.values()])
    return maxEdges


def PathToGenome(EuPath):
    GenomePath = EuPath[0]
    for i in range(len(EuPath)-1):
        if EuPath[i][1:] == EuPath[i+1][:-1]:
            GenomePath += EuPath[i+1][-1]
    return GenomePath

Kmers_in = open('dataset_203_73.txt','r')
Kmers = Kmers_in.read().split()



if __name__ == '__main__':
    StringReconstruction(Kmers)
