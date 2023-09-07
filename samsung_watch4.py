from bs4 import BeautifulSoup
import requests
import time



url = "https://www.jumia.co.ke/samsung-galaxy-watch4-classic-r890-46mm-smartwatch-black-48019461.html"


def track_price(url):
    try:
        response = requests.get(url, timeout=30)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            price_element = soup.find('span',class_="-b -ltr -tal -fs24 -prxs")

            if price_element:
                current_price = price_element.text.strip()
                return current_price
            else:
                return "Price not found!!!"
        else:
            return f"Failed to fetch webpage. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    

current_price = track_price(url)

print(f"Current Price: {current_price}")
