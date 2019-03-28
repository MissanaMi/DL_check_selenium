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

# value key for correct returns for certain DL numbers
# maybe move this to the csv column two just for testing? #### | valid/invalid/etc
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
payment_page = pay.PaymentPage(browser)


# do this better, probably with args, it could have been done in the time it took to write this comment
############################################
dl_number = 'A0124-68024-11111'
############################################

common_page.get_page()

# Home
time.sleep(waittime)
main_page.proceed()
time.sleep(waittime)

# Enter License Page
try:
    enter_licence_page.one_licence().click()
    time.sleep(waittime)
except:
    print('Already selected')

# Enter DL
enter_licence_page.single_input1(dl_number[0:5])
enter_licence_page.single_input2(dl_number[6:11])
enter_licence_page.single_input3(dl_number[12:17])

common_page.next()
time.sleep(waittime)

# assert items are still in cart
assert dl_number in confirm_page.table()

common_page.cancel()
common_page.cancel_confirm()

#Home
time.sleep(waittime)
main_page.proceed()
time.sleep(waittime)

assert browser.find_element_by_id('licenceInput10').get_attribute('value') != dl_number[0:5]

# Enter DL
enter_licence_page.single_input1(dl_number[0:5])
enter_licence_page.single_input2(dl_number[6:11])
enter_licence_page.single_input3(dl_number[12:17])

common_page.next()

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
        time.sleep(waittime)
        break

payment_page.back()
time.sleep(waittime*5)

#assert everything is still there
# does not do drop downs, they return ints not worth setting up conditions for something that might change
assert customer_phone in browser.find_element_by_id('phoneNumber').get_attribute('value')
assert customer_name in browser.find_element_by_id('name').get_attribute('value')
assert customer_company in browser.find_element_by_id('company').get_attribute('value')
assert customer_email in browser.find_element_by_id('emailAddress').get_attribute('value')
assert customer_address in browser.find_element_by_id('address').get_attribute('value')
assert customer_city in browser.find_element_by_id('city').get_attribute('value')
assert customer_postal in browser.find_element_by_id('postalCode').get_attribute('value')

common_page.back()

assert browser.find_element_by_id('licenceInput10').get_attribute('value') == dl_number[0:5]

common_page.next()
time.sleep(waittime)

#assert everything is still there
# does not do drop downs, they return ints not worth setting up conditions for something that might change
assert customer_phone in browser.find_element_by_id('phoneNumber').get_attribute('value')
assert customer_name in browser.find_element_by_id('name').get_attribute('value')
assert customer_company in browser.find_element_by_id('company').get_attribute('value')
assert customer_email in browser.find_element_by_id('emailAddress').get_attribute('value')
assert customer_address in browser.find_element_by_id('address').get_attribute('value')
assert customer_city in browser.find_element_by_id('city').get_attribute('value')
assert customer_postal in browser.find_element_by_id('postalCode').get_attribute('value')

common_page.cancel()
common_page.cancel_confirm()

#Home
time.sleep(waittime)
main_page.proceed()
time.sleep(waittime)

# Enter DL
enter_licence_page.single_input1(dl_number[0:5])
enter_licence_page.single_input2(dl_number[6:11])
enter_licence_page.single_input3(dl_number[12:17])

common_page.next()
time.sleep(waittime)

#assert everything is gone after cancel
# does not do drop downs, they return ints not worth setting up conditions for something that might change
assert customer_phone not in browser.find_element_by_id('phoneNumber').get_attribute('value')
assert customer_name not in browser.find_element_by_id('name').get_attribute('value')
assert customer_company not in browser.find_element_by_id('company').get_attribute('value')
assert customer_email not in browser.find_element_by_id('emailAddress').get_attribute('value')
assert customer_address not in browser.find_element_by_id('address').get_attribute('value')
assert customer_city not in browser.find_element_by_id('city').get_attribute('value')
assert customer_postal not in browser.find_element_by_id('postalCode').get_attribute('value')

print('Basic Clearing Passing')
