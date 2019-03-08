from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

waittime = 1

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.browser = driver


class MainPage(BasePage):

    def proceed(self):
        element = self.browser.find_element_by_link_text('Check Driver\'s Licence Status')
        element.click()

class CommonPage(BasePage):

    def back(self):
        element =  self.browser.find_element_by_partial_link_text('Back')
        element.click()

    def cancel(self):
        element = self.browser.find_element_by_partial_link_text('Cancel')
        element.click()

    def next(self):
        element = self.browser.find_element_by_partial_link_text('Next')
        element.click()

    def ontario(self):
        element = self.browser.find_element_by_xpath('/html/body/app-root/div/header/div/a/img')
        element.click()
    
    def refresh(self):
        self.browser.refresh()

    def get_page(self):
        self.browser.get('https://stage.dlc.rus.mto.gov.on.ca/dlc/')

class EnterDL(BasePage):

    def one_licence(self):
        element = self.browser.find_element_by_link_text('One Licence')
        element.click()

    def multiple_licences(self):
        element = self.browser.find_element_by_link_text('Multiple Licences')
        element.click()

    def single_input1(self,number):
        element = self.browser.find_element_by_id('licenceInput10')
        element.send_keys(number)

    def single_input2(self,number):
        element = self.browser.find_element_by_id('licenceInput20')
        element.send_keys(number)

    def single_input3(self,number):
        element = self.browser.find_element_by_id('licenceInput30')
        element.send_keys(number)

    def single_input3_clear(self):
        element = self.browser.find_element_by_id('licenceInput30')
        element.clear()

    def manual_radial(self):
        element = self.browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/div[4]/input[1]')
        element.click()

    def csv_radial(self):
        element = self.browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/div[4]/input[2]')
        element.click()

    def csv_upload(self,location):
        element =  self.browser.find_element_by_xpath('//*[@id="excelInput"]')
        element.send_keys(location)

    def multiple_input1(self,number):
        element = self.browser.find_element_by_id('licenceInput11')
        element.send_keys(number)

    def multiple_input2(self,number):
        element = self.browser.find_element_by_id('licenceInput21')
        element.send_keys(number)

    def multiple_input3(self,number):
        element = self.browser.find_element_by_id('licenceInput31')
        element.send_keys(number)
    
    def multiple_input3_clear(self):
        element = self.browser.find_element_by_id('licenceInput31')
        element.clear()
    
    def add_licence(self):
        element = self.browser.find_element_by_partial_link_text('Add Licence')
        element.click()

    def total(self):
        return self.browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/app-order-table/div[1]/div[2]/h4').text

    def table_row_column(self,row,column):
        return self.browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr['+str(row)+']/td['+str(column)+']').text.replace(" ", "")

    def load_more(self):
        element = self.browser.find_element_by_link_text('Load More')
        element.click()
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


class ConfirmOrder(BasePage):

    def email(self,value):
        element = self.browser.find_element_by_id('emailAddress')
        element.send_keys(value)

    def intended_use(self,value):
        select = Select(self.browser.find_element_by_id('intendedUse'))
        select.select_by_visible_text(value)

    def phone(self,value):
        element = self.browser.find_element_by_id('phoneNumber')
        element.send_keys(value)

    def name(self,value):
        element = self.browser.find_element_by_id('name')
        element.send_keys(value)

    def company(self,value):
        element = self.browser.find_element_by_id('company')
        element.send_keys(value)
    
    def country(self,value):
        select = Select(self.browser.find_element_by_id('country'))
        select.select_by_visible_text(value)

    def address(self,value):
        element = self.browser.find_element_by_id('address')
        element.send_keys(value)

    def city(self,value):
        element = self.browser.find_element_by_id('city')
        element.send_keys(value)

    def province(self,value):
        select = Select(self.browser.find_element_by_id('Province'))
        select.select_by_visible_text(value)

    def postal_code(self,value):
        element = self.browser.find_element_by_id('postalCode')
        element.send_keys(value)

    def total(self):
        return self.browser.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/div[1]/div[2]/h4').text

    def table(self):
        return self.browser.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr/td[2]').text.replace(" ", "")

    def table_row_column(self,row,column):
        return self.browser.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr['+str(row)+']/td['+str(column)+']').text.replace(" ", "")

    def load_more(self):
        element = self.browser.find_element_by_link_text('Load More')
        element.click()
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

class Payment(BasePage):

    def amount(self,value):
        element = self.browser.find_element_by_link_text('')
        element.send_keys(value)

    def name_on_card(self,value):
        element = self.browser.find_element_by_link_text('')
        element.send_keys(value)

    def card_type(self,value):
        element = self.browser.find_element_by_link_text('')
        element.send_keys(value)

    def card_number(self,value):
        element = self.browser.find_element_by_link_text('')
        element.send_keys(value)

    def month(self,value):
        element = self.browser.find_element_by_link_text('')
        element.send_keys(value)
    
    def year(self,value):
        element = self.browser.find_element_by_link_text('')
        element.send_keys(value)

    def cvd(self,value):
        element = self.browser.find_element_by_link_text('')
        element.send_keys(value)

    def back(self,value):
        element = self.browser.find_element_by_link_text('')
        element.send_keys(value)

    def pay(self,value):
        element = self.browser.find_element_by_link_text('')
        element.send_keys(value)

    


