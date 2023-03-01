'''
1) PatternCount(Text, Pattern) as the number of times that a k-mer Pattern....
appears as a substring of Text.
'''

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1): #range of 'sliding window'
        if Text[i: i+len(Pattern)] == Pattern: #if given pattern input matches the text window
            count = count + 1
    return count


oriC= open("oriC_Vibrio_Cholerae.txt", "r")
Text = oriC.read()
Pattern = 'TGATCA'
print(PatternCount(Text, Pattern))