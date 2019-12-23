import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):

        #Launch copart.com in chrome browser
        self.driver.get("https://www.copart.com")

        #Validating Page title
        self.assertIn("Copart", self.driver.title)

        #Finding search field by ID
        lSearchField = self.driver.find_element(By.ID, "input-search")

        #Enter text exotics in seach text box
        lSearchField.send_keys("nissan")

        #Finding search button by XPATH
        lSearchButton = self.driver.find_element(By.XPATH, "//*[@id=\"search-form\"]/div/div[2]/button")

        #Click on search button
        lSearchButton.click()

        #Wait 30 seconds implicitly until atleast one row is rendered
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//*[@id=\"serverSideDataTable\"]/tbody/tr[1]")))

        #Retrieve lot search model web element
        dynamicTableWebElement = self.driver.find_elements(By.XPATH, "//*[@id=\"serverSideDataTable\"]/tbody/tr/td[6]/span")

        lotSearchModel  =   []
        try:
            #Iterate WebElement list to fetch text
            isModelPresent = False
            for eachDynamicTableEntry in dynamicTableWebElement:
                if 'skyline' in eachDynamicTableEntry.text:
                    isModelPresent = True
            if isModelPresent is False:
                self.driver.save_screenshot("Exception_Image.png")
                raise Exception("skyline model is not available for nissan")
        except Exception as exp:
            print (exp.args[0])

if __name__ == '__main__':
    unittest.main()
