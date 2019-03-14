from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import page_object
import pay

browser = webdriver.Firefox()
#browser = webdriver.Chrome()
#browser = webdriver.Edge()
#browser = webdriver.Ie(r"C:\\Users\\MissanMi\\project\\DL_check_selenium\\IEDriverServer.exe")

customer_email = "JohnSmith@gmail.com"
customer_phone = "9051234567"
customer_name = "John Smith"
customer_company = "N/A"
customer_address = "123 Baker street"
customer_city = "Toronto"
customer_postal = "H6L5W3"
customer_use = "Business Use"
customer_country = "Canada"
customer_province = "Ontario"

waittime = 1.5

main_page = page_object.MainPage(browser)
common_page = page_object.CommonPage(browser)
enter_licence_page = page_object.EnterDL(browser)
confirm_page = page_object.ConfirmOrder(browser)
payment_page = pay.PaymentPage(browser)
results_single_page = page_object.Results_single(browser)

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
time.sleep(waittime/4)

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

browser.refresh()
time.sleep(waittime)

#recheck items are still in the cart after refresh
assert dl_number in confirm_page.table()

#assert correct number of DLs in cart and price
assert confirm_page.total() == 'Total Licence(s): 1 | Amount ($): 2.00'

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

common_page.next()

#wait until clickable or some functio like that

time.sleep(10)#long wait this page takes a while
common_page.next()

payment_page.enter_details(1)

time.sleep(10)

##############################ReSUlTs CHeCk#####################

#results_single_page.status() ####no confirmed statuses given for spefic DL
#results_single_page.description() ####above
results_single_page.dl_number(dl_number)
results_single_page.purchaser_name(customer_name)
result_price = '$2.00 CAD'
results_single_page.result_price(result_price)
payment_page.payment_results()

print('Basic Usage Passing')

browser.close()