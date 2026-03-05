from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

url = "https://www.bizbuysell.com/georgia-businesses-for-sale/"

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(url)
time.sleep(8)  # allow listings to load

titles = []
links = []

# grab all listing cards
cards = driver.find_elements(By.CSS_SELECTOR, ".listingResult")

for card in cards:
    try:
        title_element = card.find_element(By.CSS_SELECTOR, "h2 a")
        title = title_element.text.strip()
        link = title_element.get_attribute("href")

        titles.append(title)
        links.append(link)

    except:
        pass

driver.quit()

data = pd.DataFrame({
    "Business": titles,
    "Link": links
}).drop_duplicates()

data.to_csv("business_leads.csv", index=False)

print("Found", len(data), "listings")
print("Done. Leads saved to business_leads.csv")
