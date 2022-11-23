import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from validators import date_validator
from utils.date_select import DateSelect
from utils.guest import setGuest
from utils.collection import Collection
from utils.get_excel import excel_maker


class Booking(webdriver.Chrome):
    
    def __init__(self, auto_shut=False):
        # environment save
        os.environ['PATH'] += r'C:/Program Files/SeleniumDrivers'

        # setting the option for the webdriver
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        # initializing the parent class
        super().__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

        # setting the auto quit
        self.auto_shut = auto_shut
        

    def open_first_page(self):
        # opening the booking page
        url =  'https://www.booking.com/'
        self.get(url)
        try:                   
            destination_element = self.find_element(By.ID, 'ss')
            return True
        except Exception as e:      
            self.close()                 
            return False  
        

    def change_currency(self, currency=None):
        '''
        This function is to change the currency of the function
        Default will be selected by the website
        If the user enters a different value othre than the default,
        only then the currency will change 
        '''
        if currency:
            currency_button = self.find_element(By.CSS_SELECTOR, 
                'button[data-tooltip-text="Choose your currency"]'
                )
            current_currency = currency_button.text.split()[0]
            if current_currency != currency:
                currency_button.click()
                specific_currency_element = self.find_element(
                    By.CSS_SELECTOR, 
                    f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
                    )
                specific_currency_element.click()
        
            

    def select_destination(self, destination):
        '''
        This function will insert the destination in the website
        '''
        destination_element = self.find_element(By.ID, 'ss')
        destination_element.clear()
        destination_element.send_keys(f'{destination}')
        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()


    def set_dates(self,start_date, end_date):
        '''
        This function will set the check-in and check-out dates
        start date is the check-in date
        end_date is the check-out date
        '''
        ds = DateSelect(self)
        first_cnt = ds.get_click_count(start_date)
        re_start_date = date_validator.date_formatter(start_date)
        ds.confirm_date(first_cnt, re_start_date)
        second_cnt = ds.get_click_count(end_date, first_cnt)
        re_end_date = date_validator.date_formatter(end_date)
        ds.confirm_date(second_cnt, re_end_date)



    def set_guests(self, adult:int, children:int, children_ages:list, rooms:int):
        '''
        This function will set the number of adults, children and rooms required 
        '''
        guest_element = self.find_element(By.ID, 'xp__guests__toggle')
        guest_element.click()
        guest = setGuest(self)
        guest.set_adult(adult)
        if children and children_ages:
            guest.set_children(children, children_ages)
        guest.set_room(rooms)

    
    def apply_search(self):
        '''
        This function will initiate the search
        '''
        search_element = self.find_element(By.CLASS_NAME, 'sb-searchbox__button ')
        search_element.click()

    def make_data(self, destination):
        col = Collection(driver=self)
        the_data = col.collect_data()
        excel_maker(the_data, destination)
                

    def __exit__(self, exc_type, exc, traceback):
        if self.auto_shut:
            self.quit()
