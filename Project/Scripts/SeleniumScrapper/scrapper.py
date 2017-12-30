from Project.Scripts.SeleniumScrapper.SeleniumScrapper import Scraper

username = 'mastani.bajirao@hotmail.com'
password = 'gmail@123'


scr = Scraper(username, password)

query = raw_input("what do you want to search? ")

location = raw_input(" where do you want to find it ?")

########### logins into yelp #################
scr.login(scr.driver, username, password)

############## extracts Restaurant Reviews from Yelp ####################
scr.ScrapRestro(query, location, scr.driver)

############### extracts Restaurant Menus from Yelp ####################
scr.ScrapMenu(query, location, scr.driver)

