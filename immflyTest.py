import time
from libraries.connection import connectionWeb, findByCSS

#Test case Number 1 - Verify that the combo box has a default selected value ("Position"). 

protocol = "https://"
domain_web = "highlifeshop.com/speedbird-cafe"

#Word required in combo box in the fist visit.
word_first_time = "Position"

#Conecction with ChromeDriver
driver = connectionWeb()

#Visit the web page
driver.get(protocol + domain_web)

element = findByCSS(driver, 'button.amgdprcookie-button')
element.click()
element = findByCSS(driver, 'select.sorter-options')

#Compruebe the word required is present in the element
try:
    if word_first_time in element.text:
        print("PASS")
        time.sleep = 10
    else:
        print(f"FAIL:The element do not contain {word_first_time}.")
        driver.quit()
except:
    print("FAIL:The element is not present.")
    driver.quit()

