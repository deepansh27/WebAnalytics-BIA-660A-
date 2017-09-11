#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:50:31 2017

@author: deepanshparab
"""

"""
Week 2
Modified the code to count the number of lines a word occured in 
"""

#define a new function
def run(path,word1,word2):
    freq={} # new dictionary. Maps each word to each frequency 
    word1_lines = 0
    word2_lines = 0
    #initialize the frequency of the two words to zero.
    freq[word1]=0
    freq[word2]=0
    
    fin=open(path) # open a connection to the file 
    for line in fin: # read the file line by line 
        counter_word1 =0
        counter_word2=0
        words=line.lower().strip().split(' ')
       
        # use for to go over all the words in the list 
        for word in words: # for each word in the line
            if word==word1 and counter_word1==0: 
                freq[word1]=freq[word1]+1 # if the word is word1, then increase the count of word1 by
                word1_lines = word1_lines + 1
                counter_word1=1 
            elif word==word2 and counter_word2==0: 
                freq[word2]=freq[word2]+1 # if the word is word2, then increase the count of word2 by 1
                word2_lines = word2_lines + 1
                counter_word2=1

    print("word1 occured in :"+str(word1_lines))
    print("word2 occured in :"+str(word2_lines))
    fin.close() #close the connection to the text file 

    return word1,freq[word1]


# use the function 
print(run('/Users/deepanshparab/Desktop/Fall-2017-Cources/BIA-660/week2/textfile','house','yellow'))


