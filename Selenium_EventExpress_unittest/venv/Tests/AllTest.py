import unittest
from selenium import webdriver
import time


import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir+'\Resources')
sys.path.insert(0, parentdir+'\Resources\PO')

from Resources.Locators import *
from Resources.TestData import TestData
from Resources.PO import Pages
from Pages import LoginPage, CreateEvent

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
        super( ).setUp()



    def test_login_if_user_entered(self):
        self.login_Page = LoginPage( self.driver )
        self.login_Page.click_on_login_button()
        self.login_Page.type_login()
        self.login_Page.type_pass()
        self.login_Page.press_button_signin()
        self.assertTrue(self.driver.find_element(*HomePageLocators.LOGO).is_displayed()), "element not found"
      



        # self.assertEqual()

    def test_click_to_add_event(self):
        self.login_Page = LoginPage( self.driver )
        self.add_event = CreateEvent( self.login_Page )
        self.login_Page.enter_to_site()
        self.add_event.open_profile_events()
        self.add_event.click_to_add_event( )







