from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

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

#this can be moved to a csv for testing
dl_numbers = ['A0124-68024-11111','A0224-68024-11111','A0324-68024-11111','A0424-68024-11111','A0524-68024-11111']

def main():
    browser.get('http://etcbitdcapmdw44.cihs.ad.gov.on.ca/Pris_Carrier/dlc/')
    
    #Home
    browser.find_element_by_link_text('Check Driver\'s Licence Status').click()
    time.sleep(waittime)

    #Enter License Page
    try:
        browser.find_element_by_link_text('Multiple Licences').click()
        time.sleep(waittime)
    except:
        print('Multiple Licence tab not loaded')

    populate()

    count = 0
    for dl in dl_numbers:
        string = '/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr['+str(count+1)+']/td[2]'
        assert dl in browser.find_element_by_xpath(string).text.replace(" ", "")
        count=count+1

    #radial buttons
    browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/div[4]/input[2]').click()
    time.sleep(waittime)
    browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/div[4]/input[1]').click()

    try:
        browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr[1]/td[2]').is_displayed()
    except:
        print('Step Passed: table is empty after tab change')

    populate()

    browser.find_element_by_link_text('Cancel').click()

    browser.find_element_by_link_text('Check Driver\'s Licence Status').click()
    time.sleep(waittime)

    #Enter License Page
    try:
        browser.find_element_by_link_text('Multiple Licences').click()
        time.sleep(waittime)
    except:
        print('Multiple Licence tab not loaded')
    
    try:
        browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr[1]/td[2]').is_displayed()
    except:
        print('Step Passed: table is empty after pressing cancel')

def populate():

    for dl in dl_numbers:
        browser.find_element_by_id('licenceInput11').send_keys(dl[0:5])
        browser.find_element_by_id('licenceInput21').send_keys(dl[6:11])
        browser.find_element_by_id('licenceInput31').send_keys(dl[12:17])
        browser.find_element_by_partial_link_text('Add Licence').click()

if __name__ == '__main__':
    main()


