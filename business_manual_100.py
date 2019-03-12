from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
import string
import page_object
import pay

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

customer_email = "JohnSmith@gmail.com"
customer_phone = "9051234567"
customer_name = "John Smith"
customer_company = "N/A"
customer_address = "123 Baker street"
customer_city = "Toronto"
customer_postal = "H6L5W3"
customer_use = "Personal Use"
customer_country = "Canada"
customer_province = "Ontario"

waittime = 1.5

main_page = page_object.MainPage(browser)
common_page = page_object.CommonPage(browser)
enter_licence_page = page_object.EnterDL(browser)
confirm_page = page_object.ConfirmOrder(browser)
payment_page = pay.PaymentPage(browser)
results_page = page_object.Results_single(browser)

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
    time.sleep(waittime)

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
confirm_page.email(customer_email)
confirm_page.phone(customer_phone)
confirm_page.name(customer_name)
confirm_page.company(customer_company)
confirm_page.address(customer_address)
confirm_page.city(customer_city)
confirm_page.postal_code(customer_postal)

confirm_page.intended_use(customer_use)
confirm_page.country(customer_country)
confirm_page.province_canada(customer_province)


for _ in range(9):
    confirm_page.load_more()
    time.sleep(waittime*2)

count = 0
for dl in dl_numbers:
    assert dl in confirm_page.table_row_column(count+1,2).replace("-", "")
    count=count+1

total = 'Total Licence(s): '+str(len(dl_numbers))+' | Amount ($): '+str(len(dl_numbers)*2)+'.00'
assert confirm_page.total() == total

common_page.next()

#wait until clickable or some functio like that

time.sleep(5)#long wait this page takes a while
common_page.next()

payment_page.enter_details(1)

while True:
    try:
        element = results_page.result_displayed()
        break
    except:
        time.sleep(2)




print('Business Manual Entry Test Passed')