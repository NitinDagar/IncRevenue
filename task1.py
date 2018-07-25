'''
@author = Nitin Dagar
Date = 25/07/2018
description:- IncRevenue Task 1
video link is not given in mail so it is just a trending song from youtube
'''


from   selenium import webdriver

browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.maximize_window()
browser.get("https://www.youtube.com/watch?v=PjTU0DmBWiU")

