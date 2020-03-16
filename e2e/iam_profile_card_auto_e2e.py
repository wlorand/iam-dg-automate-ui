# FILE: iam_profile_card_auto_e2e.py
# DESC: use Selenium + Python to automate IAM Profile Card User Interactions in E2E
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException, NoSuchElementException

# ---------- ---------- ---------- ---------- ---------- 
# CONSTANTS
# ---------- ---------- ---------- ---------- ----------
WAIT_TIMEOUT = 30 
IAM_AUTH_URL_E2E = 'https://accounts-e2e.intuit.com/'
TEST_USERNAME = 'iamtestpass_1584036796995' 
TEST_USERPASS = 'Intuit01-'

# ---------- ---------- ---------- ---------- ---------- 
# BROWSER-SPECIFIC WEB DRIVERS
# ---------- ---------- ---------- ---------- ---------- 

# FIREFOX - geckodriver
# browser = webdriver.Firefox()

# CHROME chromedriver (80)
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" 
chrome_driver_binary = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

# ---------- ---------- ---------- ---------- ----------  
# UTILITY METHODS
# ---------- ---------- ---------- ---------- ----------

def wait_for_elem_select(selector):
    return WebDriverWait(browser, WAIT_TIMEOUT).until(lambda browser: browser.find_element_by_css_selector(selector))

# ---------- ---------- ---------- ---------- ---------- 
# SCRIPT LOGIC 
# ---------- ---------- ---------- ---------- ----------

# Tests IAM Profile Card User Interactions
while True:
    try:
        browser.get(IAM_AUTH_URL_E2E)
        browser.maximize_window()

        # 1.1: Enter User/Pass
        wait_for_elem_select('#ius-userid').send_keys(TEST_USERNAME)
        wait_for_elem_select('#ius-password').send_keys(TEST_USERPASS)

        # 1.2: Click Sign-In Button
        sleep(3)
        wait_for_elem_select('button[name="SignIn"]').click()

        # 1.3: Confirm IAM Cards Overview Page Loaded
        sleep(8)
        assert 'Intuit Accounts - Account Manager' in browser.title 
        
        # 2.0: Click Personal Info (Profile), Edit on Name sub-widget
         


    except TimeoutException:
        print("Oops - got a TimeoutException...let's try again")
        continue 
    except NoSuchElementException:
        print("Drat - DOM Element Not Found -- Time to Die!")
        break
    else:
        print("Script ran with No Exceptions")
    finally:
        # Cleanup 
        print("About to close the browser")
        sleep(20)
        browser.close()
        break