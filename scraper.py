import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

TARGET_URL = "https://us.mieleusa.com/spec-library/"
OUTPUT_FOLDER = "./manuals"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def download_manuals():
    response = requests.get(TARGET_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    count = 0
    for link in links:
        href = link['href']
        if href.endswith('.pdf'):
            full_url = urljoin(TARGET_URL, href)
            file_name = os.path.join(OUTPUT_FOLDER, href.split('/')[-1])
            pdf_content = requests.get(full_url).content
            with open(file_name, 'wb') as f:
                f.write(pdf_content)
            count += 1
            if count >= 5: break 
    return f"Downloaded {count} manuals."

if __name__ == "__main__":
    download_manuals()
