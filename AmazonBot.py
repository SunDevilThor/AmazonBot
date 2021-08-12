# Amazon Bot
# Objective: Use browser automation to order an item from Amazon and have it delivered.

# WORK IN PROGRESS - NOT FINISHED YET

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import time
import config

url = ('http://amazon.com')

# Opens Amazon site
browser = webdriver.Chrome('/Users/thor/Downloads/chromedriver') # Optional argument, if not specified will search path.
browser.get(url)

# Sign into Amazon account
print('Signing into Amazon account')
sign_in = browser.find_element_by_id('nav-link-accountList')
sign_in.click()

browser.implicitly_wait(3)

enter_email = browser.find_element_by_id('ap_email')
enter_email.click()

enter_email.send_keys(config.email)

continue_button = browser.find_element_by_id('continue')
continue_button.click()

enter_pw = browser.find_element_by_id('ap_password')
enter_pw.click()

enter_pw.send_keys(config.pw)

sign_in_submit = browser.find_element_by_id('signInSubmit')
sign_in_submit.click()
print('Signed into account successfully')

search_item = 'chapstick'

search_box = browser.find_element_by_id('twotabsearchtextbox')
search_box.click()
print('Searching for item...')

search_box.send_keys(search_item)

search_submit = browser.find_element_by_id('nav-search-submit-button')
search_submit.click()

#Item: Blistex Medicated Lip Balm, 0.15 Ounce (Pack of 3)
browser.implicitly_wait(3)
chapstick = browser.find_element_by_link_text('Blistex Medicated Lip Balm, 0.15 Ounce (Pack of 3)')
chapstick.click()

# One-time purchase selection
one_time_purchase1 = browser.find_element_by_class_name('a-declarative')
one_time_purchase1.click()
print('Selected one-time purchase successfully')

done_button = browser.find_element_by_name('glowDoneButton')
done_button.click()
print('Clicked on DONE button successfully')

try:
    one_time_purchase = browser.find_element_by_id('newAccordionRow')
    one_time_purchase.click()
    one_time_purchase.click()
    one_time_purchase.click()
    print('Selected one-time purchase successfully AGAIN')

except Exception as error:
    browser.stop_client
    print('FAILED to select one time purchase')
    print(error)

try: 
    browser.implicitly_wait(5)
    add_to_cart = browser.find_element_by_id('add-to-cart-button')
    add_to_cart.click()
    print('Added item to cart')

except Exception as error:
    print('FAILED to add item to cart')
    print(error)

browser.implicitly_wait(5)
proceed_to_checkout = browser.find_element_by_id('hlb-ptc-btn-native')
proceed_to_checkout.click()

place_order = browser.find_element_by_name('placeYourOrder1')
place_order.click()
print('Order placed successfully!')