#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:03:17 2017

@author: deepanshparab
"""
# selenium packages
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# All exceptions
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import errno
import codecs



# extraction and scrapping packages
from bs4 import BeautifulSoup
import os
import re

class Scraper(object):
    ##########################################################################################################################################
    ##########################################################################################################################################
    def __init__(self,username,password):
        self.username = username
        self.passwrd = password
        ua = UserAgent()
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (ua.random)
        service_args = ['--ssl-protocol=any', '--ignore-ssl-errors=true']
        # provide the path for the chrome driver
        chrome_path = r'/Users/deepanshparab/Desktop/Projects/Bia-660/Project/chromedriver'
        driver = webdriver.Chrome(executable_path=chrome_path, desired_capabilities=dcap, service_args=service_args)
        self.driver = driver

    ##########################################################################################################################################

    @staticmethod
    def login(driver, username, passwrd):
        #access website
        driver.get('https://www.yelp.com/')

        #find and click login icon
        icon=driver.find_element_by_xpath('//*[@id="header-log-in"]/a')
        icon.click()


        #find and fill the login credientials
        form = driver.find_element_by_id('ajax-login')
        try:
            myElem = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ajax-login"]/button')))
        except TimeoutException:
            print('Looking took much longer')
        email = form.find_element_by_id('email')
        # you can use your own mail id if you have
        email.send_keys(username)

        time.sleep(2)
        #find and fill the password box
        password = form.find_element_by_id('password')
        # own password
        password.send_keys(passwrd)


        #find and click the login button
        button=driver.find_element_by_xpath('//*[@id="ajax-login"]/button')
        time.sleep(2)
        button.click()
        time.sleep(2)


    ##########################################################################################################################################
    def ScrapRestro(self, query, location, driver):

        #indian restro in nyc
        try:
            myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header-search-submit"]')))

            search = driver.find_element_by_id("find_desc")
            search.send_keys(query)
            time.sleep(2)
            city = driver.find_element_by_id("dropperText_Mast")
            city.click()
             # Find the search box
            city.send_keys(Keys.DELETE + location)
            time.sleep(2)
            #find and click the search button
            searchBtn = driver.find_element_by_id("header-search-submit")
            time.sleep(2)
            searchBtn.click()

        except TimeoutException:
            print ("Loading took too much time!")


    #    While condition is used to check if a given webpage has <Next> icon to go from one web page to other..
    #    This is the outer while loop which runs through various restro in NYC....till have <Next> icon

        outer_condition = 1
        outer_loop = 0
        while outer_condition == 1:

            html = driver.page_source
            print(driver.current_url)
            main_url= driver.current_url
            time.sleep(1)
            soup = BeautifulSoup(html,'lxml')
            links = soup.find_all("h3",{"class":"search-result-title"}) #links to all the restro on a given page
            for link in links[1:]:
                res_name = ''.join(map(lambda x: x.strip(), link.strings)) # fetches all the restro names
                dir_name = self.MkResDir(res_name) # creating directory
                res_url = 'https://www.yelp.com/' + link.find('a').get('href') # create a URL's for the above fetched restro
                if not re.search('adredir',res_url): # the if condition is used to filter out all ads
                    driver.get(res_url)
                    time.sleep(1)

                    inner_condition = 1
                    inner_loop = 0
                    while inner_condition == 1:
                         try:
                            continue_link = driver.find_element_by_partial_link_text('Next')
                            continue_link.click()
                            time.sleep(3)
                            page = driver.page_source
                            # code for putting the data into the file
                            inner_loop = inner_loop +1
                            self.WriteFiles(dir_name, page, inner_loop)
                            print('Review '+str(inner_loop)+' Created')

                         except(NoSuchElementException, StaleElementReferenceException) as e:
                             inner_condition = 0

                         print(driver.current_url)
                         print(inner_loop)


                    print('done with restro %r'%(res_name))


            driver.get(main_url)
            time.sleep(3)
            try:
                continue_link = driver.find_element_by_partial_link_text('Next')
                continue_link.click()
                time.sleep(2)
                outer_loop = outer_loop +1

            except (NoSuchElementException, StaleElementReferenceException) as e:
                outer_condition = 0

            print(outer_loop)


    ##########################################################################################################################################

    def ScrapMenu(self, query, location, driver):
        # example Indian Restaurant in NewYork,NY
        try:
            myElem = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="header-search-submit"]')))

            search = driver.find_element_by_id("find_desc")
            search.send_keys(query)
            time.sleep(2)
            city = driver.find_element_by_id("dropperText_Mast")
            city.click()
            # Find the search box
            city.send_keys(Keys.DELETE + location)
            time.sleep(2)
            # find and click the search button
            searchBtn = driver.find_element_by_id("header-search-submit")
            time.sleep(2)
            searchBtn.click()
        except TimeoutException:
            print ("Loading took too much time!")

        outer_condition = 1
        while outer_condition == 1:

            html = driver.page_source
            print(driver.current_url)
            main_url = driver.current_url
            time.sleep(1)
            soup = BeautifulSoup(html, 'lxml')
            links = soup.find_all("h3", {"class": "search-result-title"})  # links to all the restro on a given page

            for link in links[1:]:
                res_name = ''.join(map(lambda x: x.strip(), link.strings))  # fetches all the restro names
                res_url = 'https://www.yelp.com/' + link.find('a').get(
                    'href')  # create a URL's for the above fetched restro
                if not re.search('adredir', res_url):  # the if condition is used to filter out all ads
                    driver.get(res_url)
                    time.sleep(1)
                file = codecs.open('/Users/deepanshparab/Desktop/Projects/Bia-660/Project/Menus/menus.txt', 'a', encoding='UTF-8')
                try:
                    menu = driver.find_element_by_partial_link_text('View the full menu')
                    menu.click()
                    print(driver.current_url)
                    time.sleep(3)
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'lxml')
                    divs = soup.find_all("div", {
                        "class": "arrange_unit arrange_unit--fill menu-item-details"})  # links to all the restro on a given page
                    for div in divs:
                        review_content = div.find('h4')
                        menus = str(review_content.text).replace('\n', '')
                        menus = menus.replace('  ', '')
                        file.write(menus)
                        file.write('\n')

                    print('menus added to set for restro: ', res_name)
                    file.close()

                except(NoSuchElementException, StaleElementReferenceException) as e:
                    print('menu link not found')

            driver.get(main_url)
            time.sleep(3)
            try:
                continue_link = driver.find_element_by_partial_link_text('Next')
                continue_link.click()
                time.sleep(2)

            except (NoSuchElementException, StaleElementReferenceException) as e:
                outer_condition = 0


    ##########################################################################################################################################

    @staticmethod
    def MkResDir(resname):
        base_path = '/Users/deepanshparab/Desktop/Projects/Bia-660/Project/ScrappedData'
        filename = base_path+'/Indian/'+resname

        if not os.path.exists((filename)):
            try:
                os.makedirs(filename)
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    print('dir not found')
        return filename
    ##########################################################################################################################################

    @staticmethod
    def WriteFiles(filename, page, number):
        reviewfile = str(filename+'/'+'reviewpage_'+str(number))+'.txt'
        if not os.path.exists(reviewfile):
            try:
                filename = codecs.open(reviewfile,'w', encoding="utf-8")
                filename.write(page)
                filename.close()
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    print('dir not found')

    ##########################################################################################################################################
    ##########################################################################################################################################


    


    



   

