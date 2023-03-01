from collections import defaultdict

def ClumpFind(Genome, k, L, t):
    clump_dict = defaultdict(list)
    clumps = set()

    for pos in range(len(Genome) - k + 1):
        current_pos = Genome[pos:pos + k]
        clump_dict[current_pos].append(pos)
        if len(clump_dict[current_pos]) >= t:
            if ((clump_dict[current_pos][-1] + (k - 1)) - clump_dict[current_pos][-t]) < L:
                clumps.add(current_pos)

    return clumps


E_Coli_Genome = open("E_coli.txt", "r")
Genome = E_Coli_Genome.read()
k = 9
L = 500
t = 3
data = ClumpFind(Genome, k, L, t)
print(*data)
