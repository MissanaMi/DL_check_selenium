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

waittime = 1.5

main_page = page_object.MainPage(browser)
common_page = page_object.CommonPage(browser)
enter_licence_page = page_object.EnterDL(browser)
confirm_page = page_object.ConfirmOrder(browser)
payment_page = page_object.Payment(browser)

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

    populate()

    count = 0
    for dl in dl_numbers:
        string = '/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr['+str(count+1)+']/td[2]'
        assert dl in browser.find_element_by_xpath(string).text.replace(" ", "")
        count=count+1

    #radial buttons
    enter_licence_page.csv_radial()
    time.sleep(waittime)
    enter_licence_page.manual_radial()

    try:
        enter_licence_page.table_row_column(1,2).is_displayed()
    except:
        print('Step Passed: table is empty after tab change')

    populate()

    common_page.cancel()

    main_page.proceed()
    time.sleep(waittime)

    #Enter License Page
    try:
        enter_licence_page.multiple_licences()
        time.sleep(waittime)
    except:
        print('Multiple Licence tab not loaded')
    
    try:
        enter_licence_page.table_row_column(1,2).is_displayed()
    except:
        print('Step Passed: table is empty after pressing cancel')

def populate():

    for dl in dl_numbers:
        enter_licence_page.multiple_input1(dl[0:5])
        enter_licence_page.multiple_input2(dl[6:11])
        enter_licence_page.multiple_input3(dl[12:17])
        enter_licence_page.add_licence()

if __name__ == '__main__':
    main()


