
class SearchCustomer:
    # Locators
    txtEmail_id = "//input[@id='SearchEmail']"
    txtFirstName_id = "//input[@id='SearchFirstName']"
    txtLastname_id = "//input[@id='SearchLastName']"
    btnSearch_id = "//button[@id='search-customers']"
    tblSearchResults_xpath = "//table[@role='grid']"
        #"//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.txtLastname_id).clear()
        self.driver.find_element_by_id(self.txtLastname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_element_by_id(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_element_by_id(self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1 ,self.getNoOfRows()+1):
            table =self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r )+"]/td[2]").text()
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text()
            if name == Name:
                flag = True
                break
        return flag