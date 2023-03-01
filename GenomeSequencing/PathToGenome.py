# Code for string reconstruction from a set of k-mers (first k-mer for the string is known here)

def PathToGenome(Kmers):
    GenomePath = Kmers[0]
    for i in range(len(Kmers)-1):
        if Kmers[i][1:] == Kmers[i+1][:-1]:
            GenomePath += Kmers[i+1][-1]
    return GenomePath


Kmers_in = open('dataset_198_3.txt','r')
Kmers = Kmers_in.read().split()

if __name__ == '__main__':
    PathToGenome(Kmers)