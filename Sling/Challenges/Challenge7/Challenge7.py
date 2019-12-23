import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):

        #Launch copart.com in chrome browser
        self.driver.get("https://www.copart.com")

        #Validating Page title
        self.assertIn("Copart", self.driver.title)

        makeModelArray = {}
        makeModelDivElementList =   self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]/div[2]/div//a")

        for eachDivMakeModel in makeModelDivElementList:
            makeModelArray[eachDivMakeModel.text]  = eachDivMakeModel.get_attribute("href")

        print (str(makeModelArray))
if __name__ == '__main__':
    unittest.main()
