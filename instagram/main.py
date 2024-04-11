from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import wget
import os

from login import login_to_instagram
from find import find_by_hashtag

user_agent = "Mozilla/5.0 (Windows NT 8.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

def main():

    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en-GB")
    options.add_argument(f"user-agent={user_agent}")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.instagram.com/")

    wait = WebDriverWait(driver, 10)

    login_to_instagram("faybmi007@gmail.com", "sAmat.2004h", wait)
    find_by_hashtag("cats", wait)
    
    # Scrolling down
    driver.execute_script("window.scrollTo(0, 4000);")
    
    # Extacting images
    images = driver.find_elements(By.CSS_SELECTOR, "img")
    images = [image.get_attribute("src") for image in images[3:]]
    
    # Downloading images
    path = os.getcwd()
    path = os.path.join(path, f"cat_hashtag")
    os.mkdir(path)
    
    for index, image in enumerate(images):
        save_as = os.path.join(path, f"cat{index}.jpg")
        wget.download(image, save_as)

if __name__ == "__main__":
    main()