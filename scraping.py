from selenium import webdriver
from selenium.webdriver.common.by import By
drive = webdriver.Firefox()
# drive.maximize_window()

drive.get('https://www.amazon.in/')
try:
    
    # input=drive.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
    # input.send_keys('one')
    input=drive.find_element(By.CLASS_NAME,'nav-input').send_keys('moto')
    
    search=drive.find_element(By.ID,'nav-search-submit-button').click()
    

finally:
    print('succ')
    # drive.quit()
# search=drive.find_element()