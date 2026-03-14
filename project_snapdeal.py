from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


s=Service("C:/Windows/chromedriver.exe")
driver=webdriver.Chrome(service=s)
url="https://www.snapdeal.com/"
driver.get(url)
wait=WebDriverWait(driver,10)

search=wait.until(EC.presence_of_element_located((By.XPATH,"""//input[@id='search-box-input']""")))
search.click()
search.send_keys("mens watches")
search.send_keys(Keys.ENTER)

height=driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    try:
       next=wait.until(EC.element_to_be_clickable((By.XPATH, """//div[@id='see-more-products']""")))
       driver.execute_script("arguments[0].scrollIntoView();", next)
       next.click()
    except:
        break
    print(height)
    time.sleep(2)
    newheight=driver.execute_script("return document.body.scrollHeight")
    if newheight == height:
        break
    else:
        height=newheight
    #wait.until(EC.element_to_be_clickable((By.XPATH,"""//div[@id='see-more-products']""")))
block=driver.find_elements(By.XPATH,"""//div[contains(@class,'col-xs-6  favDp product-tuple-listing js-tuple ')]""")
#blocks=block.strip()
print(len(block))
title=[]
price=[]
no_of_ratings=[]
discount=[]
for b in block:
    try:
        name=b.find_element(By.XPATH,".//p[contains(@class,'product-title')]")
        name1=name.text.strip()
        if name1:
           title.append(name1)
    except:
        title.append("no title")
    #print(name)
#print(len(name))
    try:
        rate=b.find_element(By.XPATH,".//span[contains(@class,'lfloat product-price')]")
        rate1=rate.text.strip()
        if rate1:
            price.append(rate1)
    except:
        price.append("no price")

    try:
        rating=b.find_element(By.XPATH,".//p[contains(@class,'product-rating-count')]")
        rating1=rating.text.strip()
        #if rating:
        no_of_ratings.append(rating1)
    except:
        no_of_ratings.append("no rating")

    try:
        dis=b.find_element(By.XPATH,".//div[contains(@class,'product-discount')]")
        dis1=dis.text.strip()
        discount.append(dis1)
    except:
        discount.append("no discount")

print(price)
print(title)
print(no_of_ratings)
print(discount)
df=pd.DataFrame({"product_names":title,"product_price":price,"product_rating":no_of_ratings,"product_discount":discount})
df.to_excel("scrap_project(snapdeal).xlsx",index=False)