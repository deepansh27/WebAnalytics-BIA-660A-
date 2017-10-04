#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 19:05:08 2017

@author: deepanshparab
"""
import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load
from collections import Counter

def getPOSterms(terms, POStags, tagger):
    tagged_terms = tagger.tag(terms) #do POS tagging on the tokenized sentence

    POSterms = {}
    for tag in POStags: POSterms[tag] = set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])

    return POSterms

def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
   
    for line in lex_conn:
        newLex.add(line.strip())
    lex_conn.close()

    return newLex

posLex=loadLexicon('positive-words.txt')
negLex=loadLexicon('negative-words.txt')

_POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
tagger = load(_POS_TAGGER)
sentence = "not a good idea to do things, not a bad idea"



def processSentence(sentence,posLex,negLex,tagger):
    
    terms = nltk.word_tokenize(sentence)
    POStags=['NN']
    
    POSterms=getPOSterms(terms,POStags,tagger)
    nouns = POSterms['NN']
    
    solution = []
    
    fourGrams = ngrams(terms, 4) #compute 4-grams
    for tag in fourGrams: #for each 4gram
        if tag[0] == 'not' and (tag[2] in posLex or tag[2] in negLex) and tag[3] in nouns: # checking for the condition 
            solution.append(tag)
    
    return solution

def getTop3(D):
    
    keys = []
    dictCounter = Counter(D)
    
    for key, value in dictCounter.most_common(3):    #using .most_common(3) we get the top 3 max values for our keys
        keys.append(key)
    
    return keys
    

#print(processSentence(sentence,posLex,negLex,tagger))
#print(getTop3({'a':12,'b':22,'c':45,'d':54,'e':54}))


    
    
    




