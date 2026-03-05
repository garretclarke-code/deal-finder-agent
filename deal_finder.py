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

# find listing cards
for card in soup.select("a[href*='/business-for-sale/']"):
    title = card.get_text(strip=True)
    link = card.get("href")

    if title and link:
        if not link.startswith("http"):
            link = "https://www.bizbuysell.com" + link

        titles.append(title)
        links.append(link)

data = pd.DataFrame({
    "Business": titles,
    "Link": links
}).drop_duplicates()

data.to_csv("business_leads.csv", index=False)

print("Found", len(data), "listings")
print("Done. Leads saved to business_leads.csv")
