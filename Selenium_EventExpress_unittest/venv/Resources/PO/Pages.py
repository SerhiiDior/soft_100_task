import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir)

from Resources.Locators import *
from Resources.TestData import TestData


class BasePage():

    def __init__(self,driver):
        self.driver = driver

    def find_element(self, *locators):
        wait = WebDriverWait( self.driver, 10 )
        element = wait.until(lambda driver: self.driver.find_element(*locators))
        return element


    def click_to_element(self,*locators):
        element = self.find_element(*locators)
        element.click()

    def send_keys_to(self, *locators):
        element = self.find_element(*locators)
        element.send_keys[data]




class LoginPage(BasePage):

    def __init__(self, driver):
        super( ).__init__( driver )
        self.driver.get(TestData.BASE_URL )
        
        self.locator_main = MainPageLocators
        self.locator_form = LoginPageLocators

        
    
  
    
    def click_on_login_button(self):
        self.click_to_element( *self.locator_main.SIGNIN )

    def type_login(self):
        self.find_element( *self.locator_form.EMAIL ).send_keys('user@gmail.com' )

    def type_pass(self):
        self.find_element( *self.locator_form.PASSWORD ).send_keys('1qaz1qaz')

    def press_button_signin(self):
        self.click_to_element( *self.locator_form.BUTTON_SIGIN )

  
        
    def enter_to_site(self):
        self.click_to_element( *self.locator_main.SIGNIN )
        self.find_element( *self.locator_form.EMAIL ).send_keys( 'user@gmail.com' )
        self.find_element( *self.locator_form.PASSWORD ).send_keys( '1qaz1qaz' )
        self.click_to_element( *self.locator_form.BUTTON_SIGIN )
        
        
        
class CreateEvent(BasePage):

    def __init__(self, driver):
        super( ).__init__( driver )
        self.locator_profile = ProfilePageLocators
        self.locator_home = HomePageLocators

    def open_profile_events(self):
        self.click_to_element( *self.locator_home.PROFILE )
        
    def click_to_add_event(self,*locators):
        self.click_to_element(*self.locator_profile.ADD_EVENT)

    























# from Base_page import Base
# from locators import *
# from login_data import *
# from selenium.webdriver.common.keys import Keys
#
# class LoginPage(Base):
#     def __init__(self,driver):
#         self.locator_main = MainPageLocators
#         self.locator_form = LoginPageLocators
#         super().__init__(driver)
#
#     def click_on_login_button(self):
#         self.click_to_element( *self.locator_main.SIGNIN )
#
#     def type_login(self):
#         self.find_element( *self.locator_form.EMAIL ).send_keys( user_test['email'] )
#
#     def type_pass(self):
#         self.find_element( *self.locator_form.PASSWORD ).send_keys( user_test['password'] )
#
#     def press_button_signin(self):
#         self.click_to_element( *self.locator_form.BUTTON_SIGIN )