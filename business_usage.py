from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import csv
import time
import page_object

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

main_page = page_object.MainPage(browser)
common_page = page_object.CommonPage(browser)
enter_licence_page = page_object.EnterDL(browser)
confirm_page = page_object.ConfirmOrder(browser)
payment_page = page_object.Payment(browser)

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
    print('Multiple Licence tab not loaded')

#radial buttons
enter_licence_page.csv_radial()

#csv upload
csv_location = os.getcwd() + '\\licences-tests.csv'
#browser.find_element_by_id('excelInput').send_keys(csv_location)
#browser.find_element_by_xpath('//*[@id="excelInput"]').send_keys(csv_location)
enter_licence_page.csv_upload(csv_location)

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

for number in from_csv:
    if number.count("-") != 2 and len(number) != 17: from_csv.remove(number)

time.sleep(waittime)

count = 0
for dl in from_csv:
    assert dl in enter_licence_page.table_row_column(count+1,2)
    count=count+1

total = 'Total Licence(s): '+str(len(from_csv))+' | Amount ($): '+str(len(from_csv)*2)+'.00'
assert enter_licence_page.total() == total

common_page.refresh()

count = 0
for dl in from_csv:
    assert dl in enter_licence_page.table_row_column(count+1,2)
    count=count+1

total = 'Total Licence(s): '+str(len(from_csv))+' | Amount ($): '+str(len(from_csv)*2)+'.00'
assert enter_licence_page.total() == total

common_page.next()

time.sleep(waittime)

count = 0
for dl in from_csv:
    assert dl in confirm_page.table_row_column(count+1,2)
    count=count+1

total = 'Total Licence(s): '+str(len(from_csv))+' | Amount ($): '+str(len(from_csv)*2)+'.00'
assert confirm_page.total() == total

browser.refresh()

count = 0
for dl in from_csv:
    assert dl in confirm_page.table_row_column(count+1,2)
    count=count+1

total = 'Total Licence(s): '+str(len(from_csv))+' | Amount ($): '+str(len(from_csv)*2)+'.00'
assert confirm_page.total() == total

#Customer Information
confirm_page.email("JohnSmith@gmail.com")
confirm_page.phone("905-678-9012")
confirm_page.name("John Smith")
confirm_page.company("N/A")
confirm_page.address("123 Baker street")
confirm_page.city("Toronto")
confirm_page.postal_code("H6L5W3")

confirm_page.intended_use('Personal Use')
confirm_page.country('Canada')
#confirm_page.province('Ontario')

print('Business CSV Entry Test Passed')

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