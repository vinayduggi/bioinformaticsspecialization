def Skew(Genome):
    skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'G':
            skew.append(skew[i]+1)
        elif Genome[i] == 'C':
            skew.append(skew[i]-1)
        else:
            skew.append(skew[i])
    return skew


E_Coli_Genome = open("E_coli.txt", "r")
Genome = E_Coli_Genome.read()
data = Skew(Genome)
#print(*data, sep = ' ')

pos = range(len(Genome)+1)
import matplotlib.pyplot as plt
plt.plot(pos, data)
plt.xlabel('E_Coli_Position')
plt.ylabel('Skew')
plt.show()