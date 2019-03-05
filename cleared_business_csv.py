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

    #radial buttons
    browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/div[4]/input[2]').click()

    populate()

    time.sleep(waittime)
    #check if table is populated
    try:
        browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr[2]/td[2]').is_displayed()
    except:
        print('not populated after csv upload')

    #radial buttons
    time.sleep(waittime)
    browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/div[4]/input[1]').click()
    time.sleep(waittime)
    browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/div[4]/input[2]').click()
    time.sleep(waittime)
    try:
        browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr[1]/td[2]').is_displayed()
    except:
        print('Step Passed: table is empty after tab change')

    populate()
    time.sleep(waittime)

    browser.find_element_by_link_text('Cancel').click()

    browser.find_element_by_link_text('Check Driver\'s Licence Status').click()
    time.sleep(waittime)

    #Enter License Page
    try:
        browser.find_element_by_link_text('Multiple Licences').click()
        time.sleep(waittime)
    except:
        print('Multiple Licence tab not loaded')

    #radial buttons
    browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/div[4]/input[2]').click()
    
    try:
        browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr[2]/td[2]').is_displayed()
    except:
        print('Step Passed: table is empty after pressing cancel')

def populate():

    #csv upload
    csv_location = os.getcwd() + '\\licences-tests.csv'
    #browser.find_element_by_id('excelInput').send_keys(csv_location)
    browser.find_element_by_xpath('//*[@id="excelInput"]').send_keys(csv_location)

    #error icon should be shown for invalid licences in csv
    try:
        'warning' in browser.page_source
    except:
        print("DL error icon not shown")
    time.sleep(waittime)

if __name__ == '__main__':
    main()


