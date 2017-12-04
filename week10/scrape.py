#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:10:45 2017

@author: deepanshparab
"""

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



    
#make browser
ua=UserAgent()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (ua.random)
service_args=['--ssl-protocol=any','--ignore-ssl-errors=true']
driver = webdriver.Chrome('chromedriver',desired_capabilities=dcap,service_args=service_args)


#access website
driver.get('https://www.yelp.com/')

#find and click login icon

#//*[@id="header-log-in"]/a
icon=driver.find_element_by_xpath('//*[@id="header-log-in"]/a')
icon.click()


#find and fill the email box
form = driver.find_element_by_id('ajax-login')

try:
    myElem = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ajax-login"]/button')))
except TimeoutException:
    print('Looking took much longer')
email = form.find_element_by_id('email')
email.send_keys('dp27@email.com')
WebDriverWait(driver,10)

#find and fill the password box
password = form.find_element_by_id('password')
password.send_keys('Sayali@25')
WebDriverWait(driver,10)

#find and click the login button
button=driver.find_element_by_xpath('//*[@id="ajax-login"]/button')
button.click()


#restro in hoboken

try:
    myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header-search-submit"]')))
except TimeoutException:
    print ("Loading took too much time!")
    
search = driver.find_element_by_id("find_desc")
search.send_keys('Indian Restaurants')
WebDriverWait(driver,10)

city = driver.find_element_by_id("dropperText_Mast")
city.send_keys("Newyork city, NY")
WebDriverWait(driver,10)
#find and click the search button
searchBtn = driver.find_element_by_id("header-search-submit")
searchBtn.click()


try:
    myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/div[1]/div/div/div[1]')))
except TimeoutException:
    print ("Loading took too much time!")

restro_names = driver.find_elements_by_class_name('indexed-biz-name')

for name in restro_names:
    print(name.text)

driver.quit()





