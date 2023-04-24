from behave import given, when, then
import time
from libraries.connection import connectionWeb, findByCSS
from selenium.common.exceptions import NoSuchElementException

protocol = "https://"
domain_web = "highlifeshop.com/speedbird-cafe"
#Word required in combo box in the fist visit.
word_first_time = "Position"

@given('Ingreso a la pagina')
def step_impl(context):
    #Conecction with ChromeDriver
    context.driver = connectionWeb()
    #Visit the web page
    context.driver.get(protocol + domain_web)

@when('hago click en el check')
def step_impl(context):
    #Find and click the cookie button
    context.element = findByCSS(context.driver, 'button.amgdprcookie-button')
    context.element.click()
    #Find the combo box
    context.element = findByCSS(context.driver, 'select.sorter-options')

@then('debe decir "Postion"')
def step_impl(context):
    #Compruebe the word required is present in the element
    try:
        assert word_first_time in context.element.text
        print("PASS")
        time.sleep(10)
    except NoSuchElementException:
        print("FAIL: The element is not present.")
        context.driver.quit()
    except AssertionError:
        print(f"FAIL: The element does not contain {word_first_time}.")
        context.driver.quit()
    
    context.driver.quit()
