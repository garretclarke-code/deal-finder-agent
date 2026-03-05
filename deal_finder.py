import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bizbuysell.com/georgia-businesses-for-sale/?q=Y2Zmcm9tPTc1MDAwMCZjZnRvPTMwMDAwMDA="

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

titles = []
links = []

for listing in soup.find_all("a", href=True):
    href = listing["href"]

    if "/business-for-sale/" in href:
        title = listing.get_text(strip=True)

        if title:
            link = "https://www.bizbuysell.com" + href
            titles.append(title)
            links.append(link)

data = pd.DataFrame({
    "Business": titles,
    "Link": links
}).drop_duplicates()

data.to_csv("business_leads.csv", index=False)

print("Found", len(data), "listings")
print("Done. Leads saved to business_leads.csv")
