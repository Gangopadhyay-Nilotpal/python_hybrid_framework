from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser in ('chrome','Chrome'):
        #weboptions = webdriver.ChromeOptions()
        #weboptions.add_argument("start-maximized")
        #browdriver = webdriver.Chrome(options=weboptions)
        browdriver = webdriver.Chrome()
        print("Launching Chrome browser...")
    elif browser in ('firefox','Firefox'):
        browdriver = webdriver.Firefox()
        print("\nLaunching Firefox browser...")
    else:
        browdriver = webdriver.Firefox()
        print("\nBy Default - Launching Firefox browser...")

    browdriver.maximize_window()
    return browdriver

def pytest_addoption(parser): # this will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # this will return the Browser value to setup method
    return request.config.getoption("--browser")
"""
########## PyTest HTML Report ##########

# Hooks for Adding Environment info to HTML Report
def pytest_configure(config):
    config.metadata['Project Name'] = 'nop Commerce'
    config.metadata['Module Name'] = 'Customers'
    config.metadata['Tester'] = 'Abcdef'

# Hooks for Delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
"""