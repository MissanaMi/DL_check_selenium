from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
import string

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

dl_numbers = []

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

#generate 100 random dls
for i in range(100):
    dl_number = random.choice(string.ascii_uppercase)
    for j in range(16):
        if j == 14:
            dl_number = dl_number + str(random.randint(0,3))
        elif j == 15:
            if dl_number[15] == '3':
                dl_number = dl_number + str(random.randint(0,1))
            elif dl_number[15] == '0':
                dl_number = dl_number + str(random.randint(1,9))
            else:
                dl_number = dl_number + str(random.randint(0,9))
        else:
            dl_number = dl_number + str(random.randint(0,9))
    browser.find_element_by_id('licenceInput11').send_keys(dl_number[0:5])
    browser.find_element_by_id('licenceInput21').send_keys(dl_number[6:11])
    browser.find_element_by_id('licenceInput31').send_keys(dl_number[12:17])
    browser.find_element_by_partial_link_text('Add Licence').click()
    dl_numbers.append(dl_number)
    time.sleep(waittime/4)

print(dl_numbers)

for _ in range(10):
    browser.find_element_by_link_text('Load More').click()
    time.sleep(waittime)

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
'''
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

'''

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