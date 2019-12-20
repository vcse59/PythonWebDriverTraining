import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge5(unittest.TestCase):

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
        lSearchField.send_keys("porsche")

        #Finding search button by XPATH
        lSearchButton = self.driver.find_element(By.XPATH, "//*[@id=\"search-form\"]/div/div[2]/button")

        #Click on search button
        lSearchButton.click()

        #Wait 30 seconds implicitly until atleast one row is rendered
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//*[@id=\"serverSideDataTable\"]/tbody/tr[1]")))

        #Retrieve Show entry drop down web element
        showEntriesElement = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable_length\"]/label/select")

        dropDownText = 100

        #Change show entry drop down to 100
        showEntriesElement.send_keys(dropDownText)

        #Wait 30 seconds implicitly until Showing 1 to dropDownText is present in show entry label
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element((By.XPATH,
                                            "//*[@id=\"serverSideDataTable_info\"]"),
                                            'Showing 1 to %s' %dropDownText))

        #Retrieve lot search model web element
        dynamicTableWebElement = self.driver.find_elements(By.XPATH, "//*[@id=\"serverSideDataTable\"]/tbody/tr/td[6]/span")

        lotSearchModel  =   []
        #Iterate WebElement list to fetch text
        for eachDynamicTableEntry in dynamicTableWebElement:
            if eachDynamicTableEntry.text not in lotSearchModel:
                lotSearchModel.append(eachDynamicTableEntry.text)

        print("Possible values of lot search models are : %s" %str(lotSearchModel))

        damageTypeDictionary =   {"REAR END" : 0,
                                 "FRONT END" : 0,
                                 "MINOR DENT/SCRATCHES" : 0,
                                 "UNDERCARRIAGE" : 0,
                                 "MISC" : 0
                                 }
        #Retrieving lot model damage web element
        dynamicTableWebElement = self.driver.find_elements(By.XPATH, "//*[@id=\"serverSideDataTable\"]/tbody/tr/td[12]/span")

        #Iterate WebElement list to count damage category listed in damageTypeDictionary
        for eachDynamicTableEntry in dynamicTableWebElement:
            if eachDynamicTableEntry.text in damageTypeDictionary.keys():
                damageTypeDictionary[eachDynamicTableEntry.text] = damageTypeDictionary[eachDynamicTableEntry.text] + 1
            else:
                damageTypeDictionary["MISC"] = damageTypeDictionary["MISC"] + 1

        print("Counting of models with damage category : %s" %str(damageTypeDictionary))

if __name__ == '__main__':
    unittest.main()
