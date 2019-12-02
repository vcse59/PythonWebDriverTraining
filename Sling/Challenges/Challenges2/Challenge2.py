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

        #Finding search field by ID
        lSearchField = self.driver.find_element(By.ID, "input-search")

        #Enter text exotics in seach text box
        lSearchField.send_keys("exotics")

        #Finding search button by XPATH
        lSearchButton = self.driver.find_element_by_xpath("//*[@id=\"search-form\"]/div/div[2]/button")

        #Click on search button
        lSearchButton.click()

        #Wait 10 seconds implicitly until atleast one row is rendered
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//*[@id=\"serverSideDataTable\"]"
                                            "/tbody/tr[1]/td[3]/div/button[1]")))

        #Retrieving HTML source code
        lCompleteHtmlText = self.driver.page_source

        #Asserting the Porsche text in complete HTML source
        lTextToAssert = "Porsche"
        lbIsTextPresent = lTextToAssert in lCompleteHtmlText
        self.assertTrue(lbIsTextPresent, "%s string is not present in page source" %lTextToAssert)

if __name__ == '__main__':
    unittest.main()
