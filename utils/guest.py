from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class setGuest:

    def __init__(self, driver:WebDriver) -> None:
        self.driver = driver


    def set_adult(self, adult:int):
        adult_element = self.driver.find_element(By.CSS_SELECTOR, 'span[data-adults-count]')
        adult_number = int(adult_element.text.split()[0])

        if adult != adult_number:
            diff = abs(adult-adult_number)
            if adult > adult_number:
                adult_add_element = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
                for _ in range(diff):
                    adult_add_element.click()
            elif adult < adult_number:
                adult_sub_element = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
                for _ in range(diff):
                    adult_sub_element.click()


    def set_children(self, children:int, children_ages:list):
        children_element = self.driver.find_element(By.CSS_SELECTOR, 'span[data-children-count]')
        children_number = int(children_element.text.split()[0])

        if children != children_number:
            diff = abs(children-children_number)
            if children > children_number:
                children_add_element = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Children"]')
                for _ in range(diff):
                    children_add_element.click()

            elif children < children_number:
                children_sub_element = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Children"]')
                for _ in range(diff):
                    children_sub_element.click()

            for i,age in enumerate(children_ages):
                age_click_element = self.driver.find_element(By.CSS_SELECTOR, f'select[data-group-child-age="{i}"]')    
                age_click_element.click()
                age_select_element = age_click_element.find_element(By.CSS_SELECTOR, f'option[value="{age}"]')
                age_select_element.click()

    
    def set_room(self, room:int):
        room_element = self.driver.find_element(By.CSS_SELECTOR, 'span[data-room-count]')
        room_number = int(room_element.text.split()[0])

        if room != room_number:
            diff = abs(room-room_number)
            if room > room_number:
                room_add_element = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Rooms"]')
                for _ in range(diff):
                    room_add_element.click()
            elif room < room_number:
                room_sub_element = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Rooms"]')
                for _ in range(diff):
                    room_sub_element.click()
        