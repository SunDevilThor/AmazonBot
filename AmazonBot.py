# Amazon Bot
# Objective: Use browser automation to order an item from Amazon and have it delivered.

# WORK IN PROGRESS - NOT FINISHED YET

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import time

url = ('http://amazon.com')

# Opens Amazon site
browser = webdriver.Chrome('/Users/thor/Downloads/chromedriver') # Optional argument, if not specified will search path.
browser.get(url)

search_item = 'chapstick'

search_box = browser.find_element_by_id('twotabsearchtextbox')
search_box.click()

search_box.send_keys(search_item)

search_submit = browser.find_element_by_id('nav-search-submit-button')
search_submit.click()

#Item: Blistex Medicated Lip Balm, 0.15 Ounce (Pack of 3)
browser.implicitly_wait(3)
chapstick = browser.find_element_by_link_text('Blistex Medicated Lip Balm, 0.15 Ounce (Pack of 3)')
chapstick.click()

# One-time purchase selection
try:
    one_time_purchase = browser.find_element_by_link_text('One-time purchase:')
    one_time_purchase.click()
    print('Selected one-time purchase successfully')

except Exception as error: 
    print(error)


try:
    browser.implicitly_wait(3)
    add_to_cart = browser.find_element_by_id('add-to-cart-button')
    add_to_cart.click()
    print('Added item to cart')

except Exception as error: 
    print(error)
 
try:
    browser.implicitly_wait(3)
    proceed_to_checkout = browser.find_element_by_id('hlb-ptc-btn-native')
    proceed_to_checkout.click()

except Exception as error: 
    print(error)

enter_email = browser.findfind_element_by_id('ap_email')
enter_email.click()













