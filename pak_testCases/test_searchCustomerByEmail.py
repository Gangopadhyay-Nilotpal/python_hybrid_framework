import pytest
from time import sleep

from pak_pageObjects.LoginPage import LoginPage
from pak_pageObjects.AddCustomerPage import AddCustomer
from pak_pageObjects.SearchCustomerPage import SearchCustomer
from pak_utilities.readProperties import ReadConfig
from pak_utilities.customLogger import LogGen

class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********** Test_004_SearchCustomerByEmail **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("**********  Starting Search Customer By Email **********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        sleep(3)

        self.logger.info("**********  Starting Customer By Email **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        sleep(5)
        status  = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("********** Test_004_SearchCustomerByEmail Finished **********")
        self.driver.close()
