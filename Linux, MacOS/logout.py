#!/usr/bin/env python

from selenium import webdriver 
#from time import sleep 
  
#usr=input('Enter Email Id:')  
#pwd=input('Enter Password:')
#usr = '147157'
#pwd = 'pal#100900'  
  
logout_link = 'https://securelogin.pu.ac.in/cgi-bin/login?cmd=logout'
driver = webdriver.Firefox() 
driver.get(logout_link) 
print ("PU logout") 
#sleep(1) 
""" 
username_box = driver.find_element_by_id('user') 
username_box.send_keys(usr) 
print ("Username entered") 
#sleep(1) 
  
password_box = driver.find_element_by_id('password') 
password_box.send_keys(pwd) 
print ("Password entered") 
  
login_box = driver.find_element_by_name('Login') 
login_box.click() 
"""  
print ("Logout Successful") 
#sleep(1)
#input('Press anything to quit') 
driver.quit() 
print("Finished") 
