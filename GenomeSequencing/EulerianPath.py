from collections import Counter
from itertools import chain
from random import randint

def EulerianPath(Graph):
    EulerianCycle(Graph)



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
    
    EulerCycle = StrtNode + '->'
    for Node in Cycle[::-1]:
        EulerCycle += (Node + '->')
    print(EulerCycle.strip('->'))


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


with open('dataset_203_63.txt', 'r') as file:
    Graph = dict((line.strip().split(' -> ') for line in file))
    for key in Graph:
        Graph[key] = Graph[key].split(',')


if __name__ == '__main__':
    EulerianPath(Graph)
    #StrtEndNode(Graph)