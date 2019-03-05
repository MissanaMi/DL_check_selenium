from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Firefox()
#browser = webdriver.Chrome()
#browser = webdriver.Edge()
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

#do this better, probably with args, it could have been done in the time it took to write this comment
############################################
dl_number = 'A0124-68024-11111'
############################################

browser.get('http://etcbitdcapmdw44.cihs.ad.gov.on.ca/Pris_Carrier/dlc/')

#Home
browser.find_element_by_link_text('Check Driver\'s Licence Status').click()
time.sleep(waittime)

#Enter License Page
try:
    browser.find_element_by_link_text('One Licence').click()
    time.sleep(waittime)
except:
    print('clickable')

browser.find_element_by_id('licenceInput10').send_keys(dl_number[0:5])

browser.find_element_by_id('licenceInput20').send_keys(dl_number[6:11])

browser.find_element_by_id('licenceInput30').send_keys('aaaaa')

browser.find_element_by_partial_link_text('Next').click()
time.sleep(waittime)

#error icon should be shown for invalid format
try:
    'warning' in browser.page_source
except:
    print("DL error icon not shown")


browser.find_element_by_id('licenceInput30').clear()

browser.find_element_by_id('licenceInput30').send_keys(dl_number[12:17])

#check icon should be shown after invalid input is corrected
try:
    'check_circle' in browser.page_source
except:
    print("DL check icon not shown")

browser.find_element_by_partial_link_text('Next').click()
time.sleep(waittime)

#Customer Information
browser.find_element_by_id('emailAddress').send_keys("JohnSmith@gmail.com")

browser.find_element_by_id('phoneNumber').send_keys("905-678-9012")

browser.find_element_by_id('name').send_keys("John Smith")

browser.find_element_by_id('company').send_keys("N/A")

browser.find_element_by_id('address').send_keys("123 Baker street")

browser.find_element_by_id('city').send_keys("Toronto")

browser.find_element_by_id('postalCode').send_keys("H6L5W3")

select = Select(browser.find_element_by_id('intendedUse'))
select.select_by_visible_text('Personal Use')

select = Select(browser.find_element_by_id('country'))
select.select_by_visible_text('Canada')

#select = Select(browser.find_element_by_id('Province'))
#select.select_by_visible_text('Ontario')

#assert items are still in cart
time.sleep(waittime)
string = '/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr/td[2]'

assert dl_number in browser.find_element_by_xpath(string).text.replace(" ", "")

#assert correct number of DLs in cart and price
assert browser.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/div[1]/div[2]/h4').text == 'Total Licence(s): 1 | Amount ($): 2.00'

browser.refresh()
time.sleep(waittime)

#recheck items are still in the cart after refresh
string = '/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr/td[2]'

assert dl_number in browser.find_element_by_xpath(string).text.replace(" ", "")

#assert correct number of DLs in cart and price
assert browser.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/div[1]/div[2]/h4').text == 'Total Licence(s): 1 | Amount ($): 2.00'

print('Basic Usage Test Passed')

#browser.find_element_by_partial_link_text('Next').click()

'''
#payment page !not implemented
browser.find_element_by_partial_link_text('I Paid!').click()

#results
time.sleep(waittime)
#print(browser.find_element_by_xpath('/html/body/app-root/div/app-report/div/table/tbody/tr/td[3]/span').text)
assert browser.find_element_by_xpath('/html/body/app-root/div/app-report/div/table/tbody/tr/td[3]/span').text == dl_key.get(dl_number)

#
#asserts for all payment information when implemented 
#

#
#submit feedback
#
'''

#browser.close()