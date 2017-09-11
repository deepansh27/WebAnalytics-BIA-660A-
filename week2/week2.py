"""
Week 2
The script defines a function run(). The function accepts as input the path to a text file and 2 words. It then returns the number of times that each 
word appears in the file.
"""

#define a new function
def run(path,word1,word2):
    freq={} # new dictionary. Maps each word to each frequency 
	
    #initialize the frequency of the two words to zero.
    freq[word1]=0
    freq[word2]=0
    Word1_lineCounter = 0
    Word2_lineCounter = 0

    fin=open(path) # open a connection to the file 
    for line in fin: # read the file line by line 
        # lower() converts all the letters in the string to lower-case
        # strip() removes blank space from the start and end of the string
        # split(c) splits the string on the character c and returns a list of the pieces. For example, "A1B1C1D".split('1')" returns [A,B,C,D] 
     
        words=line.lower().strip().split(' ')
       
        # use for to go over all the words in the list 
        for word in words: # for each word in the line
            if word==word1:
                Word1_lineCounter = Word1_lineCounter + 1
#                freq[word1]=freq[word1]+1 # if the word is word1, then increase the count of word1 by 
            elif word==word2: 
#                freq[word2]=freq[word2]+1
                Word2_lineCounter = Word2_lineCounter + 1# if the word is word2, then increase the count of word2 by 1
    fin.close() #close the connection to the text file 

    return Word1_lineCounter,Word2_lineCounter


# use the function 
print(run('textfile','house','blue'))
#print(run('textfile','name','kate'))







