'''
@author = Nitin Dagar
Date = 25/07/2018
description:- IncRevenue Task 2
'''


from   selenium import webdriver

# below are the lists of indian cities with free ip servers
ips = [['mumbai','220.227.70.45:8080'],['delhi','103.65.30.86:53281'],['chennai','103.240.103.67:8080'],['bangalore','159.89.166.149:3128'],['hyderabad','202.62.84.210:53281']]
options = webdriver.ChromeOptions()


#loop for opening the webpage with different ip addresses
for ip in ips:
    options.add_argument(f'--proxy-server={ip[1]}')  
    browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
    browser.get("http://buzfeeed1.blogspot.com/2018/07/test-question.html")

