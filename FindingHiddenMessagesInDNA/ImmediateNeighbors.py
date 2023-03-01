def ImmediateNeighbors(Pattern):
    Neighborhood = []
    Nucleotides = ['A', 'C', 'T', 'G']
    for i in range(len(Pattern)):
        symbol = Pattern[i]
        for x in Nucleotides:
            if x != symbol:
                Neighbor = Pattern[:i] + x + Pattern[i+1:]
                Neighborhood.append(Neighbor)
    return Neighborhood


Pattern = 'CAA'
print(ImmediateNeighbors(Pattern))