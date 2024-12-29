#Progam: To open Nopcommerce web application and do basic actions in it
#programmer name: Hari Prasad>K
#Date: 29-DEC-2024
#Caveats: None

# Here Importing necessary Modules to do automation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

# Data Class contains URL and Search value in it
class Data:

   URL = "https://demo.nopcommerce.com/"
   SEARCHSTOREVALUE ="Galaxy"


# Locators contains search locators
class Locators:

      search_store_locator = "small-searchterms"
      search_locator = "//button[@type='submit']"

# Hackathon class inherits the Data and Locators class!
class Hackathon(Data, Locators):


   def __init__(self): # Here im using the INIT constructor
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.driver.implicitly_wait(10) # Here im using the Implicit wait for this Automation


   def automation(self):
       try:  # Here im using the Exception handling to handle the errors
           self.driver.maximize_window()
           self.driver.get(self.URL)
           self.driver.find_element(by=By.ID, value=self.search_store_locator).send_keys(self.SEARCHSTOREVALUE)
           self.driver.find_element(by=By.XPATH, value=self.search_locator).click()
       except (NoSuchElementException, ElementNotVisibleException) as error:
           print(error)
       finally:
           self.driver.quit()




# main execution function


'''if __name__ == "__main__":


   hari = Hackathon()


   hari.automation()'''
