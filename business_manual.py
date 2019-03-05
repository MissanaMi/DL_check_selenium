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

dl_numbers = ['A0124-68024-11111','A0224-68024-11111','A0324-68024-11111','A0424-68024-11111','A0524-68024-11111']
############################################

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

browser.find_element_by_id('licenceInput11').send_keys(dl_numbers[0][0:5])

browser.find_element_by_id('licenceInput21').send_keys(dl_numbers[0][6:11])

browser.find_element_by_id('licenceInput31').send_keys('aaaaa')

browser.find_element_by_partial_link_text('Add Licence').click()
time.sleep(waittime)

#error icon should be shown for invalid format
try:
    'warning' in browser.page_source
except:
    print("DL error icon not shown")


browser.find_element_by_id('licenceInput31').clear()

browser.find_element_by_id('licenceInput31').send_keys(dl_numbers[0][12:17])

#check icon should be shown after invalid input is corrected
try:
    'check_circle' in browser.page_source
except:
    print("DL check icon not shown")

browser.find_element_by_partial_link_text('Add Licence').click()

#native alerts are a pain to deal with
'''
browser.find_element_by_id('licenceInput11').send_keys(dl_numbers[0][0:5])
browser.find_element_by_id('licenceInput21').send_keys(dl_numbers[0][6:11])
browser.find_element_by_id('licenceInput31').send_keys(dl_numbers[0][12:17])

try:
    browser.find_element_by_partial_link_text('Add Licence').click()
except UnexpectedAlertPresentException: 
    try:
        alert = driver.switchTo().alert().accept()
    except:
        print('error with the error')
'''
#move this entry to a for look once the alert for duplicate is implemented
browser.find_element_by_id('licenceInput11').send_keys(dl_numbers[1][0:5])
browser.find_element_by_id('licenceInput21').send_keys(dl_numbers[1][6:11])
browser.find_element_by_id('licenceInput31').send_keys(dl_numbers[1][12:17])
browser.find_element_by_partial_link_text('Add Licence').click()

browser.find_element_by_id('licenceInput11').send_keys(dl_numbers[2][0:5])
browser.find_element_by_id('licenceInput21').send_keys(dl_numbers[2][6:11])
browser.find_element_by_id('licenceInput31').send_keys(dl_numbers[2][12:17])
browser.find_element_by_partial_link_text('Add Licence').click()

browser.find_element_by_id('licenceInput11').send_keys(dl_numbers[3][0:5])
browser.find_element_by_id('licenceInput21').send_keys(dl_numbers[3][6:11])
browser.find_element_by_id('licenceInput31').send_keys(dl_numbers[3][12:17])
browser.find_element_by_partial_link_text('Add Licence').click()

browser.find_element_by_id('licenceInput11').send_keys(dl_numbers[4][0:5])
browser.find_element_by_id('licenceInput21').send_keys(dl_numbers[4][6:11])
browser.find_element_by_id('licenceInput31').send_keys(dl_numbers[4][12:17])
browser.find_element_by_partial_link_text('Add Licence').click()

count = 0
for dl in dl_numbers:
    string = '/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr['+str(count+1)+']/td[2]'
    assert dl in browser.find_element_by_xpath(string).text.replace(" ", "")
    count=count+1

browser.refresh()

try:
    browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr[5]/td[2]').is_displayed()
    time.sleep(waittime)
except:
    print('table not visible on order page ')
    time.sleep(waittime)

count = 0
for dl in dl_numbers:
    string = '/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr['+str(count+1)+']/td[2]'
    assert dl in browser.find_element_by_xpath(string).text.replace(" ", "")
    count=count+1

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
try:
    browser.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr[1]/td[2]').is_displayed()
    time.sleep(waittime)
except:
    print('table not visible on details page')
    time.sleep(waittime)

count = 0
for dl in dl_numbers:
    string = '/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr[' + str(count+1) + ']/td[2]'
    assert dl in browser.find_element_by_xpath(string).text.replace(" ", "")
    count=count+1

#assert correct number of DLs in cart and price
total = 'Total Licence(s): '+str(len(dl_numbers))+' | Amount ($): '+str(len(dl_numbers)*2)+'.00'
assert browser.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/div[1]/div[2]/h4').text == total

print('Business Manual Entry Test Passed')

#browser.find_element_by_partial_link_text('Next').click()



#not implemented stuff
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