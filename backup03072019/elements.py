from selenium import webdriver
from selenium.webdriver.support.ui import Select

#
#make a reference for common feild entries i.e DL numbers, names, addresses, etc so no need to re-write
#

class Common:
    back = 'asdf'
    cancel = 'asdf'
    next = 'asdf'
    french = 'asdf'
    ontario = 'asdf'


class Homepage:
    proceed = browser.find_element_by_link_text('Check Driver\'s Licence Status')

class Enter_DL:
    one_licence = 'asdf'
   
    multiple_licence = 'asdf'
    
    personal_feild1 = 'asdf'
    personal_feild2 = 'asdf'
    personal_feild3 = 'asdf'

    manual = 'asdf'
    csv = 'asdf'

    multiple_feild1 = 'asdf'
    multiple_feild2 = 'asdf'
    multiple_feild3 = 'asdf'

    add = 'asdf'

    table = 'asdf'
    total = 'asdf'

class Enter_details:
    email = 'asdf'
    intended_use = 'asdf'
    phone = 'asdf'
    name = 'asdf'
    company = 'asdf'
    country = 'asdf'
    address = 'asdf'
    city = 'asdf'
    province = 'asdf'
    postal = 'asdf'

    table = 'asdf'
    total = 'asdf'
