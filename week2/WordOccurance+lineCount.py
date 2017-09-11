
# To count the number of times a given word occured in a given line 

def wordInLineOccurance(path, word1):
    freq = {}
    
    input_file = open(path, 'r')
    data = input_file.readlines()
    line_counter = 0
    for lines in data:
        freq[word1]= 0
        words = lines.strip().split(" ")
        line_counter += 1
        for word in words:
            if word1 in word:
                freq[word1]+=1
        print(" In line %s the word %s occured %r number of times"%(line_counter,word1,freq[word1]))


wordInLineOccurance('/Users/deepanshparab/Desktop/Fall-2017-Cources/BIA-660/week2/textfile','yellow')      



# To count the occurance of each word in a given line

def wordOccurance(path):
    freq = {}
    input_file = open(path, 'r')
    data = input_file.readlines()
    line_counter = 0
    for lines in data:
        words = lines.strip().split(" ")
        line_counter += 1
        for word in words:
            freq.setdefault(word, 0)
            freq[word]+=1
        print(" In line %d  : "%line_counter)
        for k,v in freq.items():
            print(" the word %s occured %r number of times "%(k,v))

path= '/Users/deepanshparab/Desktop/Fall-2017-Cources/BIA-660/week2/textfile'
wordOccurance(path)
      
    
 