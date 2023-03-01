# Code for splitting a string text into k-mers of given length
def StringComposition(Text, k):
    Kmer = []
    for i in range(len(Text)-k+1):
        Compo = Text[i:i+k]
        Kmer.append(Compo)
    return Kmer


StringText= open("dataset_197_3.txt", "r")
Text = StringText.readline()
k = 100


Kmers = '\n'.join(StringComposition(Text, k))   # convert list to text with new line in-between
data_out = open("dataset_197_3_output.txt", "w")
data_out.write(Kmers)
data_out.close()
