#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:13:43 2017

@author: deepanshparab
"""


import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# All exceptions
from selenium.common.exceptions import TimeoutException



  
#make browser
ua=UserAgent()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (ua.random)
service_args=['--ssl-protocol=any','--ignore-ssl-errors=true']
# provide the path for the chrome driver
driver = webdriver.Chrome('/Users/deepanshparab/Desktop/Fall-2017-Cources/BIA-660A/WebAnalytics-BIA-660A-/week10/chromedriver',desired_capabilities=dcap,service_args=service_args)
  


def login(username,password):
    #access website
    driver.get('https://www.yelp.com/')
    
    #find and click login icon
    icon=driver.find_element_by_xpath('//*[@id="header-log-in"]/a')
    icon.click()
    
    
        #find and fill the email box
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
    
    passw = form.find_element_by_id('password')
    # own password
    passw.send_keys(password)


    
    #find and click the login button
    button=driver.find_element_by_xpath('//*[@id="ajax-login"]/button')
    time.sleep(2)
    button.click()
    
    
    time.sleep(3)
    
def submitReview(rev_text, rev_rating, restaurantID):

#    driver = init_driver()
    driver.get('https://www.yelp.com/biz/'+restaurantID)
#    driver.get('https://www.yelp.com/biz/'+restaurantID)
    time.sleep(5)
    
    
    review = driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div[1]/div/div[3]/div[2]/div/a')
    review.click()
    
    rating = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/form/div[1]/div/div[1]/div[1]/fieldset/ul')
    star_rating = 'rating-'+str(rev_rating)
    stars = rating.find_element_by_id(star_rating)
    stars.click()
    
    
    textbox = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/form/div[1]/div/textarea')
    textbox.clear()
    textbox.send_keys(rev_text)
    time.sleep(3)
    
    post = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/form/div[2]/div[2]/button')
    post.click()
    
def vote(userID):
    driver.get('https://www.yelp.com/user_details?userid='+userID)
    time.sleep(3)
    useful_icon = driver.find_element_by_xpath('//*[@id="super-container"]/div/div[2]/div/div[1]/div[2]/div/ul/li[1]/div/div[2]/div[2]/div[1]/ul/li[1]/a/span[2]')
    useful_icon.click()
    time.sleep(2)
    later = driver.find_element_by_xpath('//*[@id="yelp_main_body"]/div[8]/div/div[2]/div/div/div/div[3]/small')
    later.click()
    


def test(username,password,rev_text, rev_rating, restaurantID): 
    login(username,password)
    submitReview(rev_text, rev_rating, restaurantID)
    vote(userID)
    driver.quit()
    print('success')
    
    
    
if __name__=="__main__":
    username = 'dp27@email.com' 
    password = 'Sayali@25'
    rev_text = 'Visited dili junction last night. Great ambience, good food. Highly recommend Papri chat.'
    rev_rating = 4
    restaurantID = 'dilli-junction-hoboken-3'
    userID = 'fHyyjcdAfCF1nhDTtITTrw'
    test(username,password,rev_text, rev_rating, restaurantID)

    

    
