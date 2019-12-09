import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):

        #Launch copart.com in chrome browser
        self.driver.get("https://www.copart.com")

        #Validating Page title
        self.assertIn("Copart", self.driver.title)

        #Display Makes/Models
        print("\n\nList of Makes/Models")
        print("=======================================================================")
        self.ParseWebElementDataByXPath("//*[@id=\"tabTrending\"]/div[1]/div[2]//*/a")

        #Display Categories
        print("\n\nList of Popular Categories")
        print("=======================================================================")
        self.ParseWebElementDataByXPath("//*[@id=\"tabTrending\"]/div[3]//*/a")

    def ParseWebElementDataByXPath(self, pXPath):

        # Retrieve WebElement using XPath
        lElementList    =   self.driver.find_elements(By.XPATH, pXPath)

        for lAnchor in lElementList :
            #Retrieve the href attribute value
            lAnchorUrl  =   lAnchor.get_attribute("href")
            print("%s %s" %(lAnchor.text, lAnchorUrl))

if __name__ == '__main__':
    unittest.main()
