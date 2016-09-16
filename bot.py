#!python3

# To use this script first download selenuim through your terminal or command line
from selenium import webdriver
# Getting webdriver for firefox 
b = webdriver.Firefox()
# Requesting the web version of whatsapp
b.get('http://web.whatsapp.com')
input()
elem = b.find_element_by_xpath('//span[contains(text(),"Friend's Name)]')
elem.click()
elem1 = b.find_elements_by_class_name('input')
counter =0
# Change the counter limit in while loop to send the message at your limit or times
while counter < 100:
    counter= counter +1
    # Change the message of your own choice
    elem1[1].send_keys('Your whatsapp is hacked')
    b.find_element_by_class_name('send-container').click()
