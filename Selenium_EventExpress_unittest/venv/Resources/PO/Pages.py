# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

    def send_keys_to(self,data,*locators):
        element = self.find_element(*locators)
        element.send_keys(data)

    def upload_file(self,path, *locators):
        element = self.find_element( *locators )
        element.send_keys(path)

        
    def enter_to_site(self,login,password):
        self.click_to_element( *self.locator_main.SIGNIN )
        self.send_keys_to(login, *self.locator_form.EMAIL )
        self.send_keys_to(password, *self.locator_form.PASSWORD )
        self.click_to_element( *self.locator_form.BUTTON_SIGIN )






class LoginPage(BasePage):

    def __init__(self, driver):
        super( ).__init__( driver )
        self.driver.get(TestData.BASE_URL )
        
        self.locator_main = MainPageLocators
        self.locator_form = LoginPageLocators
        self.locator_home = HomePageLocators
        self.locator_profile = ProfilePageLocators

        
    
  
    
    def click_on_login_button(self):
        self.click_to_element( *self.locator_main.SIGNIN )

    def type_login(self, *login):
        self.send_keys_to(*login,*self.locator_form.EMAIL )

    def type_pass(self, *password):
        self.send_keys_to(*password, *self.locator_form.PASSWORD)

    def press_button_signin(self):
        self.click_to_element( *self.locator_form.BUTTON_SIGIN )
        
    def enter_to_site_e(self):
        self.enter_to_site(TestData.LOGIN_USER, TestData.PASSWORD_USER)

    def click_to_profile(self):
        self.click_to_element(*self.locator_home.PROFILE)
    
    def click_to_add_event(self,*locators):
        self.click_to_element(*self.locator_profile.ADD_EVENT)

    
        
    
        
        
        
class ViewEvent(BasePage):

    def __init__(self, driver):
        super( ).__init__( driver )
        self.locator_profile = ProfilePageLocators
        self.locator_home = HomePageLocators

    def open_profile_events(self):
        self.click_to_element( *self.locator_home.PROFILE )

    def click_to_add_event(self,*locators):
        self.click_to_element(*self.locator_profile.ADD_EVENT)
        


class AddEvent(BasePage):
    
    def __init__(self, driver):
        super( ).__init__( driver )
        
        self.locator_add_event = AddEventPageLocators
        self.title = TestData.TITLE
        self.image = TestData.IMAGE
        
    def add_title(self):
        self.send_keys_to(self.title,*self.locator_add_event.TITLE_EVENT,)

    def download(self):
        self.upload_file(self.image, *self.locator_add_event.UPLOAD_PICTURE)
        
    
        
    
        
    
    

    























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