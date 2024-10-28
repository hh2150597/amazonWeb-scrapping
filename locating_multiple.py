from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
# driver.get(f"https://www.amazon.in/s?k={query}&crid=XFGU4EUBZF6J&sprefix=laptop%2Caps%2C293&ref=nb_sb_noss_2")
for i in range(1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=XFGU4EUBZF6J&qid=1729675086&sprefix={query}%2Caps%2C293&ref=sr_pg_{i}")
    elems = driver.find_elements(By.CLASS_NAME, "puisg-row")
    print(f'{len(elems)} items found')
    for elem in elems:
        print(elem.get_attribute("outerHTML"))
    # print(elem.text)
    time.sleep(2)
    driver.close()