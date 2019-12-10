import unittest
from selenium import webdriver
from Resources.Locators import *
from Resources.PO import Pages
from Resources.PO.Pages import  AddEvent
from Tests.AllTest import TestLoginToSite
from Resources.PO.Pages import LoginPage


class TestAddEvent(TestLoginToSite):

    def setUp(self):
       super( ).setUp( )
       self.login_Page = LoginPage( self.driver )



    def test_create_event(self):
        self.create_event = AddEvent(self.login_Page)
        self.login_Page.enter_to_site_e()
        self.login_Page.click_to_profile()
        self.login_Page.click_to_add_event()
        self.create_event.add_title()
        self.assertTrue(self.driver.find_element(*AddEventPageLocators.TITLE_EVENT).is_displayed()), "title doesn't enable"
        self.create_event.download()

if __name__ == "__main__":
    unittest.main()