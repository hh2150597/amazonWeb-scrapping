from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() # Browser to work
query = "laptop"
file = 0 # HTML File numbers

# Read first 20 pages from  the search results
for i in range(1, 10):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=XFGU4EUBZF6J&sprefix=laptop%2Caps%2C293&ref=nb_sb_noss_2")
    elems = driver.find_elements(By.CLASS_NAME, "puisg-row")
    print(f'{len(elems)} items found')
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        # Store in data directry
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
    time.sleep(1)
driver.close()