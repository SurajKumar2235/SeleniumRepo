from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
drive = webdriver.Firefox()
# drive.maximize_window()
today=datetime.now()
drive.get('https://www.amazon.in/')
try:
    ## source code
    source_code=drive.page_source
#    print(source_code)

    title=drive.title
    print(title)

    url=drive.current_url
    print(url)

    print(drive.get_window_rect)
    print(drive.get_downloadable_files)
    print(drive.get_window_size)
    print(drive.get_window_position)
    print(drive.get_full_page_screenshot_as_png)


finally:
    print('succ')
    WebDriverWait(drive,60)
    print(time.time())
    print(today)
    time.sleep(5)
    drive.close()
    drive.quit()