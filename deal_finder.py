import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bizbuysell.com/georgia-businesses-for-sale/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

titles = []
links = []

for listing in soup.find_all("a", href=True):
    if "/business-for-sale/" in listing["href"]:
        titles.append(listing.text.strip())
        links.append("https://www.bizbuysell.com" + listing["href"])

data = pd.DataFrame({
    "Business": titles,
    "Link": links
})

data = data.drop_duplicates()

data.to_csv("business_leads.csv", index=False)

print("Done. Leads saved to business_leads.csv")
