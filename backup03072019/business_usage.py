from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import csv
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

#csv upload
csv_location = os.getcwd() + '\\licences-tests.csv'
#browser.find_element_by_id('excelInput').send_keys(csv_location)
browser.find_element_by_xpath('//*[@id="excelInput"]').send_keys(csv_location)

#error icon should be shown for invalid licences in csv
try:
    'warning' in browser.page_source
except:
    print("DL error icon not shown")


#
#ensuring that all entries from the csv were uploaded,note validation is not 100%
#
# open the file in universal line ending mode 
with open('licenses.csv', 'rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]
from_csv = data['Drivers License']

#removes invalid license number, not 100% proof(only checks length and dashes)
print('retrived from csv:')
print(from_csv)
for number in from_csv:
    if number.count("-") != 2 and len(number) != 17: from_csv.remove(number)
print('after removing invalid:')
print(from_csv)

time.sleep(waittime)
#check to ensure all licenses are uploaded correctly
count = 1
for number in from_csv:
    string = '/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr[' + str(count) + ']/td[2]'
    assert number in browser.find_element_by_xpath(string).text.replace(" ", "") 
    count+=1

#refresh to ensure sessions are working
browser.refresh()
try:
    browser.find_element_by_xpath('/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr[5]/td[2]').is_displayed()
    time.sleep(waittime)
except:
    print('table not visible on order page')
    time.sleep(waittime+5)

#check to ensure all licenses are uploaded correctly after refresh
count = 1
for number in from_csv:
    string = '/html/body/app-root/div/app-enter-details/div/app-order-table/table/tbody/tr[' + str(count) + ']/td[2]'
    assert number in browser.find_element_by_xpath(string).text.replace(" ", "") 
    count+=1

#Enter details page
browser.find_element_by_partial_link_text('Next').click()

try:
    browser.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr[5]/td[2]').is_displayed()
    time.sleep(waittime)
except:
    print('table not visible on order page')
    time.sleep(waittime+5)

#check to ensure all licenses are uploaded correctly after refresh
count = 1
for number in from_csv:
    string = '/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr[' + str(count) + ']/td[2]'
    assert number in browser.find_element_by_xpath(string).text.replace(" ", "") 
    count+=1

#refresh to ensure sessions are working
browser.refresh()
try:
    browser.find_element_by_xpath('/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr[5]/td[2]').is_displayed()
    time.sleep(waittime)
except:
    print('table not visible on order page')
    time.sleep(waittime+5)

#check to ensure all licenses are uploaded correctly after refresh
count = 1
for number in from_csv:
    string = '/html/body/app-root/div/app-confirm-order/div/app-order-table/table/tbody/tr[' + str(count) + ']/td[2]'
    assert number in browser.find_element_by_xpath(string).text.replace(" ", "") 
    count+=1

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


print('Business Csv Entry Test Passed')
browser.find_element_by_partial_link_text('Next').click()

'''
#PAYMENT PAGE !not implemented
browser.find_element_by_partial_link_text('I Paid!').click()

#RESULTS PAGE
#allow table to load
time.sleep(2)
count = 1
for number in from_csv:
    string = '/html/body/app-root/div/app-report/div/table/tbody/tr[' + str(count) + ']/td[2]'
    string2 = '/html/body/app-root/div/app-report/div/table/tbody/tr[' + str(count) + ']/td[3]/span'
    #assert that correct DL number was shown
    assert number in browser.find_element_by_xpath(string).text.replace(" ", "") 
    #assert that correct value was returned
    #doesnt work cuz return doesnt return right thing literally just math.random or something idk
    #assert browser.find_element_by_xpath(string2).text == dl_key.get(number)
    print(browser.find_element_by_xpath(string2).text, ' - should be - ',dl_key.get(number))
    count+=1

#transaction details is not implemented
#check $$, name, address, idk whatever they inputed previously that is then shown again

#
#submit feedback
#

'''