
import pytest
from selenium import webdriver
from pak_pageObjects.LoginPage import LoginPage
from pak_utilities.readProperties import ReadConfig
from pak_utilities.customLogger import LogGen

class Test_001_Login:

    # class variables
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    pagetitle_beforelogin = ReadConfig.getpageTitleBefLogin()
    pagetitle_afterlogin = ReadConfig.getpageTitleAftLogin()
    # all are moved to "config.ini" file, & called via "readProperties.py", no hard coding here

    loggerobjvar = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.loggerobjvar.info("********** Test_001_Login **********")
        self.loggerobjvar.info("********** Verifying Home page Title Test - Started **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == self.pagetitle_beforelogin:
            self.loggerobjvar.info("********** Verifying Home page Title Test - Passed **********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\dir_Screenshots\\"+"test_homePageTitle.png")
            self.loggerobjvar.error("********** Verifying Home page Title Test - Failed **********")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.loggerobjvar.info("********** Verifying Login Test - Started **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.lp.clickLogout()
        if act_title == self.pagetitle_afterlogin:
            self.loggerobjvar.info("********** Verifying Login Test - Passed **********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\dir_Screenshots\\" + "test_login.png")
            self.loggerobjvar.error("********** Verifying Login Test - Failed **********")
            self.driver.close()
            assert False
