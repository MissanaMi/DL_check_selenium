from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

waittime= 1.5

def details_populate():
    #Customer Information
    browser.find_element_by_id('emailAddress').send_keys(customer_email)

    browser.find_element_by_id('phoneNumber').send_keys(customer_phone)

    browser.find_element_by_id('name').send_keys(customer_name)

    browser.find_element_by_id('company').send_keys(customer_company)

    browser.find_element_by_id('address').send_keys(customer_address)

    browser.find_element_by_id('city').send_keys(customer_city)

    browser.find_element_by_id('postalCode').send_keys(customer_postal)

    select = Select(browser.find_element_by_id('intendedUse'))
    select.select_by_visible_text(customer_use)

    select = Select(browser.find_element_by_id('country'))
    select.select_by_visible_text(customer_country)

    #select = Select(browser.find_element_by_id('Province'))
    #select.select_by_visible_text(customer_province)

def csv_upload():
    #csv upload
    csv_location = os.getcwd() + '\\licences-tests.csv'
    #browser.find_element_by_id('excelInput').send_keys(csv_location)
    browser.find_element_by_xpath('//*[@id="excelInput"]').send_keys(csv_location)

    #error icon should be shown for invalid licences in csv
    try:
        'warning' in browser.page_source
    except:
        print("DL error icon not shown")
    time.sleep(waittime)

def manual_upload(dl_numbers):
    for dl in dl_numbers:
        browser.find_element_by_id('licenceInput11').send_keys(dl[0:5])
        browser.find_element_by_id('licenceInput21').send_keys(dl[6:11])
        browser.find_element_by_id('licenceInput31').send_keys(dl[12:17])
        browser.find_element_by_partial_link_text('Add Licence').click()

