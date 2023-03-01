from random import randint

def EulerianCycle(Graph):
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
    
    EulerCycle = StrtNode + '->'
    for Node in Cycle[::-1]:
        EulerCycle += (Node + '->')
    print(EulerCycle.strip('->'))
    
    



with open('sample.txt', 'r') as file:
    Graph = dict((line.strip().split(' -> ') for line in file))
    for key in Graph:
        Graph[key] = Graph[key].split(',')


def maxEdges(Graph):
    maxEdges = sum([len(x) for x in Graph.values()])
    return maxEdges


if __name__ == '__main__':
    EulerianCycle(Graph)