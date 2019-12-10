import unittest
from selenium import webdriver
import time
from Resources.Locators import *
from Resources.TestData import TestData
from Resources.PO import Pages
from Resources.PO.Pages import LoginPage, ViewEvent

class TestLoginToSite(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class Test_Login(TestLoginToSite):

    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()



    def test_login_if_user_entered(self):
        self.login_Page = LoginPage( self.driver )
        self.login_Page.click_on_login_button()
        self.login_Page.type_login(TestData.LOGIN_USER)
        self.login_Page.type_pass(TestData.PASSWORD_USER)
        self.login_Page.press_button_signin()
        self.assertTrue(self.driver.find_element(*HomePageLocators.LOGO).is_displayed()), "element not found"


    def test_click_to_add_event(self):
        self.login_Page = LoginPage( self.driver )
        self.add_event = ViewEvent( self.login_Page )
        self.login_Page.enter_to_site_e()
        self.add_event.open_profile_events()
        self.add_event.click_to_add_event( )
        self.assertTrue(self.driver.find_element(*AddEventPageLocators.PICTURE).is_displayed()), "element not found"







if __name__ == '__main__':
    unittest.main()
    






