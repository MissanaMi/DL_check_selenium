from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
import string
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

dl_numbers = []

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

#generate 100 random dls
for i in range(99):
    dl_number = random.choice(string.ascii_uppercase)
    for j in range(14):
        if j == 12:
            dl_number = dl_number + str(random.randint(0,3))
        elif j == 13:
            if dl_number[13] == '3':
                dl_number = dl_number + str(random.randint(0,1))
            elif dl_number[13] == '0':
                dl_number = dl_number + str(random.randint(1,9))
            else:
                dl_number = dl_number + str(random.randint(0,9))
        else:
            dl_number = dl_number + str(random.randint(0,9))
    enter_licence_page.multiple_input1(dl_number[0:5])
    enter_licence_page.multiple_input2(dl_number[5:10])
    enter_licence_page.multiple_input3(dl_number[10:17]) 
    enter_licence_page.add_licence()
    dl_numbers.append(dl_number)
    time.sleep(waittime/2)

time.sleep(waittime)

for _ in range(9):
    enter_licence_page.load_more()
    time.sleep(waittime*2)

count = 0
for dl in dl_numbers:
    assert dl in enter_licence_page.table_row_column(count+1,2).replace("-", "")
    count=count+1

total = 'Total Licence(s): '+str(len(dl_numbers))+' | Amount ($): '+str(len(dl_numbers)*2)+'.00'
assert enter_licence_page.total() == total

browser.refresh()

for _ in range(9):
    enter_licence_page.load_more()
    time.sleep(waittime*2)

count = 0
for dl in dl_numbers:
    assert dl in enter_licence_page.table_row_column(count+1,2).replace("-", "")
    count=count+1

total = 'Total Licence(s): '+str(len(dl_numbers))+' | Amount ($): '+str(len(dl_numbers)*2)+'.00'
assert enter_licence_page.total() == total


browser.find_element_by_partial_link_text('Next').click()
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


for _ in range(9):
    confirm_page.load_more()
    time.sleep(waittime*2)

count = 0
for dl in dl_numbers:
    assert dl in confirm_page.table_row_column(count+1,2).replace("-", "")
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