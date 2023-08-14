import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error downloading page: {e}")
        return None

def save_page(url, content):
    page_name = url.split("/")[-1] or "index.html"
    with open(page_name, "wb") as f:
        f.write(content)

def download_website(base_url):
    base_response = download_page(base_url)
    if base_response:
        save_page(base_url, base_response)
        base_soup = BeautifulSoup(base_response, "html.parser")

        for link in base_soup.find_all("a", href=True):
            link_url = urljoin(base_url, link["href"])
            if base_url in link_url:
                link_response = download_page(link_url)
                if link_response:
                    save_page(link_url, link_response)
                    print(f"Downloaded: {link_url}")

base_url = "https://pyflo.net/"
download_website(base_url)
