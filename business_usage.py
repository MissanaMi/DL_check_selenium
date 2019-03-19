from selenium import webdriver
import os
import csv
import time
import page_object
import pay

########################################################################################
########################################################################################
####                                DISCLAIMER                                      ####
####                                                                                ####
####          This test does not use the same validation as the dlc site            ####
####  Therefore this test is not intended to use use to test the sites validation   ####
####                  See line ~101 for low level validation done                   ####
####                                                                                ####
########################################################################################
########################################################################################

browser = webdriver.Firefox()
# browser = webdriver.Chrome()
# browser = webdriver.Edge()
# browser = webdriver.Ie(r"C:\\Users\\MissanMi\\project\\DL_check_selenium\\IEDriverServer.exe")

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
results_page = page_object.Results_multiple(browser)

common_page.get_page()

# Home
time.sleep(waittime)
main_page.proceed()
time.sleep(waittime)

# Enter License Page
try:
    enter_licence_page.multiple_licences()
    time.sleep(waittime)
except:
    print('Multiple Licence tab not loaded')

# radial buttons
enter_licence_page.csv_radial()

# csv upload
csv_location = os.getcwd() + '\\licences-tests.csv'
enter_licence_page.csv_upload(csv_location)

# error icon should be shown for invalid licences in csv
try:
    'warning' in browser.page_source
except:
    print("DL error icon not shown")


#
# ensuring that all entries from the csv were uploaded,note validation is not 100%
#
# open the file in universal line ending mode 
with open('licences-tests.csv', 'rU') as infile:
    # read the file as a dictionary for each row ({header : value})
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]
from_csv = data['Drivers Licence']

for number in from_csv:
    if number.count("-") != 2 and len(number) != 17: from_csv.remove(number)

time.sleep(waittime)
count = 0
for dl in from_csv:
    assert dl in enter_licence_page.table_row_column(count+1, 2)
    count = count+1

total = 'Total Licence(s): '+str(len(from_csv))+' | Amount ($): '+str(len(from_csv)*2)+'.00'
assert enter_licence_page.total() == total

common_page.refresh()

count = 0
for dl in from_csv:
    assert dl in enter_licence_page.table_row_column(count+1, 2)
    count=count+1

total = 'Total Licence(s): '+str(len(from_csv))+' | Amount ($): '+str(len(from_csv)*2)+'.00'
assert enter_licence_page.total() == total

common_page.next()

time.sleep(waittime)

count = 0
for dl in from_csv:
    assert dl in confirm_page.table_row_column(count+1,2)
    count = count+1

total = 'Total Licence(s): '+str(len(from_csv))+' | Amount ($): '+str(len(from_csv)*2)+'.00'
assert confirm_page.total() == total

browser.refresh()

count = 0
for dl in from_csv:
    assert dl in confirm_page.table_row_column(count+1,2)
    count = count+1

total = 'Total Licence(s): '+str(len(from_csv))+' | Amount ($): '+str(len(from_csv)*2)+'.00'
assert confirm_page.total() == total

# Customer Information
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

time.sleep(waittime)
payment_page.enter_details(len(from_csv))


url = common_page.get_baseurl()
url = url + 'report'

while browser.current_url != url:
    time.sleep(5)
    

# results_single_page.status()       no confirmed statuses given for spefic DL
# results_single_page.description()  ^^^^
results_page.expand()

# purchaser name
results_page.purchaser_name(customer_name)

# confirm price on transaction details
result_price = '$'+str(len(from_csv)*2)+'.00 CAD'
results_page.result_price(result_price)

# confirm dl and status
results_page.dl_number_and_status(from_csv)

# confirm payment info
payment_page.payment_results()

print('Basic Usage Passing')

browser.close()
