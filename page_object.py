from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

waittime = 1

BaseURL = 'http://etcbitdcapmdw30.cihs.ad.gov.on.ca/Pris_Carrier/dlc/'

dl_key =	{
    'L0127-15675-70417': 'Not Found',
    'K0733-19005-65811': 'Not Valid',
    'M2135-18407-40922': 'Not Valid',
    'M8231-35818-00102': 'Not Found',
    'A1742-60506-10101': 'Valid (Ignition Interlock Required)',
    'A5359-30506-71010': 'Valid',
    'L0001-75688-30707': 'Not Valid',
    'K0733-12887-35522': 'Not Found',
    'T7565-75205-80513': 'Not Valid',
    'A1013-78506-55101': 'Not Found'
}

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
        self.browser.get(BaseURL)
    
    def get_baseurl(self):
        return BaseURL

class EnterDL(BasePage):

    def one_licence(self):
        element = self.browser.find_element_by_link_text('One Licence')
        element.click()

    def multiple_licences(self):
        element = self.browser.find_element_by_link_text('Check Multiple Driver\'s Licences')
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
        element = self.browser.find_element_by_link_text('Enter Manually')
        element.click()

    def csv_radial(self):
        element = self.browser.find_element_by_link_text('Upload a CSV File')
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
        return self.browser.find_element_by_xpath('/html/body/app-root/app-enter-details/div/app-order-table/div[1]/div[2]/h4').text

    def table_row_column(self,row,column):
        return self.browser.find_element_by_xpath('/html/body/app-root/app-enter-details/div/app-order-table/table/tbody/tr['+str(row)+']/td['+str(column)+']').text.replace(" ", "")

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
        element = self.browser.find_element_by_link_text(value)
        element.click()

    def address(self,value):
        element = self.browser.find_element_by_id('address')
        element.send_keys(value)

    def city(self,value):
        element = self.browser.find_element_by_id('city')
        element.send_keys(value)

    def province_canada(self,value):
        select = Select(self.browser.find_element_by_id('provinceId'))
        select.select_by_visible_text(value)

    def state_usa(self,value):
        element = 1+1
        #implement me

    def province_other(self,value):
        element = 1+1
        #implement me

    def postal_code(self,value):
        element = self.browser.find_element_by_id('postalCode')
        element.send_keys(value)

    def total(self):
        return self.browser.find_element_by_xpath('/html/body/app-root/app-confirm-order/div/app-order-table/div[1]/div[2]/h4').text

    def table(self):
        return self.browser.find_element_by_xpath('/html/body/app-root/app-confirm-order/div/app-order-table/table/tbody/tr/td[2]').text.replace(" ", "")

    def table_row_column(self,row,column):
        return self.browser.find_element_by_xpath('/html/body/app-root/app-confirm-order/div/app-order-table/table/tbody/tr['+str(row)+']/td['+str(column)+']').text.replace(" ", "")

    def load_more(self):
        element = self.browser.find_element_by_link_text('Load More')
        element.click()
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

class Results_single(BasePage):
    def status(self,value):
        assert self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/div[4]/div[1]/div/h4[1]').text == value
    
    def description(self,value):
        assert self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/div[4]/div[3]/div/p').text == value
    
    def dl_number(self,value):
        assert self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/div[4]/div[1]/div/h4[2]').text == value
    
    def purchaser_name(self,value):
        assert self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/div[5]/div/div/div[1]/div/div[12]').text == value
    
    def result_price(self,value):
        assert self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/div[5]/div/div/div[2]/div/div[2]').text == value
    
class Results_multiple(BasePage):
    def status(self):
        values = []

        for i in range(1,6):
            string = '/html/body/app-root/app-report/div/div[4]/div['+str(i)+']/div/div[3]/p'
            values.append(self.browser.find_element_by_xpath(string).text)
        return values

    #will need to supply an array of status's(or 2d with dl_numbers) to check coresponding dl returned right result
    def dl_number(self,dl_numbers):
        count = 1
        for dl in dl_numbers:
            assert dl in self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/table/tbody/tr['+str(count)+']/td[2]').text
            count=count+1

    def dl_number_and_status(self,dl_numbers):
        count = 1
        for dl in dl_numbers:
            assert dl in self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/table/tbody/tr['+str(count)+']/td[2]').text

            print(dl,':',dl_key[dl],'==',self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/table/tbody/tr['+str(count)+']/td[3]').text)
            assert dl_key[dl] in self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/table/tbody/tr['+str(count)+']/td[3]').text
            count=count+1

        

    def purchaser_name(self,value):
        assert self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/div[5]/div/div/div[1]/div/div[12]').text == value
    
    def result_price(self,value):
        assert self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/div[5]/div/div/div[2]/div/div[2]').text == value

    def expand(self):
        self.browser.find_element_by_xpath('/html/body/app-root/app-report/div/div[5]/a/div/div[2]/span/span').click()