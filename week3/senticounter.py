#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:49:46 2017

@author: deepanshparab
"""

def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
   
    for line in lex_conn:
        newLex.add(line.strip())
    lex_conn.close()

    return newLex

def run(path):
    posLex=loadLexicon('/Users/deepanshparab/Desktop/Fall-2017-Cources/BIA-660A/WebAnalytics-BIA-660A-/week3/positive-words.txt')
    positive_word_counter = {}
 
    fin=open(path)
    for line in fin: 
        
        line=line.lower().strip()   
        exists_counter = 0
        
        words=line.split(' ') 
        for word in words: #for every word in the review
            
            if word in posLex and exists_counter==0:
                positive_word_counter.setdefault(word,0)  #set a default value of each word
                positive_word_counter[word]+=1  # increaments the value of the key if the word appears in list of positive words
                exists_counter=1 # to avoid redundancy
        
    fin.close()
    return positive_word_counter



if __name__ == "__main__": 
    positive_words_in_reviews=run('/Users/deepanshparab/Desktop/Fall-2017-Cources/BIA-660A/WebAnalytics-BIA-660A-/week3/textfile')
    for keys,values in positive_words_in_reviews.items():
        if values > 0:
            print("%s appears %d reviews"%(keys,values))
    