# Amazon Bot
# Use browser automation to order an item from Amazon and have it delivered.

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import time

url = ('http://amazon.com')

# Opens Amazon site
browser = webdriver.Chrome('/Users/thor/Downloads/chromedriver') # Optional argument, if not specified will search path.
browser.get(url)

search_item = 'eye drops'

search_box = browser.find_element_by_id('twotabsearchtextbox')
search_box.click()

search_box.send_keys(search_item)

search_submit = browser.find_element_by_id('nav-search-submit-button')
search_submit.click()

#Item: /Systane-Ultra-Lubricant-Drops-10-mL/dp/B0036B8QL0/
try: 
    time.sleep(3)
    systane_eyedrops = browser.find_element_by_link_text('Systane Ultra Lubricant Eye Drops, Twin Pack, 10-mL Each,packaging may vary')
    print("found linked text")
    systane_eyedrops.click()
    
    

except Exception as error:
    print("Failed: ", error)

add_to_cart = browser.find_element_by_id('add-to-cart-button')
add_to_cart.click()

proceed_to_checkout = browser.find_element_by_id('hlb-ptc-btn-native')
proceed_to_checkout.click()


enter_email = browser.findfind_element_by_id('ap_email')
enter_email.click()













