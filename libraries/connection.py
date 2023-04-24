from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def connectionWeb():
    '''The function creates a new instance of the Chrome and return [driver].'''
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def findByCSS(driver,selector):
    '''This function is used to locate an element on a webpage using a CSS selector and returns it [element].
    Takes two arguments, a [driver] and [selector]. To obtein a [driver] use the function connectionWeb().'''
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    return element

