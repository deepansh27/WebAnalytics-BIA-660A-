#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:37:12 2017

@author: deepanshparab
"""
# all the pacakages required for the code
from bs4 import BeautifulSoup
import os
import sys
import codecs


class ExtractReviews(object):

    ##########################################################################################################################################
    ##########################################################################################################################################
    '''
    In this function returns a dictionary which contains restro folder name as its key and the scrapped html pages as its values
    eg : {'FishmarketRestaurant.txt': [reviewpage_1.txt,reviewpage_2.txt,reviewpage_3.txt,reviewpage_4.txt,reviewpage_5.txt,reviewpage_6.txt,reviewpage_7.txt,
    reviewpage_8.txt,reviewpage_9.txt,reviewpage_12.txt,reviewpage_13.txt,reviewpage_14.txt,reviewpage_15.txt,reviewpage_16.txt,
    reviewpage_17.txt,reviewpage_18.txt,reviewpage_19.txt]}
    '''

    def __init__(self, inputdir, outputdir):
        self.inputdir = inputdir
        self.outputdir = outputdir


    def readRestaurant(self, inputdir):
        restro= {}
        for restroName in os.listdir(inputdir):
            if restroName =='.DS_Store':
                continue
            else:
                folder = os.path.join(inputdir,restroName)
                for reviews in os.listdir(folder):
                    restro.setdefault(restroName,[]).append((str(os.path.join(folder,reviews))))
        return restro

    ##########################################################################################################################################
    ##########################################################################################################################################
    '''
    The function accepts input and output dir paths as parameters and creates a text files of the restro withs all the extracted reviews for that restro
    
    '''
    def extractRestaurant(self,inputpath,outputpath):
        restro = self.readRestaurant(inputpath)
        reviews_counter= 0
        for k,v in restro.items():
            k = k.replace(" ",'')
            filename = outputpath+'/'+str(k)+'.txt'
            try:
                restro_name = codecs.open(filename, 'a', encoding='UTF-8')
            except IOError:
                print ("Could not read file:", filename)
                sys.exit()
            for files in v:
                try:
                    html = open(files,'r')
                except IOError:
                    print ("Could not read file:", files)
                    sys.exit()
                soup = BeautifulSoup(html,'xml')

                reviews = soup.findAll('div', {'class':'review-content'})

                for review in reviews:
                    review_content = review.find('p',{'lang':'en'})
                    data = review_content.text
                    restro_name.write(data)
                    restro_name.write('\n')
                    reviews_counter = reviews_counter+1

            restro_name.close()
            print('Reviews successfully wrote in file '+k)
        print("total reviews extracted: "+str(reviews_counter))


