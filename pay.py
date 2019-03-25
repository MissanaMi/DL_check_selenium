from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

waittime = 1
name = 'John Smith'
card = '4030000010001234'
cardtype = 'VISA'
month = '01'
year = '2019'
CVD = '123'

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.browser = driver

class PaymentPage(BasePage):
    def enter_details(self,num_of_dls):
        #correct price
        assert self.browser.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/form/table[2]/tbody/tr[7]/td[2]/font').text == '$'+str(num_of_dls*2)+'.00 CAD'

        #name
        self.browser.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/form/table[2]/tbody/tr[8]/td[2]/input').send_keys(name)
        
        #type
        select = Select(self.browser.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/form/table[2]/tbody/tr[9]/td[2]/select'))
        select.select_by_visible_text(cardtype)

        #card
        self.browser.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/form/table[2]/tbody/tr[10]/td[2]/input').send_keys(card)

        #month
        select = Select(self.browser.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/form/table[2]/tbody/tr[11]/td[2]/select[1]'))
        select.select_by_visible_text(month)

        #year
        select = Select(self.browser.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/form/table[2]/tbody/tr[11]/td[2]/select[2]'))
        select.select_by_visible_text(year)

        #CVD
        self.browser.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/form/table[2]/tbody/tr[12]/td[2]/input').send_keys(CVD)

        #click next
        self.browser.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/form/table[2]/tbody/tr[13]/td/table/tbody/tr/td[3]/input').click()

    def payment_results(self):
        #check details is correctly displayed on results page
        assert self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/div[8]/div/div/div[1]/div/div[14]').text == name

        assert self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/div[8]/div/div/div[1]/div/div[16]').text == cardtype
            
        cardnumber =self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/div[8]/div/div/div[1]/div/div[18]').text
        assert cardnumber[12:16] == card[12:16]




