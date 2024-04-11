from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def find_by_hashtag(hashtag, wait):
    search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Search"]')))
    search.click()

    search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Search input"]')))
    time.sleep(1)
    search_input.click()
    search_input.send_keys(f"#{hashtag}")

    first_hashtag = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Hashtag"]')))
    first_hashtag.click()