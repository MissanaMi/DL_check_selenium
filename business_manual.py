from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import page_object
import pay

browser = webdriver.Firefox()
#browser = webdriver.Chrome()
#browser = webdriver.Edge()
#browser = webdriver.Ie(r"C:\\Users\\MissanMi\\project\\DL_check_selenium\\IEDriverServer.exe")

waittime = 3

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

main_page = page_object.MainPage(browser)
common_page = page_object.CommonPage(browser)
enter_licence_page = page_object.EnterDL(browser)
confirm_page = page_object.ConfirmOrder(browser)
payment_page = pay.PaymentPage(browser)
results_single_page = page_object.Results_single(browser)
results_multiple_page = page_object.Results_multiple(browser)


dl_numbers = ['L0127-15675-70417','K0733-19005-65811','M2135-18407-40922','M8231-35818-00102','A1742-60506-10101','A5359-30506-71010','L0001-75688-30707','K0733-12887-35522','T7565-75205-80513','A1013-78506-55101']


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

time.sleep(waittime)
enter_licence_page.add_licence()

for i in range(1,len(dl_numbers)):
    if i != 0:
        enter_licence_page.multiple_input1(dl_numbers[i][0:5])
        enter_licence_page.multiple_input2(dl_numbers[i][6:11])
        enter_licence_page.multiple_input3(dl_numbers[i][12:17])
        time.sleep(waittime/3)
        enter_licence_page.add_licence()

time.sleep(waittime)
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

count = 0
for dl in dl_numbers:
    assert dl in confirm_page.table_row_column(count+1,2)
    count=count+1

total = 'Total Licence(s): '+str(len(dl_numbers))+' | Amount ($): '+str(len(dl_numbers)*2)+'.00'
assert confirm_page.total() == total

browser.refresh()
time.sleep(waittime)

count = 0
for dl in dl_numbers:
    assert dl in confirm_page.table_row_column(count+1,2)
    count=count+1

total = 'Total Licence(s): '+str(len(dl_numbers))+' | Amount ($): '+str(len(dl_numbers)*2)+'.00'
assert confirm_page.total() == total

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


while True:
    try:
        common_page.next()
    except:
        time.sleep(waittime)
    if 'https://www.beanstream.com' in browser.current_url:
        break


payment_page.enter_details(len(dl_numbers))


while browser.current_url != 'http://etcbitdcapmdw30.cihs.ad.gov.on.ca/Pris_Carrier/dlc/report':
    time.sleep(5)
    

#results_single_page.status()       no confirmed statuses given for spefic DL
#results_single_page.description()  ^^^^
results_multiple_page.expand()

#purchaser name
results_multiple_page.purchaser_name(customer_name)

#confirm price on transaction details
result_price = '$'+str(len(dl_numbers)*2)+'.00 CAD'
results_multiple_page.result_price(result_price)

#confirm dl and status
results_multiple_page.dl_number_and_status(dl_numbers)

#print status totals 
print(results_multiple_page.status())

#confirm payment info
payment_page.payment_results()

print('Basic Usage Passing')

browser.close()