#!python3

from selenium import webdriver
b = webdriver.Firefox()
b.get('http://web.whatsapp.com')
input()
elem = b.find_element_by_xpath('//span[contains(text(),"Saurabh G")]')
elem.click()
elem1 = b.find_elements_by_class_name('input')
counter =0
while counter < 5:
    counter= counter +1
    elem1[1].send_keys('Your whatsapp is hacked')
    b.find_element_by_class_name('send-container').click()