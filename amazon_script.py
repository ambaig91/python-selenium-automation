from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(4)

driver.get('https://www.amazon.com/gp/help/customer/display.html')

search_field = driver.find_element(By.ID, 'helpsearch')
search_field.send_keys('Cancel Order')
search_field.send_keys(Keys.RETURN)

actual_text = driver.find_element(By.XPATH, "//a[contains(@href, 'GSL37WQTJZUYA9QE')]").text
expected_text = 'Cancel Items or Orders'

assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

driver.quit()

