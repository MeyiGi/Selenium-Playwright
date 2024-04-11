from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def login_to_instagram(my_username, my_password, wait):
    username = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username.click()
    username.send_keys(my_username)
    password.click()
    password.send_keys(my_password)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    time.sleep(6)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()