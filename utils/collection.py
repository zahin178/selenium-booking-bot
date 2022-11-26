from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Collection:

    def __init__(self, driver:WebDriver) -> None:
        self.driver = driver
        self.data = []

    def get_page_count(self):
        try:
            nav_element = self.driver.find_element(By.CLASS_NAME, 'a8b500abde')
            nav_element_lists = nav_element.find_elements(By.TAG_NAME, 'li')
            nav_element_lists_last = nav_element_lists[-1].text
            page_count = int(nav_element_lists_last)+1
        except Exception as e:
            page_count = 2

        return page_count

    def collect_data(self):
        counter = 1
        cnt = self.get_page_count()
        for _ in range(1,cnt):
            self.driver.refresh()
            full_element = self.driver.find_element(By.CLASS_NAME, 'd4924c9e74')
            full_element_boxes = full_element.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
            print('Total hotels found',len(full_element_boxes))
            for box in full_element_boxes:
                print(f'Hotel number {counter}')
                box_info = {}
                try:
                    title_element = box.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]')
                    title = title_element.text
                except Exception as e:
                    title = None
                box_info['title'] = title

                try:
                    review_score_element = box.find_element(By.CSS_SELECTOR, 'div[data-testid="review-score"]')
                    score_element = review_score_element.find_element(By.CLASS_NAME, 'd10a6220b4')
                    score = score_element.text
                except Exception as e:
                    score = None
                box_info['score'] = score

                try:
                    review_element = review_score_element.find_element(By.CLASS_NAME, 'db63693c62')
                    review_cnt = review_element.text
                except Exception as e:
                    review_cnt = None
                box_info['review_cnt'] = review_cnt

                try:
                    distance_element = box.find_element(By.CSS_SELECTOR, 'span[data-testid="distance"]')
                    distance = distance_element.text
                except Exception as e:
                    distance = None
                box_info['distance'] =  distance

                self.data.append(box_info)

                counter+=1

            try:
                next_page_element = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next page"]')
                next_page_element.click()
            except Exception as e:
                pass

            

        return self.data


