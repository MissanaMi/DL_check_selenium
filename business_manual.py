from selenium import webdriver
from selenium.webdriver.support.ui import Select
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

#do this better, probably with args, it could have been done in the time it took to write this comment
############################################
dl_number = 'A0124-68024-11111'

dl_numbers = ['A0124-68024-11111','A0224-68024-11111','A0324-68024-11111','A0424-68024-11111','A0524-68024-11111']
############################################

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

enter_licence_page.multiple_input1(dl_numbers[0][0:5])

enter_licence_page.multiple_input2(dl_numbers[0][6:11])

enter_licence_page.multiple_input3('aaaaa')

enter_licence_page.add_licence()
time.sleep(waittime)

#error icon should be shown for invalid format
try:
    'warning' in browser.page_source
except:
    print("DL error icon not shown")


enter_licence_page.multiple_input3_clear()

enter_licence_page.multiple_input3(dl_numbers[0][12:17])

#check icon should be shown after invalid input is corrected
try:
    'check_circle' in browser.page_source
except:
    print("DL check icon not shown")

enter_licence_page.add_licence()

#native alerts are a pain to deal with

#move this entry to a for look once the alert for duplicate is implemented
enter_licence_page.multiple_input1(dl_numbers[1][0:5])
enter_licence_page.multiple_input2(dl_numbers[1][6:11])
enter_licence_page.multiple_input3(dl_numbers[1][12:17])
enter_licence_page.add_licence()

enter_licence_page.multiple_input1(dl_numbers[2][0:5])
enter_licence_page.multiple_input2(dl_numbers[2][6:11])
enter_licence_page.multiple_input3(dl_numbers[2][12:17])
enter_licence_page.add_licence()

enter_licence_page.multiple_input1(dl_numbers[3][0:5])
enter_licence_page.multiple_input2(dl_numbers[3][6:11])
enter_licence_page.multiple_input3(dl_numbers[3][12:17])
enter_licence_page.add_licence()

enter_licence_page.multiple_input1(dl_numbers[4][0:5])
enter_licence_page.multiple_input2(dl_numbers[4][6:11])
enter_licence_page.multiple_input3(dl_numbers[4][12:17])
enter_licence_page.add_licence()

count = 0
for dl in dl_numbers:
    assert dl in enter_licence_page.table_row_column(count+1,2)
    count=count+1

total = 'Total Licence(s): '+str(len(dl_numbers))+' | Amount ($): '+str(len(dl_numbers)*2)+'.00'
assert enter_licence_page.total() == total

browser.refresh()

count = 0
for dl in dl_numbers:
    assert dl in enter_licence_page.table_row_column(count+1,2)
    count=count+1

total = 'Total Licence(s): '+str(len(dl_numbers))+' | Amount ($): '+str(len(dl_numbers)*2)+'.00'
assert enter_licence_page.total() == total

common_page.next()
time.sleep(waittime)

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

count = 0
for dl in dl_numbers:
    assert dl in confirm_page.table_row_column(count+1,2)
    count=count+1

total = 'Total Licence(s): '+str(len(dl_numbers))+' | Amount ($): '+str(len(dl_numbers)*2)+'.00'
assert confirm_page.total() == total

browser.refresh()

count = 0
for dl in dl_numbers:
    assert dl in confirm_page.table_row_column(count+1,2)
    count=count+1

total = 'Total Licence(s): '+str(len(dl_numbers))+' | Amount ($): '+str(len(dl_numbers)*2)+'.00'
assert confirm_page.total() == total

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


    