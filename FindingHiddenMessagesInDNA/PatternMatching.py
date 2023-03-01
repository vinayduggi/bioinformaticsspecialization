def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return(positions)


Vibrio_Cholorae= open("Vibrio_Cholorae_Genome.txt", "r")
Genome = Vibrio_Cholorae.read()
Pattern = 'CTTGATCAT'
data = PatternMatching(Pattern, Genome)
print(*data)