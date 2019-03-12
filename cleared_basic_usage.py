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
############################################

common_page.get_page()

#Home
time.sleep(waittime)
main_page.proceed()
time.sleep(waittime)

#Enter License Page
try:
    enter_licence_page.one_licence().click()
    time.sleep(waittime)
except:
    print('Already selected')

enter_licence_page.single_input1(dl_number[0:5])

enter_licence_page.single_input2(dl_number[6:11])

enter_licence_page.single_input3('aaaaa')

common_page.next()
time.sleep(waittime)

#error icon should be shown for invalid format
try:
    'warning' in browser.page_source
except:
    print("DL error icon not shown")


enter_licence_page.single_input3_clear()

enter_licence_page.single_input3(dl_number[12:17])

#check icon should be shown after invalid input is corrected
try:
    'check_circle' in browser.page_source
except:
    print("DL check icon not shown")

common_page.next()
time.sleep(waittime)

#assert items are still in cart
assert dl_number in confirm_page.table()

#assert correct number of DLs in cart and price
assert confirm_page.total() == 'Total Licence(s): 1 | Amount ($): 2.00'

common_page.cancel()

#Home
time.sleep(waittime)
main_page.proceed()
time.sleep(waittime)

'''
print('-',enter_licence_page.single_input1.text,'-')
assert enter_licence_page.single_input1 == '  '
assert enter_licence_page.single_input2 == '  '
assert enter_licence_page.single_input3 == '  '

print('Feilds Cleared Test Passed')
'''