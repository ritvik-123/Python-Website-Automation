from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('http://thedemosite.co.uk/addauser.php')
user_input_1 = chrome_browser.find_element_by_name('username')
user_input_2 = chrome_browser.find_element_by_name('password')
user_input_1.send_keys('ritvik123')
user_input_2.send_keys('Tannushree2010')
button = chrome_browser.find_element_by_name('FormsButton2')
button.click()
x = input('hi')
print(x)
