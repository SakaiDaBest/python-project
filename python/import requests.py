import requests
from bs4 import BeautifulSoup
import os
import re

def scrape_bing_images(search_query, num_images=10):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = search_query.replace(" ", "_")
    save_path = os.path.join(desktop, folder_name)
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    search_url = f"https://www.bing.com/images/search?q={search_query.replace(' ', '+')}&form=HDRSC2"

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch page")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    
    images = soup.find_all("a", {"class": "iusc"})
    count = 0

    for img_tag in images:
        m = img_tag.get("m")
        if m:
            match = re.search(r'"murl":"(.*?)"', m)
            if match:
                img_url = match.group(1)
                try:
                    img_data = requests.get(img_url, timeout=5)
                    img_format = img_url.split('.')[-1].split('?')[0]

                    if img_format.lower() not in ['jpg', 'jpeg', 'png']:
                        img_format = 'jpg'

                    file_path = os.path.join(save_path, f"{search_query}_{count}.{img_format}")
                    with open(file_path, 'wb') as f:
                        f.write(img_data.content)
                    
                    print(f"Downloaded {img_url}")
                    count += 1

                    if count >= num_images:
                        break
                except Exception as e:
                    print(f"Could not download {img_url} - {e}")

    if count == 0:
        print("No images found.")
    else:
        print(f"\n{count} images downloaded into folder '{save_path}'.")

scrape_bing_images("porn", num_images=100)
