class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.browser = driver


class MainPage(BasePage):

    def proceed(self):
        return self.browser.find_element_by_link_text('Check Driver\'s Licence Status')

class CommonPage(BasePage):

    def back(self):
        return self.browser.find_element_by_partial_link_text('Cancel')

    def cancel(self):
        return self.browser.find_element_by_partial_link_text('Cancel')

    def next(self):
        return self.browser.find_element_by_partial_link_text('Next')

    def ontario(self):
        return self.browser.find_element_by_xpath('/html/body/app-root/div/header/div/a/img')


class EnterDetails(BasePage):

    def one_licence(self):
        return self.browser.find_element_by_link_text('One Licence')

    def multiple_licences(self):
        return self.browser.find_element_by_link_text('Multiple Licences')

class EnterDL(BasePage):

    def single_input1(self):
        return self.browser.find_element_by_id('licenceInput10')

    def single_input2(self):
        return self.browser.find_element_by_id('licenceInput20')

    def single_input2(self):
        return self.browser.find_element_by_id('licenceInput30')

    def manual_radial(self):
        return self.browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/div[4]/input[1]')

    def csv_radial(self):
        return self.browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/div[4]/input[2]')

    def csv_upload(self):
        return self.browser.find_element_by_xpath('//*[@id="excelInput"]')

    def multiple_input1(self):
        return self.browser.find_element_by_id('licenceInput11')

    def multiple_input2(self):
        return self.browser.find_element_by_id('licenceInput21')

    def multiple_input3(self):
        return self.browser.find_element_by_id('licenceInput31')
    
    def add_licence(self):
        return self.browser.find_element_by_partial_link_text('Add Licence')

    def total(self):
        return self.driver.browser.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/div[1]/div[2]/h4')

    def table_row_column(self,row,column):
        return self.browser.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr['+str(row)+']/td['+str(column)+']')


class ConfirmOrder(BasePage):

    def email(self):
        return self.browser.find_element_by_id('emailAddress')

    def intended_use(self):
        return self.browser.find_element_by_id('intendedUse')

    def phone(self):
        return self.browser.find_element_by_id('phoneNumber')

    def name(self):
        return self.browser.find_element_by_id('name')

    def company(self):
        return self.browser.find_element_by_id('company')
    
    def country(self):
        return self.browser.find_element_by_id('country')

    def address(self):
        return self.browser.find_element_by_id('address')

    def city(self):
        return self.browser.find_element_by_id('city')

    def province(self):
        return self.browser.find_element_by_id('Province'))

    def postal_code(self):
        return self.browser.find_element_by_id('postalCode')

    def total(self):
        return self.driver.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/div[1]/div[2]/h4')

    def table(self):
        return self.driver.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr[1]/td[2]')

    def table_row_column(self,row,column):
        return self.driver.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr['+str(row)+']/td['+str(column)+']')

class Payment(BasePage):

    def amount(self):
        return self.driver.find_element_by_link_text('')

    def name_on_card(self):
        return self.driver.find_element_by_link_text('')

    def card_type(self):
        return self.driver.find_element_by_link_text('')

    def card_number(self):
        return self.driver.find_element_by_link_text('')

    def month(self):
        return self.driver.find_element_by_link_text('')
    
    def year(self):
        return self.driver.find_element_by_link_text('')

    def cvd(self):
        return self.driver.find_element_by_link_text('')

    def back(self):
        return self.driver.find_element_by_link_text('')

    def pay(self):
        return self.driver.find_element_by_link_text('')

    


