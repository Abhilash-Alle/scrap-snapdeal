from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def set_driver():
    s=Service("C:/Windows/chromedriver.exe")
    driver=webdriver.Chrome(service=s)
    return driver

def search_items(driver,product):
    url="https://www.snapdeal.com/"
    driver.get(url)
    wait=WebDriverWait(driver,10)

    search=wait.until(EC.presence_of_element_located((By.XPATH,"""//input[@id='search-box-input']""")))
    search.click()
    search.send_keys(product)
    search.send_keys(Keys.ENTER)

def load_items(driver):
    wait = WebDriverWait(driver, 10)

    height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)

        try:
            next_btn = wait.until(
                EC.element_to_be_clickable((By.ID, "see-more-products"))
            )
            driver.execute_script("arguments[0].click();", next_btn)
        except:
            break

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == height:
            break
        height = new_height

def extract_items(driver):
    block=driver.find_elements(By.XPATH,"""//div[contains(@class,'col-xs-6  favDp product-tuple-listing js-tuple ')]""")
    data=[]
    for b in block:
       try:
           name=b.find_element(By.XPATH,".//p[contains(@class,'product-title')]")
           name1=name.text.strip()
           title=name1
       except:
           title="no title"

       try:
           rate=b.find_element(By.XPATH,".//span[contains(@class,'lfloat product-price')]")
           rate1=rate.text.strip()
           prices=rate1
       except:
           prices="no price"

       try:
           rating=b.find_element(By.XPATH,".//p[contains(@class,'product-rating-count')]")
           rating1=rating.text.strip()
           no_of_ratings=rating1
       except:
           no_of_ratings="no rating"

       try:
           dis=b.find_element(By.XPATH,".//div[contains(@class,'product-discount')]")
           dis1=dis.text.strip()
           discount=dis1
       except:
           discount="no discount"

       data.append({
         "title":title,
         "price":prices,
         "rating":no_of_ratings,
         "discount":discount
        })
    return data

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    print(len(df))
    df.to_csv(filename, index=False)

def main():
    driver=set_driver()
    try:
        search_items(driver,"mens watches")
        load_items(driver)
        data=extract_items(driver)
        save_to_csv(data,"snapdeal_scaper2.csv")
    finally:
        driver.quit()
        
main()
