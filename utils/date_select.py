from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class DateSelect:
    months = [
        'january', 'february', 'march', 'april', 'may', 'june', 'july',
        'august', 'september', 'october', 'november', 'december'
    ]

    def __init__(self, driver:WebDriver) -> None:
        self.driver = driver

    def get_click_count(self,date,cnt=0):
        date_month_index = int(date[2:4])-1
        date_month = self.months[date_month_index]

        month_names = self.driver.find_elements(By.CLASS_NAME, 'bui-calendar__month')

        first_month_text = month_names[0].text
        second_month_text = month_names[1].text

        first_month = first_month_text.split()[0].lower()
        second_month = second_month_text.split()[0].lower()
        second_month_index = self.months.index(second_month)

        if date_month == first_month or date_month == second_month:
            cnt = 0
        elif date_month_index > second_month_index:
            cnt = date_month_index - second_month_index
        elif date_month_index < second_month_index:
            cnt = (11-second_month_index)+(date_month_index+1)

        return cnt

    def confirm_date(self, cnt, date):
        try:
            next_button = self.driver.find_element(By.CLASS_NAME, 'bui-calendar__control--next')
            for _ in range(cnt):
                next_button.click()
            
            date_element = self.driver.find_element(By.CSS_SELECTOR, f'td[data-date="{date}"]')
            date_element.click()
        except Exception as e:
            print(f'Exception {e}')