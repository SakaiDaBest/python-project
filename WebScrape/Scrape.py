import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re

url = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_films#Highest-grossing_films'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first relevant table
table = soup.find('table', {'class': 'wikitable'})

# Extract all rows from the table
rows = table.find_all('tr')

# Loop through and print Rank, Title, Gross
open("Top_Grossing_Films.csv", "w").close()

for row in rows[1:]:  # skip header
    cells = row.find_all(['th', 'td'])
    rank = cells[0].get_text(strip=True)
    title = cells[2].get_text(strip=True)
    gross = cells[3].get_text(strip=True)
    grossn=gross[gross.find('$'):].strip()
    info = {
        "rank":rank,
        "title":title,
        "gross":grossn
    }
    print(f"{rank}: {title:<50} — {grossn}")
    df = pd.DataFrame([info])
    df.to_csv('Top_Grossing_Films.csv',mode='a',header=not os.path.exists('Top_Grossing_Films.csv') or os.stat('Top_Grossing_Films.csv').st_size==0,index=False)

