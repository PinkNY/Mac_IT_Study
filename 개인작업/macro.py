import logging
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# 로깅 설정
logging.basicConfig(filename=os.path.expanduser('~/Downloads/error.log'), level=logging.DEBUG)

def download_image(url, folder_path, num):
    try:
        response = requests.get(url)
        with open(os.path.join(folder_path, f'image_{num}.jpg'), 'wb') as file:
            file.write(response.content)
        return True
    except Exception as e:
        logging.error(f"Failed to download {url} - {e}")
        return False

def main(search_query, max_images=1000):
    logging.info("Setting up download folder...")
    folder_path = os.path.expanduser('~/Downloads/downloaded_images')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    logging.info("Setting up ChromeDriver path...")
    driver_path = "/usr/local/bin/chromedriver"  # 크롬 드라이버의 실제 경로

    logging.info("Starting Selenium...")
    driver = webdriver.Chrome(driver_path)
    driver.get('https://www.google.com/imghp')
    
    logging.info("Searching for images...")
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    logging.info("Scrolling to load images...")
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                break
        last_height = new_height

    logging.info("Extracting image URLs...")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    img_tags = soup.find_all('img', class_='rg_i')

    count = 0
    for img_tag in img_tags:
        img_url = img_tag.get('src') or img_tag.get('data-src')
        if img_url:
            if download_image(img_url, folder_path, count):
                count += 1
                if count >= max_images:
                    break

    driver.quit()
    logging.info(f"Downloaded {count} images to {folder_path}")

if __name__ == '__main__':
    search_query = '인터넷 밈'  # 또는 '짤방'
    logging.info(f"Starting search for {search_query}...")
    main(search_query)
    logging.info("Search completed.")