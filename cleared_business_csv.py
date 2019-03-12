from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import page_object

browser = webdriver.Firefox()
#browser = webdriver.Chrome(os.getcwd() +'\chromedriver.exe')
#browser = webdriver.Edge(os.getcwd() +'\MicrosoftWebDriver.exe')
#browser = webdriver.Ie(r"C:\\Users\\MissanMi\\project\\DL_check_selenium\\IEDriverServer.exe")

#value key for correct returns for certain DL numbers
#maybe move this to the csv column two just for testing? #### | valid/invalid/etc
dl_key =	{
  "A0124-68024-11111": "Valid",
  "A0224-68024-11111": "Not Valid",
  "A0324-68024-11111": "Not Found",
  "A0424-68024-11111": "Valid With Ignition Interlock",
  "A0524-68024-11111": "Valid With W Code",
}

main_page = page_object.MainPage(browser)
common_page = page_object.CommonPage(browser)
enter_licence_page = page_object.EnterDL(browser)
confirm_page = page_object.ConfirmOrder(browser)
payment_page = page_object.Payment(browser)

waittime = 1.5

#this can be moved to a csv for testing
dl_numbers = ['A0124-68024-11111','A0224-68024-11111','A0324-68024-11111','A0424-68024-11111','A0524-68024-11111']

def main():
    common_page.get_page()

    #Home
    time.sleep(waittime)
    main_page.proceed()
    time.sleep(waittime)

    #Enter License Page
    try:
        enter_licence_page.multiple_licences()
        time.sleep(waittime)
    except:
        print('Already selected')

    #radial buttons
    enter_licence_page.csv_radial

    populate()

    time.sleep(waittime)
    #check if table is populated
    try:
        #browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr[2]/td[2]').is_displayed()
        enter_licence_page.table_row_column(2,2).is_displayed()
    except:
        print('not populated after csv upload')

    #radial buttons
    
    #browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/div[4]/input[1]').click()
    enter_licence_page.manual_radial()
    
    #browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/div[4]/input[2]').click()
    enter_licence_page.csv_radial()
    time.sleep(waittime)
    
    try:
        browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr[1]/td[2]').is_displayed()
        enter_licence_page.table_row_column(2,2).is_displayed()
    except:
        print('Step Passed: table is empty after tab change')

    populate()
    time.sleep(waittime)

    common_page.cancel()
    time.sleep(waittime)

    main_page.proceed()
    time.sleep(waittime)

    #Enter License Page
    try:
        enter_licence_page.multiple_licences()
        time.sleep(waittime)
    except:
        print('Already selected')

    #radial buttons
    enter_licence_page.csv_radial()
    
    try:
        #browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr[2]/td[2]').is_displayed()
        enter_licence_page.table_row_column(2,2).is_displayed()
    except:
        print('Step Passed: table is empty after pressing cancel')

def populate():

    #csv upload
    csv_location = os.getcwd() + '\\licences-tests.csv'

    enter_licence_page.csv_upload(csv_location)

    #error icon should be shown for invalid licences in csv
    try:
        'warning' in browser.page_source
    except:
        print("DL error icon not shown")

if __name__ == '__main__':
    main()


