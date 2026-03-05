from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

url = "https://www.bizbuysell.com/georgia-businesses-for-sale/"

options = Options()
options.add_argument("--headless")  # runs browser without opening a window

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(url)
time.sleep(5)  # allow page to fully load

titles = []
links = []

cards = driver.find_elements(By.CSS_SELECTOR, "a[href*='/business-for-sale/']")

for card in cards:
    title = card.text.strip()
    link = card.get_attribute("href")

    if title:
        titles.append(title)
        links.append(link)

driver.quit()

data = pd.DataFrame({
    "Business": titles,
    "Link": links
}).drop_duplicates()

data.to_csv("business_leads.csv", index=False)

print("Found", len(data), "listings")
print("Done. Leads saved to business_leads.csv")
